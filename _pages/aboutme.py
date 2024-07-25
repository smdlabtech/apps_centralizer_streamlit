import streamlit as st
import app_styles as app_styles

#---------------------#
# Page : "aboutme.py"
#---------------------#
def page_aboutme():
    # Inclure le lien vers la bibliothèque Font Awesome
    st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """, unsafe_allow_html=True)

    # Afficher l'image avec app_styles
    app_styles.styles_img("portofolio-rond.jpg", caption="Passionate about AI🤖 [Data Scientist]", width=2, use_column_width=True, output_format='JPG')
    st.subheader("About Me : ✨ Data Scientist | Data Engineer ✨")     # Ajouter les icônes côte à côte
    st.markdown("""
        👋 Hi, I'm Daya
        I'm a data scientist with a passion for soccer and basketball.
        I'm passionate about Business Intelligence, data science and programming through the languages :
        Python, R, SQL, Javascript and tools like Power BI, Shiny, Streamlit, Excel VBA and Google Sheets (via Google Apps Script).
        And love working on topics of : Web Scraping, Chatbot Assistant, Text Mining & NLP and Web App Machine Learning, Deep Learning and AI Assistant. ⭐
    """, unsafe_allow_html=True)

    # Utiliser les fonctions pour ajouter du HTML (LinkedIn)
    app_styles.create_clickable_image("portofolio-rond.jpg", "https://www.linkedin.com/in/dayasylla/", "")

    # Générer le HTML pour les icônes
    linkedin_icon = app_styles.create_icon_link("fab fa-linkedin", "https://www.linkedin.com/in/dayasylla/", "#0e76a8")
    github_icon = app_styles.create_icon_link("fab fa-github", "https://github.com/smdlabtech", "black")

    # Ajouter les icônes côte à côte
    st.markdown(f"""
    <div style="display: flex; justify-content: left; gap: 10px;">
        {linkedin_icon}
        {github_icon}
    </div>
    """, unsafe_allow_html=True)


# MAIN ------------------#
if __name__ == "__main__":
    page_aboutme()
