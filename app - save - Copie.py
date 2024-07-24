import streamlit as st

# Titre de l'application
st.title("Centralisateur d'applications Streamlit")

# Description
st.write("Bienvenue sur le centralisateur de toutes mes applications Streamlit. Cliquez sur les liens ci-dessous pour accéder à chaque application.")

# Liste des applications avec leurs liens
apps = {
    "Application 1": "https://link_to_app1.streamlit.app",
    "Application 2": "https://link_to_app2.streamlit.app",
    "Application 3": "https://link_to_app3.streamlit.app",
    # Ajoutez plus d'applications ici
}

# Affichage des liens
for app_name, app_link in apps.items():
    st.markdown(f"- [{app_name}]({app_link})")

# Ajout d'une section de contact (facultatif)
st.write("## Contact")
st.write("Pour toute question ou suggestion, veuillez me contacter à [votre_email@example.com](mailto:votre_email@example.com).")

# Optionnel: Ajout de styles personnalisés
st.markdown(
    """
    <style>
    .reportview-container {
        background: #f0f0f0;
    }
    .sidebar .sidebar-content {
        background: #f0f0f0;
    }
    </style>
    """,
    unsafe_allow_html=True
)
