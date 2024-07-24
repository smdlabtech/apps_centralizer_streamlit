import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import streamlit as st
from fuzzywuzzy import fuzz, process
from app_data_loader import load_lcl, load_brsma
from details_kpis import calculate_kpis
import app_styles


# Fonction pour regrouper les mots similaires
def group_similar_words(mots, seuil_similarite=80):
    groupes = []
    mots_restants = mots.copy()
    
    while mots_restants:
        mot = mots_restants.pop(0)
        groupe = [mot]
        similar_words = process.extract(mot, mots_restants, scorer=fuzz.ratio, limit=None)
        
        for similar_word, score in similar_words:
            if score >= seuil_similarite:
                groupe.append(similar_word)
                mots_restants.remove(similar_word)
                
        groupes.append(groupe)
    
    # Choisir un représentant pour chaque groupe (par exemple, le premier mot)
    representatives = {mot: groupe[0] for groupe in groupes for mot in groupe}
    return representatives


###################################
class LCLDetails:
    def __init__(self, data, kpis):
        self.data = data
        self.kpis = kpis
    
        ### Conversions ###
        self.data['operation'] = self.data['operation'].astype(str)
        mots_uniques = self.data['operation'].unique().tolist()
        self.representants = group_similar_words(mots_uniques)
        self.data['operation'] = self.data['operation'].map(self.representants)


    # Formatages Monetaire
    def format_currency(self, x, pos=None):
        """Formate les nombres en euros."""
        return f'{x:,.2f} €'

    ## AFFICHAGES #####################
    def display_summary(self):
        st.subheader("📊 LCL EVENTS :")
        

        # Filtrer les données en fonction du mois sélectionné
        lcl_year = self.data['anneeOp'].unique().tolist()
        lcl_selected_year = st.selectbox("Filter : Select a Year ", lcl_year)
        lcl_filtered_data = self.data[self.data['anneeOp'] == lcl_selected_year]

        with st.expander("**📈 Financial KPIs [LCL]**"):
            self.display_financial_kpis(lcl_filtered_data)
        
        with st.expander("**Distribution of transactions [LCL]**"):
            self.display_transaction_type_pie_chart(lcl_filtered_data)

        with st.expander("**Transactions over time [LCL]**"):
            self.display_transactions_over_time(lcl_filtered_data)

        with st.expander("**Transactions by Day of the Week [LCL]**"):
            self.display_transactions_by_day(lcl_filtered_data)

        with st.expander("**Distribution of Creditors/Debtors [LCL]**"):
            self.display_creditor_debtor(lcl_filtered_data)
            
        with st.expander("**🔍 Metrics by Operation [LCL]**"):
            self.display_lcl_operation_text_metrics(lcl_filtered_data)


    ### CALCULS DE FONCTIONS (params := "lcl_filtered_data")
    def display_transaction_type_pie_chart(self, lcl_filtered_data):
        lcl_pie_chart = px.pie(lcl_filtered_data, names='typeOp', values='montant', title='Distribution of transactions by type')
        st.plotly_chart(lcl_pie_chart)

    def display_transactions_over_time(self, lcl_filtered_data):
        lcl_filtered_data['dateOp'] = pd.to_datetime(lcl_filtered_data['dateOp'])
        lcl_line_chart = px.line(lcl_filtered_data, x='dateOp', y='montant', title='Transactions over time', markers=True)
        st.plotly_chart(lcl_line_chart)

    def display_transactions_by_day(self, lcl_filtered_data):
        lcl_filtered_data['dayOfWeek'] = lcl_filtered_data['dateOp'].dt.day_name()
        lcl_day_expenses = lcl_filtered_data.groupby('dayOfWeek')['montant'].sum().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
        lcl_bar_chart = px.bar(lcl_day_expenses, x=lcl_day_expenses.index, y='montant', title='Transactions par Jour de la Semaine')
        st.plotly_chart(lcl_bar_chart)

    def display_creditor_debtor(self, lcl_filtered_data):
        lcl_creditor_debtor = lcl_filtered_data['creancier'].value_counts()
        lcl_bar_chart_cd = px.bar(lcl_creditor_debtor, x=lcl_creditor_debtor.index, y=lcl_creditor_debtor.values, title='Distribution of Creditors/Debtors')
        st.plotly_chart(lcl_bar_chart_cd)
        
    def lcl_metrique_org(self, lcl_filtered_data):
        grouped_df = lcl_filtered_data.groupby('operation_texte').agg(
            nombre=('montant', 'size'),
            montant_total=('montant', 'sum'),
            montant_moyenne=('montant', 'mean'),
            montant_median=('montant', 'median'),
            montant_min=('montant', 'min'),
            montant_max=('montant', 'max')
        ).reset_index()
        return grouped_df


    ### Affichage des étiquettes de métriques : LCL ###
    def display_lcl_operation_text_metrics(self, lcl_filtered_data):
        
        # Utilisation de st.session_state pour stocker l'état de la recherche
        if 'search_query' not in st.session_state:
            st.session_state['search_query'] = ""

        # Bouton de réinitialisation pour la zone de recherche
        if st.button("🔄 Reset Filter LCL"):
            st.session_state['search_query'] = ""
            
        search_query = st.text_input("🔍 Search an operation [KPIs will be displayed in results]", value=st.session_state.get('search_query', ""), key='search_query', placeholder="Search an operation...")
        if search_query:
            filtered_metric_data = self.lcl_metrique_org(lcl_filtered_data)[self.lcl_metrique_org(lcl_filtered_data).apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)]
            occurrence = self.lcl_metrique_org(lcl_filtered_data).astype(str).apply(lambda x: x.str.contains(search_query, case=False)).sum().sum()
            st.write(f"*Search results [rows : {filtered_metric_data.shape[0]}, occurrences : {occurrence}]*")
            
            # Calcul des KPI à partir des données filtrées (KPI afficher au niveau des étiquettes)
            nombre_total = filtered_metric_data['nombre'].sum()
            montant_total = filtered_metric_data['montant_total'].sum()
            montant_moyenne = filtered_metric_data['montant_moyenne'].mean()
            montant_median = filtered_metric_data['montant_median'].median()
            montant_min = filtered_metric_data['montant_min'].min()
            montant_max = filtered_metric_data['montant_max'].max()

            # Diviser l'espace en colonnes pour les KPIs
            cols = st.columns(2)  # Deux colonnes par ligne
            
            #----------#
            with cols[0]:
                # Container pour chaque KPI
                app_styles.apply_css("style_kpi_metrics_lcl.css")
                
                #1). nombre_total
                st.markdown(f"""
                    <div class="kpi-container">
                        <div class="kpi-value">{nombre_total}</div>
                        <div class="kpi-label">Total operations</div>
                    </div>
                """, unsafe_allow_html=True)
                
                #2). montant_total
                st.markdown(f"""
                    <div class="kpi-container">
                        <div class="kpi-value">{self.format_currency(montant_total)}</div>
                        <div class="kpi-label">Total transactions</div>
                    </div>
                """, unsafe_allow_html=True)

                #3). montant_moyenne
                st.markdown(f"""
                    <div class="kpi-container">
                        <div class="kpi-value">{self.format_currency(montant_moyenne)}</div>
                        <div class="kpi-label">Average transaction</div>
                    </div>
                """, unsafe_allow_html=True)

            #-----------#
            with cols[1]:
                # Container pour chaque KPI
                app_styles.apply_css("style_kpi_metrics_lcl.css")
                
                #4). montant_median
                st.markdown(f"""
                    <div class="kpi-container">
                        <div class="kpi-value">{self.format_currency(montant_median)}</div>
                        <div class="kpi-label">Median transaction</div>
                    </div>
                """, unsafe_allow_html=True)

                #5). montant_min
                st.markdown(f"""
                    <div class="kpi-container">
                        <div class="kpi-value">{self.format_currency(montant_min)}</div>
                        <div class="kpi-label">Minimum transaction</div>
                    </div>
                """, unsafe_allow_html=True)

                #6). montant_max
                st.markdown(f"""
                    <div class="kpi-container">
                        <div class="kpi-value">{self.format_currency(montant_max)}</div>
                        <div class="kpi-label">Maximum transaction</div>
                    </div>
                """, unsafe_allow_html=True)

            # Affichage des données filtrées
            montant_columns = filtered_metric_data.filter(regex='^montant').columns
            for col in montant_columns:
                filtered_metric_data[col] = filtered_metric_data[col].apply(self.format_currency)
            st.dataframe(filtered_metric_data)

        
        ## Mise en forme de la sortie (LCL) ###
        else:
            kpi_data_lcl = self.lcl_metrique_org(lcl_filtered_data)
            montant_columns = kpi_data_lcl.filter(regex='^montant').columns
            for col in montant_columns:
                kpi_data_lcl[col] = kpi_data_lcl[col].apply(self.format_currency)
            st.dataframe(kpi_data_lcl)


    #-------------------------------#
    def display_financial_kpis(self, data):
        kpi_keys = [key for key in self.kpis.keys() if key.startswith('[LCL]')]
        num_kpis = len(kpi_keys)
        
        cols = st.columns(min(num_kpis, 4))  # Ajuster le nombre de colonnes selon les besoins
        for i, key in enumerate(kpi_keys):
            col = cols[i % 4]  # Ajuster le modulus selon le nombre de colonnes
            
            # determination de la couleur en fonction de la valeur de self.kpis[key] 
            value = round(self.kpis[key], 2)

            #-------#
            # Container pour chaque KPI ++ Affichage du KPI avec label et valeur formatée
            with col:
                app_styles.apply_css("style_kpi_financial.css")
                st.markdown(f'<div class="metric-container"><div class="metric-value">{value:,.2f} €</div><div class="metric-label">{key[6:]}</div></div>', unsafe_allow_html=True)




######################
class BRSMAExpenses:
    def __init__(self, data, kpis):
        self.data = data
        self.kpis = kpis

        # Convertir toutes les valeurs de la colonne 'organisme' en chaînes de caractères
        self.data['organisme'] = self.data['organisme'].astype(str)
        mots_uniques = self.data['organisme'].unique().tolist()
        self.representants = group_similar_words(mots_uniques)
        self.data['organisme'] = self.data['organisme'].map(self.representants)
        
        
    # Formatages des montants
    def format_currency(self, x, pos=None):
        """Formate les nombres en euros."""
        return f'{x:,.2f} €'

    ###  AFFICHAGES
    def display_summary(self):
        st.subheader("📊 BRSMA EVENTS :")
        
        # option = st.selectbox("BRSMA : Mois",("Email", "Home phone", "Mobile phone"))
        # st.write("You selected:", option)
        # brsma_link_icon = app_styles.load_img_clickable("logo-brsma-rmvbg.png", link="https://clients.boursobank.com/connexion/saisie-mot-de-passe", alt_text="BRSMA.fr", width=200)
        
        # # Filtrer les données en fonction du mois sélectionné
        # brsma_year = self.data['anneeOp'].unique().tolist()
        # brsma_year_selected_year = st.selectbox("Filter : Select a Year ", brsma_year)
        # brsma_lcl_filtered_data = self.data[self.data['anneeOp'] == brsma_year_selected_year]

        
        with st.expander("**📈 Financial KPIs [BRSMA]**"):
            self.display_financial_kpis()

        with st.expander("**Expenses by Category [BRSMA]**"):
            self.display_expenses_by_category()

        with st.expander("**Average transaction per transaction [BRSMA]**"):
            self.display_average_transaction_transaction()

        with st.expander("**Top 5 Creditors [BRSMA]**"):
            self.display_top_suppliers()

        with st.expander("**Expenses by Transaction Type [BRSMA]**"):
            self.display_expenses_by_transaction_type()

        with st.expander("**Expenses over time [BRSMA]**"):
            self.display_expenses_over_time()

        with st.expander("**Expenses by Day of the Week [BRSMA]**"):
            self.display_expenses_by_day()

        with st.expander("**🔍 Metrics by Organization [BRSMA]**"):
            self.display_organism_metrics()



    ###  CALCULS DE FONCTIONS
    def display_expenses_by_category(self):
        fig = px.pie(self.data, names='categorie', values='montant', title=' Breakdown of expenditure by category')
        st.plotly_chart(fig)

    def display_average_transaction_transaction(self):
        average_montant = self.data['montant'].mean()
        fig = go.Figure(data=go.Indicator(
            mode="gauge+number+delta",
            value=average_montant,
            delta={'reference': self.data['montant'].median(), 'increasing': {'color': "red"}},
            title={'text': "Average transaction per transaction"},
            domain={'x': [0, 1], 'y': [0, 1]}
        ))
        st.plotly_chart(fig)

    def display_top_suppliers(self):
        top_suppliers = self.data.groupby('organisme')['montant'].sum().nlargest(5)
        fig = px.bar(top_suppliers, x=top_suppliers.index, y='montant')
        st.plotly_chart(fig)

    def display_expenses_by_transaction_type(self):
        transaction_types = self.data['type_operation'].str.split(' ', n=1).str[0]  # Extrait le type de la transaction
        self.data['transactionType'] = transaction_types
        fig = px.histogram(self.data, x='transactionType', y='montant', title=' Expenses by Transaction Type')
        st.plotly_chart(fig)

    def display_expenses_over_time(self):
        self.data['dateOp'] = pd.to_datetime(self.data['dateOp'], errors='coerce')  # Convertir montant en numérique si nécessaire
        fig = px.line(self.data, x='dateOp', y='montant', title=' Expenses over time', markers=True)
        st.plotly_chart(fig)

    def display_expenses_by_day(self):
        self.data['dayOfWeek'] = self.data['dateOp'].dt.day_name()
        day_expenses = self.data.groupby('dayOfWeek')['montant'].sum().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
        fig = px.bar(day_expenses, x=day_expenses.index, y='montant', title=' Expenses by Day of the Week')
        st.plotly_chart(fig)

    #----------------------------------------------------------------------#   
    def display_organism_metrics(self):
        
        # Utilisation de st.session_state pour stocker l'état de la recherche
        if 'search_query_brsma' not in st.session_state:
            st.session_state['search_query_brsma'] = ""

        # Bouton de réinitialisation pour la zone de recherche
        if st.button("🔄 Reset Filter BSRMA"):
            st.session_state['search_query_brsma'] = ""
            
        search_query_brsma = st.text_input("🔍Search an organism [KPIs will be displayed in results]", value=st.session_state.get('search_query_brsma', ""), key='search_query_brsma', placeholder="Search an organism...")

        if search_query_brsma:
            lcl_filtered_data = self.brsma_metrique_org()[self.brsma_metrique_org().apply(lambda row: row.astype(str).str.contains(search_query_brsma, case=False).any(), axis=1)]
            occurrence = self.brsma_metrique_org().astype(str).apply(lambda x: x.str.contains(search_query_brsma, case=False)).sum().sum()
            st.write(f"*Search results [rows : {lcl_filtered_data.shape[0]}, occurrences : {occurrence}]*")
            
            # Calcul des KPI à partir des données filtrées
            total_organismes = lcl_filtered_data['organisme'].nunique()
            total_transactions = lcl_filtered_data['nombre'].sum()
            montant_total = lcl_filtered_data['montant_total'].sum()
            montant_moyenne = lcl_filtered_data['montant_moyenne'].mean()

            ### Affichages des étiquettes de KPI's : Diviser l'espace en colonnes pour les KPIs ###
            cols = st.columns(2)  # Deux colonnes par ligne
            
            
            #-----------#
            # Container pour chaque KPI ++ Stylisation des 'kpi-value' et 'kpi-label'
            with cols[0]:
                app_styles.apply_css("style_kpi_metrics_brsma.css")
                
                # total_organismes
                st.markdown(f"""
                    <div class="kpi-container">
                        <div class="kpi-value">{total_organismes}</div>
                        <div class="kpi-label">Total number of organizations</div>
                    </div>
                """, unsafe_allow_html=True)

                # total_transactions
                st.markdown(f"""
                    <div class="kpi-container">
                        <div class="kpi-value">{total_transactions}</div>
                        <div class="kpi-label">Total number of transactions</div>                        
                    </div>
                """, unsafe_allow_html=True)
                
                                
            #-----------#
            with cols[1]:
                # Stylisation des 'kpi-value' et 'kpi-label'
                app_styles.apply_css("style_kpi_metrics_brsma.css")
                
                # montant_total
                st.markdown(f"""
                    <div class="kpi-container">
                        <div class="kpi-value">{self.format_currency(montant_total)}</div>
                        <div class="kpi-label">Total transactions</div>
                    </div>
                """, unsafe_allow_html=True)

                # montant_moyenne
                st.markdown(f"""
                    <div class="kpi-container">
                        <div class="kpi-value">{self.format_currency(montant_moyenne)}</div>
                        <div class="kpi-label">Average transaction</div>
                    </div>
                """, unsafe_allow_html=True)

            # Affichage des données filtrées
            montant_columns = lcl_filtered_data.filter(regex='^montant').columns
            for col in montant_columns:
                lcl_filtered_data[col] = lcl_filtered_data[col].apply(self.format_currency)
            st.dataframe(lcl_filtered_data)
            
        
        #------------------------------#
        ## Mise en forme de la sortie ###
        else:
            data = self.brsma_metrique_org()
            montant_columns = data.filter(regex='^montant').columns
            for col in montant_columns:
                data[col] = data[col].apply(self.format_currency)
            st.dataframe(data)
    
    
    
    #-------------------------------#
    def display_financial_kpis(self):
        
        kpi_keys = [key for key in self.kpis.keys() if key.startswith('[BRSMA]')]
        num_kpis = len(kpi_keys)
        
        cols = st.columns(min(num_kpis, 4))  # Ajuster le nombre de colonnes selon les besoins
        for i, key in enumerate(kpi_keys):
            col = cols[i % 4]  # Ajuster le modulus selon le nombre de colonnes
            
            # determination de la couleur en fonction de la valeur de self.kpis[key]
            value = round(self.kpis[key], 2)
            
            with col:
            # Stylisation des 'kpi-value' et 'kpi-label' ++ Affichage du KPI avec label et valeur formatée
                app_styles.apply_css("style_kpi_metrics_brsma.css")
                st.markdown(f'<div class="metric-container"><div class="metric-value">{value:,.2f} €</div><div class="metric-label">{key[7:]}</div></div>', unsafe_allow_html=True)


    # Metric table (dataframe)
    def brsma_metrique_org(self):
        grouped_df = self.data.groupby('organisme').agg(
            nombre=('montant', 'size'),
            montant_total=('montant', 'sum'),
            montant_moyenne=('montant', 'mean'),
            montant_median=('montant', 'median'),
            montant_min=('montant', 'min'),
            montant_max=('montant', 'max')
        ).reset_index()
        return grouped_df


#--------------------#
# Fonction principale
#--------------------#
def page_details():
    lcl_data = load_lcl()
    brsma_data = load_brsma()

    # Calcul des KPIs
    kpis = calculate_kpis(lcl_data, brsma_data)

    ## 1. Section LCL
    lcl_details = LCLDetails(lcl_data, kpis)
    lcl_details.display_summary()

    ## 2. Section BRSMA
    brsma_expenses = BRSMAExpenses(brsma_data, kpis)
    brsma_expenses.display_summary()

