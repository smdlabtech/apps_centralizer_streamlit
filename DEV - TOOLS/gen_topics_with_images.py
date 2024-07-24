import os

# Définir le répertoire de base
base_directory = os.path.dirname(os.path.abspath(__file__))

# Chemin des images
img_path = "_topics/Theme 06 - GCP Study Hub - gcpstudyhub/Review Courses/02 - Identity and Access Management/assets/img"

# Générer la liste des fichiers image
image_files = [f"IAM {i:02}.png" for i in range(1, 19)]

# Générer le code HTML pour afficher les images
html_code = ""
for image in image_files:
    full_path = os.path.join(img_path, image)
    relative_path = os.path.relpath(full_path, base_directory)
    html_code += f'''
<p align="center"> 
    <img width = "700" src="{relative_path}" align="center"></img>
</p>
<br>
'''

# Écrire le code HTML dans un fichier .md
with open("images.md", "w", encoding="utf-8") as file:
    file.write(html_code)

print("Le fichier images.md a été généré avec succès.")
