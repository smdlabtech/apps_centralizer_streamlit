# File .DS_Store ()

# File .gitignore ()

# File app.py (.py)
 - **display_html** : No docstring found.
 - **display_js** : No docstring found.
 - **apply_js** : No docstring found.
 - **go_to_previous_page** : No docstring found.
 - **go_to_next_page** : No docstring found.
 - **main** : No docstring found.

# File app_data_loader.py (.py)
 - **load_csv_files_from_directory** : No docstring found.
 - **load_brsma** : No docstring found.
 - **load_lcl** : No docstring found.
 - **load_data_lcl** : No docstring found.
 - **process_data_lcl** : No docstring found.
 - **load_data_brsma** : No docstring found.
 - **process_data_brsma** : Traite les données BRSMA en s'assurant qu'elles soient sous forme de DataFrame,
filtre les lignes où la colonne 'dateOp' ne contient pas la valeur 'dateOp',
puis effectue des conversions de type sur les colonnes pertinentes.

Args:
data_brsma (list, dict, str, etc.): Les données BRSMA à traiter.

Returns:
pd.DataFrame: Le DataFrame traité avec les colonnes de type approprié.
 - **define_transfer_type** : No docstring found.

# File app_styles.py (.py)
 - **styles_img** : Loads and displays an image in a Streamlit application.

Args:
image_file (str): Name of the image file to load.
caption (str): Optional caption to be displayed below the image.
use_column_width (bool): Whether or not to use column width for the image.
width (int): Image width in pixels.
height (int): Image height in pixels.
output_format (str): Image output format (e.g. 'PNG', 'JPEG').
 - **styles_css** : Loads and applies a CSS file to a Streamlit application.

Args:
css_file (str): Name of CSS file to load.
 - **load_img** : Charge et affiche une image dans une application Streamlit.

Args:
image_file (str): Nom du fichier image à charger.
caption (str): Légende facultative à afficher sous l'image.
use_column_width (bool): Utiliser ou non la largeur de colonne pour l'image.
width (int): Largeur de l'image en pixels.
height (int): Hauteur de l'image en pixels.
output_format (str): Format de sortie de l'image (par exemple, 'PNG', 'JPEG').
 - **load_css** : Charge et applique un fichier CSS à une application Streamlit.

Args:
css_file (str): Nom du fichier CSS à charger.
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

# File details_kpis.py (.py)
 - **calculate_kpis** : No docstring found.

# File dev_generate_docs.py (.py)
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

# File LICENSE ()

# File app - Copie.py (.py)
 - **display_html** : No docstring found.
 - **display_js** : No docstring found.
 - **apply_js** : No docstring found.
 - **go_to_previous_page** : No docstring found.
 - **go_to_next_page** : No docstring found.
 - **main** : No docstring found.

# File app_data_loader_20240616.py (.py)
 - **load_csv_files_from_directory** : No docstring found.
 - **load_brsma** : No docstring found.
 - **load_lcl** : No docstring found.
 - **load_data_lcl** : No docstring found.
 - **process_data_lcl** : No docstring found.
 - **load_data_brsma** : No docstring found.
 - **process_data_brsma** : Traite les données BRSMA en s'assurant qu'elles soient sous forme de DataFrame,
filtre les lignes où la colonne 'dateOp' ne contient pas la valeur 'dateOp',
puis effectue des conversions de type sur les colonnes pertinentes.

Args:
data_brsma (list, dict, str, etc.): Les données BRSMA à traiter.

Returns:
pd.DataFrame: Le DataFrame traité avec les colonnes de type approprié.
 - **define_transfer_type** : No docstring found.

# File app_data_loader_new.py (.py)
 - **format_currency** : No docstring found.
 - **load_csv_files_from_directory** : No docstring found.
 - **load_brsma** : No docstring found.
 - **load_lcl** : No docstring found.
 - **load_data_lcl** : No docstring found.
 - **process_data_lcl** : No docstring found.
 - **load_data_brsma** : No docstring found.
 - **process_data_brsma** : No docstring found.
 - **define_transfer_type** : No docstring found.

# File app_data_loader_save_old.py (.py)
 - **load_csv_files_from_directory** : No docstring found.
 - **load_brsma** : No docstring found.
 - **load_lcl** : No docstring found.
 - **load_data_lcl** : No docstring found.
 - **process_data_lcl** : No docstring found.
 - **load_data_brsma** : No docstring found.
 - **process_data_brsma** : Traite les données BRSMA en s'assurant qu'elles soient sous forme de DataFrame,
filtre les lignes où la colonne 'dateOp' ne contient pas la valeur 'dateOp',
puis effectue des conversions de type sur les colonnes pertinentes.

Args:
data_brsma (list, dict, str, etc.): Les données BRSMA à traiter.

Returns:
pd.DataFrame: Le DataFrame traité avec les colonnes de type approprié.
 - **define_transfer_type** : No docstring found.

# File details copy 2.py (.py)
 - **calculate_kpis** : No docstring found.
 - **display_kpis** : No docstring found.
 - **plot_total_expenses** : No docstring found.
 - **plot_expenses_by_categorie** : No docstring found.
 - **plot_avg_transaction_montant** : No docstring found.
 - **plot_top_suppliers** : No docstring found.
 - **plot_expenses_by_transaction_type** : No docstring found.
 - **plot_expenses_over_time** : No docstring found.
 - **plot_expenses_by_day** : No docstring found.
 - **brsma_metrique_org** : No docstring found.
 - **page_details** : No docstring found.

# File details copy.py (.py)
 - **plot_total_expenses** : No docstring found.
 - **plot_expenses_by_categorie** : No docstring found.
 - **plot_avg_transaction_montant** : No docstring found.
 - **plot_top_suppliers** : No docstring found.
 - **plot_expenses_by_transaction_type** : No docstring found.
 - **plot_expenses_over_time** : No docstring found.
 - **plot_expenses_by_day** : No docstring found.
 - **brsma_metrique_org** : No docstring found.
 - **page_details** : No docstring found.

# File raw_data copy.py (.py)
 - **calculate_kpis** : No docstring found.
 - **display_kpis** : No docstring found.
 - **page_raw_data** : No docstring found.

# File raw_data_save.py (.py)
 - **page_raw_data** : No docstring found.

# File aboutme.py (.py)
 - **create_clickable_image** : Crée un HTML pour une image cliquable qui redirige vers un lien donné.

:param image_path: Chemin vers l'image.
:param link: URL vers laquelle l'image redirige.
:param alt_text: Texte alternatif pour l'image.
:param style: Style CSS pour l'image.
 - **create_icon_link** : Crée un HTML pour une icône cliquable qui redirige vers un lien donné.

:param icon_class: Classe de l'icône (par exemple, "fab fa-linkedin").
:param link: URL vers laquelle l'icône redirige.
:param color: Couleur de l'icône.
:param size: Taille de l'icône (par exemple, "2x").
 - **page_aboutme** : No docstring found.

# File details.py (.py)
 - **LCLDetails** : No docstring found.
 - **BRSMAExpenses** : No docstring found.
 - **page_details** : No docstring found.
 - **__init__** : No docstring found.
 - **display_summary** : No docstring found.
 - **display_transaction_type_pie_chart** : No docstring found.
 - **display_transactions_over_time** : No docstring found.
 - **display_transactions_by_day** : No docstring found.
 - **display_creditor_debtor** : No docstring found.
 - **display_financial_kpis** : No docstring found.
 - **display_expenses_by_category** : No docstring found.
 - **display_average_transaction_amount** : No docstring found.
 - **display_top_suppliers** : No docstring found.
 - **display_expenses_by_transaction_type** : No docstring found.
 - **display_expenses_over_time** : No docstring found.
 - **display_expenses_by_day** : No docstring found.
 - **display_organism_metrics** : No docstring found.
 - **brsma_metrique_org** : No docstring found.

# File homepage.py (.py)
 - **page_home** : No docstring found.

# File overview.py (.py)

# File raw_data.py (.py)
 - **format_currency** : No docstring found.
 - **LCLDetails** : No docstring found.
 - **BRSMAExpenses** : No docstring found.
 - **page_raw_data** : No docstring found.
 - **__init__** : No docstring found.
 - **display_summary** : No docstring found.

