# Dev App Documentation

## File 1: app_styles.py (.py)
 - **create_clickable_image** : No docstring found.
 - **create_icon_link** : cree un HTML pour une icône cliquable qui redirige vers un lien donné.

:param icon_class: Classe de l'icône (par exemple, "fab fa-linkedin").
:param link: URL vers laquelle l'icône redirige.
:param color: Couleur de l'icône.
:param size: Taille de l'icône (par exemple, "2x").
 - **styles_img** : Loads and displays an image in a Streamlit application.

Args:
image_file (str): Name of the image file to load.
caption (str): Optional caption to be displayed below the image.
use_column_width (bool): Whether or not to use column width for the image.
width (int): Image width in pixels.
height (int): Image height in pixels.
output_format (str): Image output format (e.g. 'PNG', 'JPEG').
 - **load_img** : Charge et affiche une image dans une application Streamlit.

Args:
image_file (str): Nom du fichier image à charger.
caption (str): Légende facultative à afficher sous l'image.
use_column_width (bool): Utiliser ou non la largeur de colonne pour l'image.
width (int): Largeur de l'image en pixels.
height (int): Hauteur de l'image en pixels.
output_format (str): Format de sortie de l'image (par exemple, 'PNG', 'JPEG').
 - **load_img_as_base64** : Charge une image et la convertit en base64.

Args:
image_file (str): Nom du fichier image à charger.

Returns:
str: L'image encodée en base64.
 - **load_img_clickable** : Charge et affiche une image dans une application Streamlit avec une option de lien hypertexte.

Args:
image_file (str): Nom du fichier image à charger.
link (str): URL vers laquelle l'image redirige.
alt_text (str): Texte alternatif pour l'image.
width (int): Largeur de l'image en pixels.
height (int): Hauteur de l'image en pixels.
style (str): Style CSS pour l'image.
 - **load_logo** : Charge et affiche un logo avec une option de lien hypertexte dans une application Streamlit.

Args:
image_file (str): Nom du fichier image à charger.
link (str): URL à ouvrir lors du clic sur l'image.
width (int): Largeur de l'image en pixels.
height (int): Hauteur de l'image en pixels.
 - **apply_css** : No docstring found.
 - **styles_css** : Loads and applies a CSS file to a Streamlit application.

Args:
css_file (str): Name of CSS file to load.
 - **load_css** : Charge et applique un fichier CSS à une application Streamlit.

Args:
css_file (str): Nom du fichier CSS à charger.
 - **display_html** : No docstring found.
 - **load_html** : Charge le contenu HTML à partir du nom de fichier donné.

Args:
file_name (str): Nom du fichier HTML à charger.

Returns:
str: Le contenu HTML en tant que chaîne de caractères.
 - **load_js** : Charge le contenu JavaScript à partir du nom de fichier donné.

Args:
file_name (str): Nom du fichier JavaScript à charger.

Returns:
str: Le contenu JavaScript en tant que chaîne de caractères.

## File 2: centralizer.py (.py)
 - **display_html** : No docstring found.
 - **display_js** : No docstring found.
 - **apply_js** : No docstring found.
 - **create_icon_link** : Crée un HTML pour une icône cliquable qui redirige vers un lien donné.

:param icon_class: Classe de l'icône (par exemple, "fab fa-linkedin").
:param link: URL vers laquelle l'icône redirige.
:param color: Couleur de l'icône.
:param size: Taille de l'icône (par exemple, "2x").
 - **setup_carousel** : No docstring found.
 - **main** : No docstring found.

## File 3: dev_generate_docs.py (.py)
 - **extract_info_from_file** : Extracts relevant information (docstrings, functions, classes) from a Python file,
and content for CSS and JavaScript files, while ignoring specified file types.

Args:
    file_path (str): The full path to the file.
    
Returns:
    dict: A dictionary containing the extracted information.
 - **generate_documentation_md** : Generates a Markdown file containing documentation for all files in a directory,
ignoring specified directories and file types.

Args:
    directory_path (str): The path of the directory containing the files.
    output_file (str): The path of the output Markdown file.

## File 4: test.py (.py)
 - **display_html** : No docstring found.
 - **display_js** : No docstring found.
 - **apply_js** : No docstring found.
 - **create_icon_link** : Crée un HTML pour une icône cliquable qui redirige vers un lien donné.

:param icon_class: Classe de l'icône (par exemple, "fab fa-linkedin").
:param link: URL vers laquelle l'icône redirige.
:param color: Couleur de l'icône.
:param size: Taille de l'icône (par exemple, "2x").
 - **setup_carousel** : No docstring found.
 - **main** : No docstring found.

## File 5: aboutme.py (.py)
 - **page_aboutme** : No docstring found.

## File 6: details.py (.py)
 - **group_similar_words** : No docstring found.
 - **LCLDetails** : No docstring found.
 - **BRSMAExpenses** : No docstring found.
 - **page_details** : No docstring found.
 - **__init__** : No docstring found.
 - **format_currency** : Formate les nombres en euros.
 - **display_summary** : No docstring found.
 - **display_transaction_type_pie_chart** : No docstring found.
 - **display_transactions_over_time** : No docstring found.
 - **display_transactions_by_day** : No docstring found.
 - **display_creditor_debtor** : No docstring found.
 - **lcl_metrique_org** : No docstring found.
 - **display_lcl_operation_text_metrics** : No docstring found.
 - **display_financial_kpis** : No docstring found.
 - **display_expenses_by_category** : No docstring found.
 - **display_average_transaction_transaction** : No docstring found.
 - **display_top_suppliers** : No docstring found.
 - **display_expenses_by_transaction_type** : No docstring found.
 - **display_expenses_over_time** : No docstring found.
 - **display_expenses_by_day** : No docstring found.
 - **display_organism_metrics** : No docstring found.
 - **brsma_metrique_org** : No docstring found.

## File 7: homepage.py (.py)
 - **page_home** : No docstring found.

## File 8: overview.py (.py)

## File 9: plan_eco_tax_and_invest.py (.py)
 - **PlanEcoTaxAndInvest** : No docstring found.
 - **page_plan_eco_tax_and_invest** : No docstring found.
 - **__init__** : No docstring found.
 - **calculate_expenses** : No docstring found.
 - **calculate_investments** : No docstring found.
 - **calculate_tax_optimization** : No docstring found.
 - **calculate_long_term_planning** : No docstring found.
 - **show_budget** : No docstring found.
 - **show_investments** : No docstring found.
 - **show_tax_optimization** : No docstring found.
 - **show_long_term_planning** : No docstring found.

## File 10: raw_data.py (.py)
 - **format_currency** : No docstring found.
 - **format_euro** : Format a number as Euro currency with thousand separators.
 - **LCLDetails** : No docstring found.
 - **BRSMAExpenses** : No docstring found.
 - **page_raw_data** : No docstring found.
 - **__init__** : No docstring found.
 - **display_summary** : No docstring found.

