import os
import streamlit as st
from PIL import Image
import io
import base64




## IMAGE + LOGO #################
def create_clickable_image(image_file, link, alt_text, style="width:100%;"):
    
    image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"assets", "img", image_file)
    """
    cree un HTML pour une image cliquable qui redirige vers un lien donné.

    :param image_path: Chemin vers l'image.
    :param link: URL vers laquelle l'image redirige.
    :param alt_text: Texte alternatif pour l'image.
    :param style: Style CSS pour l'image.
    """
    html_code = f"""
    <a href="{link}" target="_blank">
        <img src="{image_path}" alt="{alt_text}" style="{style}">
    </a>
    """
    st.markdown(html_code, unsafe_allow_html=True)

def create_icon_link(icon_class, link, color, size="2x"):
    """
    cree un HTML pour une icône cliquable qui redirige vers un lien donné.

    :param icon_class: Classe de l'icône (par exemple, "fab fa-linkedin").
    :param link: URL vers laquelle l'icône redirige.
    :param color: Couleur de l'icône.
    :param size: Taille de l'icône (par exemple, "2x").
    """
    html_code = f"""
    <a href="{link}" target="_blank">
        <i class="{icon_class} fa-{size}" style="color:{color};"></i>
    </a>
    """
    return html_code



def styles_img(image_file, caption=None, use_column_width=True, width=None, height=None, output_format=None):
    """
    Loads and displays an image in a Streamlit application.
    
    Args:
    image_file (str): Name of the image file to load.
    caption (str): Optional caption to be displayed below the image.
    use_column_width (bool): Whether or not to use column width for the image.
    width (int): Image width in pixels.
    height (int): Image height in pixels.
    output_format (str): Image output format (e.g. 'PNG', 'JPEG').
    """
    # Construire le chemin complet vers le fichier image en utilisant le nom du fichier passé en argument
    image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"assets", "img", image_file)
    return st.image(image_path, caption=caption, use_column_width=use_column_width, width=width, output_format=output_format)



#-------------
def load_img(image_file, caption=None, use_column_width=True, width=None, height=None, output_format=None):
    """
    Charge et affiche une image dans une application Streamlit.
    
    Args:
    image_file (str): Nom du fichier image à charger.
    caption (str): Légende facultative à afficher sous l'image.
    use_column_width (bool): Utiliser ou non la largeur de colonne pour l'image.
    width (int): Largeur de l'image en pixels.
    height (int): Hauteur de l'image en pixels.
    output_format (str): Format de sortie de l'image (par exemple, 'PNG', 'JPEG').
    """
    # Construire le chemin complet vers le fichier image en utilisant le nom du fichier passé en argument
    image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"assets", "img", image_file)
    if os.path.exists(image_path):
        return st.image(image_path, caption=caption, use_column_width=use_column_width, width=width, output_format=output_format)
    else:
        st.error(f"Image {image_file} not found.")

def load_img_as_base64(image_file):
    """
    Charge une image et la convertit en base64.
    
    Args:
    image_file (str): Nom du fichier image à charger.
    
    Returns:
    str: L'image encodée en base64.
    """
    image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "img", image_file)
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.error(f"File {image_file} not found.")
        return None

#--------------------------


def load_img_clickable(image_file, link, alt_text, width=None, height=None, style="width:100%;"):
    """
    Charge et affiche une image dans une application Streamlit avec une option de lien hypertexte.
    
    Args:
    image_file (str): Nom du fichier image à charger.
    link (str): URL vers laquelle l'image redirige.
    alt_text (str): Texte alternatif pour l'image.
    width (int): Largeur de l'image en pixels.
    height (int): Hauteur de l'image en pixels.
    style (str): Style CSS pour l'image.
    """
    # Construire le chemin complet vers le fichier image en utilisant le nom du fichier passé en argument
    image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "img", image_file)
    
    # Créer un lien hypertexte autour de l'image
    html_code = f"""
    <a href="{link}" target="_blank">
        <img src="{image_path}" alt="{alt_text}" style="{style}" width="{width}" height="{height}">
    </a>
    """
    st.markdown(html_code, unsafe_allow_html=True)



def load_logo(image_file, link=None, width=None, height=None):
    """
    Charge et affiche un logo avec une option de lien hypertexte dans une application Streamlit.
    
    Args:
    image_file (str): Nom du fichier image à charger.
    link (str): URL à ouvrir lors du clic sur l'image.
    width (int): Largeur de l'image en pixels.
    height (int): Hauteur de l'image en pixels.
    """
    # Construire le chemin complet vers le fichier image en utilisant le nom du fichier passé en argument
    image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "img", image_file)
    
    if link:
        # Créer un lien hypertexte autour de l'image
        image_html = f'<a href="{link}" target="_blank"><img src="{image_path}" width="{width}" height="{height}"></a>'
        st.markdown(image_html, unsafe_allow_html=True)
    else:
        # Afficher simplement l'image
        st.image(image_path, width=width, height=height)


## CSS #################
# Apply CSS styles
def apply_css(file_name):
    try:
        css_content = styles_css(file_name)
        st.markdown(f'<style>{css_content}</style>', unsafe_allow_html=True)
    except FileNotFoundError as e:
        st.error(f"Error: {e}")
        

def styles_css(css_file):
    """
    Loads and applies a CSS file to a Streamlit application.
    
    Args:
    css_file (str): Name of CSS file to load.
    """
    # Construire le chemin complet vers le fichier CSS en utilisant le nom du fichier passé en argument
    css_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "css", css_file)
    if not os.path.exists(css_path):
        raise FileNotFoundError(f"File '{css_file}' not found at '{css_path}'")
    
    with open(css_path) as f:
        css = f.read()
    
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)



def load_css(css_file):
    """
    Charge et applique un fichier CSS à une application Streamlit.
    
    Args:
    css_file (str): Nom du fichier CSS à charger.
    """
    # Construire le chemin complet vers le fichier CSS en utilisant le nom du fichier passé en argument
    css_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "css", css_file)
    if not os.path.exists(css_path):
        raise FileNotFoundError(f"File '{css_file}' not found at '{css_path}'")
    
    with open(css_path) as f:
        css = f.read()
    
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)




## HTML #################
# Display HTML content
def display_html(file_name):
    try:
        html_content = load_html(file_name)
        st.markdown(html_content, unsafe_allow_html=True)
    except FileNotFoundError as e:
        st.error(f"Error: {e}")



def load_html(file_name):
    """
    Charge le contenu HTML à partir du nom de fichier donné.
    
    Args:
    file_name (str): Nom du fichier HTML à charger.

    Returns:
    str: Le contenu HTML en tant que chaîne de caractères.
    """
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "html", file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_name}' not found at '{file_path}'")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


## JS #################
def load_js(file_name):
    """
    Charge le contenu JavaScript à partir du nom de fichier donné.
    
    Args:
    file_name (str): Nom du fichier JavaScript à charger.

    Returns:
    str: Le contenu JavaScript en tant que chaîne de caractères.
    """
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "js", file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_name}' not found at '{file_path}'")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    return content
