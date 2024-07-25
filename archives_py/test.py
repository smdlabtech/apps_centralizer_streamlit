import streamlit as st
import os
from streamlit_carousel import carousel
import app_styles



# Initialiser l'état de session pour la configuration de la page
if 'page_layout' not in st.session_state:
    st.session_state.page_layout = 'wide'  # Layout par défaut

# Configuration initiale de la page
st.set_page_config(
    page_title="Apps Centralizer",
    page_icon="👨‍💻",
    layout=st.session_state.page_layout,
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.example.com/help',
        'Report a bug': 'https://www.example.com/bug',
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# Functions 
def display_html(file_name):
    try:
        html_content = app_styles.load_html(file_name)
        st.markdown(html_content, unsafe_allow_html=True)
    except FileNotFoundError as e:
        st.error(f"Erreur: {e}")

def display_js(file_name):
    try:
        js_content = app_styles.load_js(file_name)
        st.markdown(js_content, unsafe_allow_html=True)
    except FileNotFoundError as e:
        st.error(f"Erreur: {e}")

def apply_js(file_name):
    try:
        js_content = app_styles.load_js(file_name)
        st.write(js_content, unsafe_allow_html=True)
    except FileNotFoundError as e:
        st.error(f"Erreur: {e}")


#--------------#
## Set Carrousel 
def setup_carousel(image_folder, start_index, end_index, carousel_app_list):
    # Générer les chemins des images
    images = [f"{image_folder}/img ({i}).JPG" for i in range(start_index, end_index + 1)]
    
    # Vérifier que les images existent
    for image in images:
        if not os.path.exists(image):
            st.error(f"Image non trouvée: {image}")
    
    # Définir les éléments du carrousel avec les images et les liens correspondants
    carousel_items = [
        {"img": images[i], "caption": item["caption"], "title": item["title"], "text": item["text"], "url": item["url"]}
        for i, item in enumerate(carousel_app_list)
    ]
    
    # Afficher le carrousel
    return carousel(carousel_items)




## Carousel images 
carousel_app_list = [
    {"caption": "Expenses Tracker", "title": "Expenses Tracker", "text": "Expenses Tracker", "url": "https://expensestrackerr.streamlit.app/"},
    {"caption": "Professional Data Engineer Quizes", "title": "Professional Data Engineer Quizes", "text": "Professional Data Engineer Quizes", "url": "https://quizappdelpgcp.streamlit.app/"},
    {"caption": "Analyse Immo-info", "title": "Analyse Immo-info", "text": "Analyse Immo-info", "url": "https://analyse-immo-info.streamlit.app/"},
    {"caption": "Predicting the Creditworthiness of Bank Customers", "title": "Predicting the Creditworthiness of Bank Customers", "text": "Predicting the Creditworthiness of Bank Customers", "url": "https://cyclientscreditworthinesspyapp-dq6q6sm24bakhp34memfrr.streamlit.app/"}
]



## Chemin vers les images et afficher le carrousel
setup_carousel("assets/img", 1, 4, carousel_app_list)


#---------#
# MAIN
#---------#
def main():
    st.markdown("<h1 style='text-align: center;'>✨Apps Centralizer✨</h1>", unsafe_allow_html=True)

    with st.sidebar:
        st.image("assets/img/senlab_ia_gen_rmv_bgrd.png", caption="🇸🇳 SenLab IA 🇫🇷", use_column_width=True)
        st.sidebar.markdown("<h1 style='text-align: left; color: grey;'>Sidebar Panel : </h1>", unsafe_allow_html=True)

        # Sidebar gestions
        if "page" not in st.session_state:
            st.session_state.page = "🏠HomePage"
            st.session_state.page_layout = "wide"

        # Ajout du bouton radio pour choisir la largeur de la page
        page_size_option = st.sidebar.radio("Page size", ["Wide", "Normal"])
        
        # Vérifiez si la configuration de la page doit être mise à jour
        if page_size_option == "Normal" and st.session_state.page_layout != "centered":
            st.session_state.page_layout = "centered"
            st.experimental_rerun()
            
        elif page_size_option == "Wide" and st.session_state.page_layout != "wide":
            st.session_state.page_layout = "wide"
            st.experimental_rerun()

    # Description
    st.write("Welcome to the Central Repository of all my Streamlit applications. Click on the links below to access each application.")

    ### Liste des applications avec leurs liens ###
    apps = {
        "Expenses Tracker": "https://expensestrackerr.streamlit.app/",
        "Professional Data Engineer Quizes": "https://quizappdelpgcp.streamlit.app/",
        "Analyse Immo-info": "https://analyse-immo-info.streamlit.app/",
        "Predicting the Creditworthiness of Bank Customers": "https://cyclientscreditworthinesspyapp-dq6q6sm24bakhp34memfrr.streamlit.app/",
        # Ajoutez plus d'applications ici
    }

    # Affichage des liens
    for app_name, app_link in apps.items():
        st.markdown(f"- [{app_name}]({app_link})")

    # Ajout d'une section de contact (facultatif)
    st.write("## Contact")
    st.write("If you have any questions or suggestions, please contact me at [smdlabtech@gmail.com](smdlabtech@gmail.com).")

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

    display_html("footer.html")
    with st.sidebar:
        display_html("footer.html")



#------------------------#
if __name__ == "__main__":
    main()
