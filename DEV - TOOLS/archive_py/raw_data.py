import streamlit as st
import pandas as pd
import app_data_loader

# # Function to format float columns as currency
def format_currency(val):
    if isinstance(val, float):
        return f"{val:.2f} €"
    return val




######################################
# Fonction de formatage du montant
def format_euro(amount):
    """Format a number as Euro currency with thousand separators."""
    return f"{amount:,.2f} €".replace(",", " ")

# Classe pour afficher les détails LCL
class LCLDetails:
    def __init__(self, data):
        self.data = data

    def display_summary(self, search_query):
        with st.expander("🗄️ LCL Events : [raw data]"):
            # Initialisation de la session_state pour LCL search_query si elle n'existe pas
            if 'lcl_search_query' not in st.session_state:
                st.session_state['lcl_search_query'] = ""

            # Initialisation des dates minimales et maximales si elles n'existent pas
            if 'date_min_lcl' not in st.session_state:
                st.session_state['date_min_lcl'] = self.data["dateOp"].min().date()
            if 'date_max_lcl' not in st.session_state:
                st.session_state['date_max_lcl'] = self.data["dateOp"].max().date()

            col1, col2 = st.columns(2)
            with col1:
                # Bouton de réinitialisation pour LCL
                if st.button("🔄 Reset LCL Filters"):
                    st.session_state['lcl_search_query'] = ""
                    st.session_state['date_min_lcl'] = self.data["dateOp"].min().date()
                    st.session_state['date_max_lcl'] = self.data["dateOp"].max().date()
                    
                # Zone de recherche pour LCL avec placeholder
                lcl_search_query = st.text_input("🔎 Search in LCL", value=st.session_state['lcl_search_query'], key='lcl_search_query', placeholder="Enter search term...")


            with col2:
                # Calendrier interactif pour sélectionner la plage de dates
                date_min_lcl = st.date_input("date min. LCL :", min_value=self.data["dateOp"].min().date(), max_value=self.data["dateOp"].max().date(), value=st.session_state['date_min_lcl'], key='date_min_lcl')
                date_max_lcl = st.date_input("date max. LCL :", min_value=self.data["dateOp"].min().date(), max_value=self.data["dateOp"].max().date(), value=st.session_state['date_max_lcl'], key='date_max_lcl')

                # Mettre à jour les valeurs de session_state après sélection de la plage de dates
                if date_min_lcl != st.session_state['date_min_lcl']:
                    st.session_state['date_min_lcl'] = date_min_lcl
                if date_max_lcl != st.session_state['date_max_lcl']:
                    st.session_state['date_max_lcl'] = date_max_lcl

                # Filtrage des données par plage de dates sélectionnée
                filtered_data = self.data[
                    (self.data['dateOp'] >= pd.Timestamp(st.session_state['date_min_lcl'])) &
                    (self.data['dateOp'] <= pd.Timestamp(st.session_state['date_max_lcl']))
                ]


            # Filtrage des données LCL en fonction de la recherche
            if lcl_search_query:
                filtered_lcl_data = filtered_data[filtered_data.apply(lambda row: row.astype(str).str.contains(lcl_search_query, case=False).any(), axis=1)]
                occurrence_lcl = filtered_lcl_data.shape[0]

                montant_lcl = round(filtered_lcl_data['montant'].sum(), 2)
                
                # montant_lcl_str = format_euro(montant_lcl)
                # FORMATAGE EN AFFICHAGES  : Afficher les résultats de la recherche, les occurrences et le montant total
                # st.write(f"*Search results [rows : {occurrence_lcl}, sum montant : {montant_lcl_str}]*")
                
                st.write(f"*Search results [rows : {occurrence_lcl}]*")
                formatted_lcl_data = filtered_lcl_data.copy()
                formatted_lcl_data['montant_calc'] = formatted_lcl_data['montant']
                formatted_lcl_data['montant'] = formatted_lcl_data['montant'].apply(format_euro)
                
                #----------------------------------------------------------------------------------------------------------------------#                                
                formatted_lcl_data['mois_op_nom'] = formatted_lcl_data['dateOp'].dt.strftime('%b')
                formatted_lcl_data['mois_op'] = formatted_lcl_data['dateOp'].dt.strftime('%m').astype(str).str.zfill(2)
                formatted_lcl_data['jours_Op'] = formatted_lcl_data['dateOp'].dt.day
                #------------------------------------------------------------------------------------------------------------------------#
                
                st.write(formatted_lcl_data)
            else:
                formatted_lcl_data = filtered_data.copy()
                formatted_lcl_data['montant_calc'] = formatted_lcl_data['montant']
                formatted_lcl_data['montant'] = formatted_lcl_data['montant'].apply(format_euro)
                
                #------------------------------------------------------------------------------------------------------------------#                                
                formatted_lcl_data['mois_op_nom'] = formatted_lcl_data['dateOp'].dt.strftime('%b')
                formatted_lcl_data['mois_op'] = formatted_lcl_data['dateOp'].dt.strftime('%m').astype(str).str.zfill(2)
                formatted_lcl_data['jours_Op'] = formatted_lcl_data['dateOp'].dt.day
                #---------------------------------------------------------------------------------------------------------------------#
                
                st.write(formatted_lcl_data)

            # Affichage de statistiques supplémentaires pour LCL
            st.write(f"***Table** [rows, columns]: [{formatted_lcl_data.shape[0]}, {formatted_lcl_data.shape[1]}]*")
            total_montant_montant_calc = f"{round(formatted_lcl_data['montant_calc'].sum(), 2):,.2f}".replace(",", " ").replace(",", ".")
            st.write(f"*Total montant: {total_montant_montant_calc} €*")    
            
            st.write(f"*dateOp [min: {formatted_lcl_data['dateOp'].min()}]*")
            st.write(f"*dateOp [max: {formatted_lcl_data['dateOp'].max()}]*")

            # Affichage des types de colonnes pour LCL
            col1, col2 = st.columns(2)
            with col1:
                column_labels = ['Column Name', "Type"]
                lcl_data_dtypes = formatted_lcl_data.dtypes.reset_index()
                lcl_data_dtypes.columns = column_labels
                st.write('*describe [results]: columns types*')
                st.dataframe(lcl_data_dtypes)

            with col2:
                st.write('*describe [results]: quantitative variables*', formatted_lcl_data.describe())



########################################
# Classe pour afficher les details BRSMA
class BRSMAExpenses:
    def __init__(self, data):
        self.data = data
        self.data["dateOp"] = pd.to_datetime(self.data["dateOp"])  # Assurez-vous que les dates sont converties en Timestamp

    def display_summary(self, search_query):
        with st.expander("🗄️ BRSMA Events : [raw data]"):
            # Initialisation de la session_state pour BRSMA search_query si elle n'existe pas
            if 'brsma_search_query' not in st.session_state:
                st.session_state['brsma_search_query'] = ""

            # Initialisation des dates minimales et maximales si elles n'existent pas
            if 'date_min_brsma' not in st.session_state:
                st.session_state['date_min_brsma'] = self.data["dateOp"].min().date()
            if 'date_max_brsma' not in st.session_state:
                st.session_state['date_max_brsma'] = self.data["dateOp"].max().date()

            col1, col2 = st.columns(2)
            with col1:
                # Bouton de réinitialisation pour BRSMA
                if st.button("🔄 Reset BRSMA Filters"):
                    st.session_state['brsma_search_query'] = ""
                    st.session_state['date_min_brsma'] = self.data["dateOp"].min().date()
                    st.session_state['date_max_brsma'] = self.data["dateOp"].max().date()
                    
                # Zone de recherche pour BRSMA avec placeholder
                brsma_search_query = st.text_input("🔎 Search in BRSMA", value=st.session_state['brsma_search_query'], key='brsma_search_query', placeholder="Enter search term...")

            with col2:
                # Calendrier interactif pour sélectionner la plage de dates
                date_min_brsma = st.date_input("Date minimum BRSMA", min_value=self.data["dateOp"].min().date(), max_value=self.data["dateOp"].max().date(), value=st.session_state['date_min_brsma'], key='date_min_brsma')
                date_max_brsma = st.date_input("Date maximum BRSMA", min_value=self.data["dateOp"].min().date(), max_value=self.data["dateOp"].max().date(), value=st.session_state['date_max_brsma'], key='date_max_brsma')

                # Mettre à jour les valeurs de session_state après sélection de la plage de dates
                if date_min_brsma != st.session_state['date_min_brsma']:
                    st.session_state['date_min_brsma'] = date_min_brsma
                if date_max_brsma != st.session_state['date_max_brsma']:
                    st.session_state['date_max_brsma'] = date_max_brsma

                # Filtrage des données par plage de dates sélectionnée et recherche par texte
                filtered_data = self.data[
                    (self.data['dateOp'] >= pd.Timestamp(st.session_state['date_min_brsma'])) &
                    (self.data['dateOp'] <= pd.Timestamp(st.session_state['date_max_brsma'])) &
                    (self.data.apply(lambda row: row.astype(str).str.contains(brsma_search_query, case=False).any(), axis=1))
                ]

            # Filtrage des données BRSMA en fonction de la recherche
            if brsma_search_query:
                filtered_brsma_data = filtered_data[filtered_data.apply(lambda row: row.astype(str).str.contains(brsma_search_query, case=False).any(), axis=1)]
                occurrence_brsma = filtered_brsma_data.shape[0]
                montant_brsma = round(filtered_brsma_data['montant'].sum(), 2)
                # montant_brsma_str = format_euro(montant_brsma)

                # Afficher les résultats de la recherche, les occurrences et le montant total
                st.write(f"*Search results [rows : {occurrence_brsma}]*")
                # st.write(f"*Search results [rows : {occurrence_brsma}, sum montant : {montant_brsma_str}]*")
                formatted_brsma_data = filtered_brsma_data.copy()
                formatted_brsma_data['montant_calc'] = formatted_brsma_data['montant']
                formatted_brsma_data['montant'] = formatted_brsma_data['montant'].apply(format_euro)
                st.write(formatted_brsma_data)

            else:
                formatted_brsma_data = filtered_data.copy()
                formatted_brsma_data['montant_calc'] = formatted_brsma_data['montant']
                formatted_brsma_data['montant'] = formatted_brsma_data['montant'].apply(format_euro)
                st.write(formatted_brsma_data)

            # Affichage de statistiques supplémentaires pour BRSMA
            st.write(f"***Table** [rows, columns]: [{formatted_brsma_data.shape[0]}, {formatted_brsma_data.shape[1]}]*")
            total_montant_montant_calc = f"{round(formatted_brsma_data['montant_calc'].sum(), 2):,.2f}".replace(",", " ").replace(",", ".")
            st.write(f"*Total montant: {total_montant_montant_calc} €*")  
                        
            st.write(f"*dateOp [min: {formatted_brsma_data['dateOp'].min()}]*")
            st.write(f"*dateOp [max: {formatted_brsma_data['dateOp'].max()}]*")

            # Affichage des types de colonnes pour BRSMA
            col1, col2 = st.columns(2)
            with col1:
                column_labels = ['Column Name', "Type"]
                brsma_data_dtypes = formatted_brsma_data.dtypes.reset_index()
                brsma_data_dtypes.columns = column_labels
                st.write('*describe [results]: columns types*')
                st.dataframe(brsma_data_dtypes)

            with col2:
                st.write('*describe [results]: quantitative variables*', formatted_brsma_data.describe())


#---------------------------------------#
# Fonction principale pour rendre la page
def page_raw_data():
    st.subheader("🗄️ Raw Data")

    # Initialisation des session_state pour les recherches si elles n'existent pas
    if 'lcl_search_query' not in st.session_state:
        st.session_state['lcl_search_query'] = ""
    if 'brsma_search_query' not in st.session_state:
        st.session_state['brsma_search_query'] = ""

    # Bouton de réinitialisation global
    if st.button("🔄 Reset All Filters"):
        st.session_state['lcl_search_query'] = ""
        st.session_state['brsma_search_query'] = ""

    # Chargement des données LCL et BRSMA
    lcl_data = app_data_loader.load_lcl()
    brsma_data = app_data_loader.load_brsma()

    # Affichage des details LCL
    lcl_details = LCLDetails(lcl_data)
    lcl_details.display_summary(st.session_state['lcl_search_query'])

    # Affichage des details BRSMA
    brsma_expenses = BRSMAExpenses(brsma_data)
    brsma_expenses.display_summary(st.session_state['brsma_search_query'])




#------------------------#
#      MAIN
#------------------------#
if __name__ == "__main__":
    page_raw_data()
