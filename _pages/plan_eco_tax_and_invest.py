import streamlit as st
import pandas as pd
import app_data_loader
import streamlit as st
import plotly.express as px




#----------------------------------#
# Plan Economic Tax And Investments
#----------------------------------#
class PlanEcoTaxAndInvest:
    def __init__(self, income):
        self.income = income
        self.expenses = self.calculate_expenses()
        self.investments = self.calculate_investments()
        self.tax_optimization = self.calculate_tax_optimization()
        self.long_term_planning = self.calculate_long_term_planning()


    def calculate_expenses(self):
        return {
            "Loyer": self.income * 0.3,
            "Charges": self.income * 0.05,
            "Alimentation": self.income * 0.15,
            "Transport": self.income * 0.05,
            "Épargne": self.income * 0.2,
            "Loisirs": self.income * 0.1,
            "Autres": self.income * 0.15
        }


    def calculate_investments(self):
        return {
            "Livret A": 0.5 * self.income * 0.2,
            "Plan Epargne en Action  (PEA)": 0.2 * self.income * 0.2,
            "Assurance-vie": 0.2 * self.income * 0.2,
            "Plan d'Épargne Retraite (PER)": 0.1 * self.income * 0.2
        }


    def calculate_tax_optimization(self):
        annual_income = self.income * 12
        tax_rate = 0.3  # Hypothetical tax rate
        base_tax = annual_income * tax_rate
        return {
            "base_tax": base_tax,
            "donations": 100,
            "per_contribution": 1000,
            "tax_reduction": 100 * 0.66 + 1000 * tax_rate,
            "optimized_tax": max(0, base_tax - (100 * 0.66 + 1000 * tax_rate))
        }


    def calculate_long_term_planning(self):
        monthly_savings = 0.15 * self.income
        years_to_retirement = 30
        expected_return = 5
        future_value = monthly_savings * 12 * ((1 + expected_return / 100) ** years_to_retirement - 1) / (expected_return / 100)
        return {
            "monthly_savings": monthly_savings,
            "years_to_retirement": years_to_retirement,
            "expected_return": expected_return,
            "future_value": future_value
        }


    def show_budget(self):
        st.header("Budget Mensuel")
        fig = px.pie(values=self.expenses.values(), names=self.expenses.keys(), title="Répartition du Budget")
        st.plotly_chart(fig)

        st.subheader("Ajustez votre budget")
        for category, amount in self.expenses.items():
            self.expenses[category] = st.slider(f"{category} (%)", 0, 100, int(amount / self.income * 100)) * self.income / 100

        fig_adjusted = px.pie(values=self.expenses.values(), names=self.expenses.keys(), title="Budget Ajusté")
        st.plotly_chart(fig_adjusted)


    def show_investments(self):
        st.header("Stratégie d'Investissement")
        for option, amount in self.investments.items():
            st.write(f"{option}: {amount:.2f} €")

        st.subheader("Simulateur de croissance")
        years = st.slider("Nombre d'années", 1, 30, 10)
        interest_rate = st.slider("Taux d'intérêt annuel (%)", 1, 10, 5)

        total_investment = sum(self.investments.values()) * 12 * years
        future_value = total_investment * (1 + interest_rate / 100) ** years

        st.write(f"Valeur future estimée: {future_value:.2f} €")


    def show_tax_optimization(self):
        st.header("Optimisation Fiscale")
        st.write(f"Impôt estimé sans optimisation: {self.tax_optimization['base_tax']:.2f} €")

        donations = st.slider("Dons aux associations (€)", 0, 1000, self.tax_optimization['donations'])
        per_contribution = st.slider("Contribution au Plan d'Épargne Retraite (PER) (€)", 0, 5000, self.tax_optimization['per_contribution'])

        tax_reduction = donations * 0.66 + per_contribution * 0.3
        optimized_tax = max(0, self.tax_optimization['base_tax'] - tax_reduction)

        st.write(f"Impôt estimé après optimisation: {optimized_tax:.2f} €")
        st.write(f"Économie d'impôt: {self.tax_optimization['base_tax'] - optimized_tax:.2f} €")


    def show_long_term_planning(self):
        st.header("Planification à Long Terme")
        monthly_savings = st.slider("Épargne mensuelle (€)", 0, self.income, int(self.long_term_planning['monthly_savings']))
        years_to_retirement = st.slider("Années avant la retraite", 5, 40, self.long_term_planning['years_to_retirement'])
        expected_return = st.slider("Rendement annuel espéré (%)", 1, 10, self.long_term_planning['expected_return'])

        future_value = monthly_savings * 12 * ((1 + expected_return / 100) ** years_to_retirement - 1) / (expected_return / 100)
        st.write(f"Capital estimé à la retraite: {future_value:.2f} €")

        years = list(range(years_to_retirement + 1))
        capital = [monthly_savings * 12 * ((1 + expected_return / 100) ** y - 1) / (expected_return / 100) for y in years]

        fig = px.line(x=years, y=capital, labels={'x': 'Années', 'y': 'Capital'}, title="Évolution du Capital Retraite")
        st.plotly_chart(fig)




#---------------------------------#
# Fonction principale
#---------------------------------#
def page_plan_eco_tax_and_invest():
    st.title("Planificateur Financier")
    
    income = st.sidebar.number_input("Revenu mensuel net", value=2700)
    plan = PlanEcoTaxAndInvest(income)
    tabs = st.tabs(["Budget", "Investissements", "Optimisation Fiscale", "Planification"])
    
    # getting tabs by 'tab' indexes
    with tabs[0]:
        plan.show_budget()
    
    with tabs[1]:
        plan.show_investments()
    
    with tabs[2]:
        plan.show_tax_optimization()
    
    with tabs[3]:
        plan.show_long_term_planning()


#------------------------#
#   Call Principale
#------------------------#
if __name__ == "__main__":
    page_plan_eco_tax_and_invest()