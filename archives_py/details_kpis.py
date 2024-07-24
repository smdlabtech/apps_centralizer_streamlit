import pandas as pd

def calculate_kpis(data_lcl, data_brsma):
    # Nettoyage des données
    data_lcl['montant'] = pd.to_numeric(data_lcl['montant'], errors='coerce').fillna(0)
    data_brsma['montant'] = pd.to_numeric(data_brsma['montant'], errors='coerce').fillna(0)

    # KPI pour LCL
    total_crediteur_lcl = data_lcl[data_lcl['montant'] > 0]['montant'].sum()
    total_debiteur_lcl = data_lcl[data_lcl['montant'] < 0]['montant'].sum()
    nombre_transactions_lcl = len(data_lcl)
    solde_moyen_lcl = data_lcl['montant'].mean()
    max_transaction_lcl = data_lcl['montant'].max()
    min_transaction_lcl = data_lcl['montant'].min()
    variance_lcl = data_lcl['montant'].var()

    # Nouveaux KPIs pour LCL
    lcl_growth_rate = (data_lcl['montant'].iloc[-1] - data_lcl['montant'].iloc[0]) / data_lcl['montant'].iloc[0] * 100
    lcl_liquidity_ratio = data_lcl[data_lcl['montant'] > 0]['montant'].sum() / abs(data_lcl[data_lcl['montant'] < 0]['montant'].sum())

    # KPI pour BRSMA
    montant_total_brsma = data_brsma['montant'].sum()
    montant_moyen_brsma = data_brsma['montant'].mean()
    nombre_transactions_brsma = len(data_brsma)
    solde_moyen_brsma = data_brsma['montant'].mean()

    # Nouveaux KPIs pour BRSMA
    brsma_growth_rate = (data_brsma['montant'].iloc[-1] - data_brsma['montant'].iloc[0]) / data_brsma['montant'].iloc[0] * 100
    brsma_profitability_ratio = data_brsma[data_brsma['montant'] > 0]['montant'].sum() / abs(data_brsma[data_brsma['montant'] < 0]['montant'].sum())

    # Ajout des KPIs saisonniers pour LCL
    data_lcl['month'] = data_lcl['dateOp'].dt.month
    data_lcl['season'] = data_lcl['dateOp'].dt.month.map({1:1, 2:1, 3:1, 4:2, 5:2, 6:2, 7:3, 8:3, 9:3, 10:4, 11:4, 12:4})

    monthly_totals = data_lcl.groupby('month')['montant'].sum()
    seasonal_totals = data_lcl.groupby('season')['montant'].sum()
    monthly_transaction_counts = data_lcl.groupby('month')['montant'].count()
    seasonal_transaction_counts = data_lcl.groupby('season')['montant'].count()

    # Dictionnaire des KPIs
    kpis = {
        '[LCL] Total Creditor': total_crediteur_lcl,
        '[LCL] Total Debtor': total_debiteur_lcl,
        '[LCL] Number of Transactions': nombre_transactions_lcl,
        '[LCL] Average Balance': solde_moyen_lcl,
        '[LCL] Max Transaction': max_transaction_lcl,
        '[LCL] Min Transaction': min_transaction_lcl,
        '[LCL] Variance': variance_lcl,
        
        '[BRSMA] Total Amount': montant_total_brsma,
        '[BRSMA] Average Amount': montant_moyen_brsma,
        '[BRSMA] Number of Transactions': nombre_transactions_brsma,
        '[BRSMA] Average Balance': solde_moyen_brsma,
        
        '[LCL] Growth Rate (%)': lcl_growth_rate,
        '[LCL] Liquidity Ratio': lcl_liquidity_ratio,
        '[BRSMA] Growth Rate (%)': brsma_growth_rate,
        '[BRSMA] Profitability Ratio': brsma_profitability_ratio,
        
        # '[LCL] Monthly Amounts': monthly_totals,
        # '[LCL] Seasonal Amounts': seasonal_totals,
        # '[LCL] Monthly Transaction Counts': monthly_transaction_counts,
    }

    return kpis