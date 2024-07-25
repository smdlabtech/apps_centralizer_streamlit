import streamlit as st
from app_data_loader import load_data_brsma, load_data_lcl, process_data_lcl, process_data_brsma
import app_styles
from _pages import homepage, details, raw_data, aboutme, plan_eco_tax_and_invest

# Initialiser l'état de session pour la configuration de la page
if 'page_layout' not in st.session_state:
    st.session_state.page_layout = 'wide'  # Layout par défaut

# Configuration initiale de la page
st.set_page_config(
    page_title="Expenses Tracker",
    page_icon="💵",
    layout=st.session_state.page_layout,
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.example.com/help',
        'Report a bug': 'https://www.example.com/bug',
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


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

def go_to_previous_page():
    pages = ["🏠HomePage","💰PlanEcoTaxInvest", "📊Details", "🗄️Raw Data","😎AboutMe"]
    current_index = pages.index(st.session_state.page)
    if current_index > 0:
        st.session_state.page = pages[current_index - 1]

def go_to_next_page():
    pages = ["🏠HomePage","💰PlanEcoTaxInvest", "📊Details", "🗄️Raw Data","😎AboutMe"]
    current_index = pages.index(st.session_state.page)
    if current_index < len(pages) - 1:
        st.session_state.page = pages[current_index + 1]

def main():
    st.markdown("<h1 style='text-align: center;'>💵Expenses Tracker</h1>", unsafe_allow_html=True)

    with st.sidebar:
        app_styles.load_img("senlab_ia_gen_rmv_bgrd.png", caption="🇸🇳 SenLab IA 🇫🇷", width=5, use_column_width=True, output_format='PNG')
        st.sidebar.markdown("<h1 style='text-align: left; color: grey;'>Sidebar Panel : </h1>", unsafe_allow_html=True)

        if "page" not in st.session_state:
            st.session_state.page = "🏠HomePage"
            st.session_state.page_layout = "wide"

        # Ajout du bouton radio pour choisir la largeur de la page
        page_size_option = st.sidebar.radio("Page size", ["Wide", "Normal"])
        
        # Vérifiez si la configuration de la page doit être mise à jour
        if page_size_option == "Normal" and st.session_state.page_layout != "centered":
            st.session_state.page_layout = "centered"
            st.rerun()
            
        elif page_size_option == "Wide" and st.session_state.page_layout != "wide":
            st.session_state.page_layout = "wide"
            st.rerun()

        st.sidebar.button("🏠HomePage", on_click=lambda: st.session_state.update(page="🏠HomePage"))
        st.sidebar.button("💰PlanEcoTaxInvest", on_click=lambda: st.session_state.update(page="💰PlanEcoTaxInvest"))
        st.sidebar.button("📊Details", on_click=lambda: st.session_state.update(page="📊Details"))
        st.sidebar.button("🗄️Raw Data", on_click=lambda: st.session_state.update(page="🗄️Raw Data"))
        st.sidebar.button("😎AboutMe", on_click=lambda: st.session_state.update(page="😎AboutMe"))

    # col1, col2, _ = st.columns([1, 10, 1])
    col1, col2, _ = st.columns([1, 8, 1])
    with col1:
        if st.button("Prev."):
            go_to_previous_page()
    with col2:
        empty_space = st.empty()
    with _:
        if st.button("Next"):
            go_to_next_page()

    
    ## Calling other modules (pages) ##
    if st.session_state.page == "🏠HomePage":
        homepage.page_home()
        
    elif st.session_state.page == "💰PlanEcoTaxInvest":
        plan_eco_tax_and_invest.page_plan_eco_tax_and_invest()
    
    elif st.session_state.page == "📊Details":
        details.page_details()
    
    elif st.session_state.page == "🗄️Raw Data":
        raw_data.page_raw_data()
    
    elif st.session_state.page == "😎AboutMe":
        aboutme.page_aboutme()

    display_html("footer.html")
    with st.sidebar:
        display_html("footer.html")
        


#------------------------#
if __name__ == "__main__":
    main()
