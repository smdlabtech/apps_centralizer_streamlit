import pandas as pd
import os
from glob import glob
import streamlit as st
import Levenshtein

### Chargement des fichiers .CSV ###
def load_csv_files_from_directory(directory, delimiter="\t", encoding="cp1252"):
    all_files = glob(os.path.join(directory, "*.csv"))
    data = pd.concat(
        (pd.read_csv(f, delimiter=delimiter, encoding=encoding, header=None) for f in all_files),
        ignore_index=True
    )
    return data

### LOAD DATA LCL
@st.cache_data 
def load_lcl():
    data_lcl = load_data_lcl()
    data_lcl_processed = process_data_lcl(data_lcl)   
    return data_lcl_processed

### LOAD DATA BRSMA
@st.cache_data 
def load_brsma():
    data_brsma = load_data_brsma()
    data_brsma_processed = process_data_brsma(data_brsma)
    return data_brsma_processed

#--------------------------------#
# 1. Chargement des données (LCL)
#--------------------------------#
def load_data_lcl():
    lcl_directory = "_data/data_lcl"
    data_lcl = load_csv_files_from_directory(lcl_directory, delimiter=";", encoding="utf-8")
    data_lcl.columns = ["dateOp", "montant", "typeOp", "compteU", "operation", "type action", "etat", "autres"]
    expected_columns = ["dateOp", "montant", "typeOp", "compteU", "operation", "type action", "etat", "autres"]
    
    if data_lcl.shape[1] != len(expected_columns):
        raise ValueError(f"Expected {len(expected_columns)} columns, but got {data_lcl.shape[1]}")
    data_lcl.columns = expected_columns
    return data_lcl

# Fonction pour regrouper les mots similaires
def group_similar_words(mots, seuil_similarite=80):
    groupes = []
    mots_restants = mots.copy()
    
    while mots_restants:
        mot = mots_restants.pop(0)
        groupe = [mot]
        
        similar_words = [(other_mot, Levenshtein.ratio(mot, other_mot) * 100) for other_mot in mots_restants]
        
        for similar_word, score in similar_words:
            if score >= seuil_similarite:
                groupe.append(similar_word)
                mots_restants.remove(similar_word)
                
        groupes.append(groupe)
    
    # Choisir un représentant pour chaque groupe (par exemple, le premier mot)
    representatives = {mot: groupe[0] for groupe in groupes for mot in groupe}
    return representatives

# Remplacer les virgules par des points pour la conversion en float
def process_data_lcl(data_lcl):
    
    ## Transformation de 'type action' en minuscules
    data_lcl['type action'] = data_lcl['type action'].str.lower()
    data_lcl['operation'] = data_lcl['operation'].str.lower()
    data_lcl['dateOp'] = pd.to_datetime(data_lcl['dateOp'], format='%d/%m/%Y', errors='coerce')
        
    data_lcl['montant'] = data_lcl['montant'].str.replace(',', '.').astype(float)
    data_lcl['creancier'] = data_lcl['montant'].apply(lambda x: 'crediteur' if x > 0 else 'debiteur')
    data_lcl['creancier_crediteur'] = data_lcl['montant'].where(data_lcl['montant'] > 0).fillna(0)
    data_lcl['creancier_debiteur'] = data_lcl['montant'].where(data_lcl['montant'] < 0).fillna(0)
    
    data_lcl['anneeOp'] = data_lcl['dateOp'].dt.year
    
    data_lcl['mois_op_nom'] = data_lcl['dateOp'].dt.strftime('%b')
    data_lcl['mois_op'] = data_lcl['dateOp'].dt.strftime('%m').astype(str).str.zfill(2)
    data_lcl['jours_Op'] = data_lcl['dateOp'].dt.day



    data_lcl['operation_copie'] = data_lcl['operation'].astype(str)
    ## Clean operation (for operation)
    def clean_operation(op):
        cleaned_op = []
        found_digit = False
        
        for char in op:
            if char.isdigit():
                found_digit = True
                break
            cleaned_op.append(char)
        
        cleaned_op = ''.join(cleaned_op)
        return cleaned_op
    data_lcl['operation_texte'] = data_lcl['operation_copie'].apply(clean_operation)
    
    
    mots_uniques = data_lcl['operation_texte'].unique().tolist()
    representants = group_similar_words(mots_uniques)
    data_lcl['operation_texte'] = data_lcl['operation_texte'].map(representants)
        
    ## Traitement des "NA" ou valeurs manquantes dans les différentes colonnes
    data_lcl = data_lcl.fillna(value={'montant' : 0.00, 'typeOp': '', 'operation': '', 'compteU': '','type action': '', 'etat': 0.00, 'autres': '','operation_copie' : '', 'operation_texte':''})
    data_lcl = data_lcl.drop(columns=['etat'])   # Virer la colonne "etat"

    df = pd.DataFrame(data_lcl)
    filtered_df = df.loc[df['dateOp'].notnull()].copy()
    df = filtered_df.copy()
    df.reset_index(inplace=True, drop=True)
    
    actions = {
        "virement axys consultants": "Revenu Axys",
        "virement auchan hypermarche": "Revenu Auchan",
        "virement m mamadou daya sylla": "Epargne et Cpt Courant",
        "vir sepa mamadou sylla b": "Epargne et Cpt Courant",
        "vir sepa m mamadou daya sylla": "Epargne et Cpt Courant",
        "vir inst mamadou sylla b": "Epargne et Cpt Courant"
    }
    
    df['type action'] = df['type action'].fillna('')
    
    def define_transfer_and_operation(row):
        type_transfert_operation = "Autres"
        
        if row['type action'] in actions:
            type_transfert_operation = actions[row['type action']]
        elif row['type action'] == '' and row['operation'] in ['vir sepa mamadou sylla b', 'vir sepa m mamadou daya sylla']:
            type_transfert_operation = "Epargne et Cpt Courant"
        
        return type_transfert_operation
    
    df['type_transfert_operation'] = df.apply(define_transfer_and_operation, axis=1)
    df = df[df['dateOp'].notnull()].reset_index(drop=True)
    return df

#-----------------------------------#
# 2. Chargement des données (BRSMA)
#-----------------------------------#
def load_data_brsma():
    brsma_directory = "_data/data_brsma"
    data_brsma = load_csv_files_from_directory(brsma_directory, delimiter=";", encoding="utf-8")
    data_brsma.columns = ["dateOp", "dateVal", "label", "category", "categoryParent", "supplierFound", "amount", "accountNum", "accountLabel", "accountBalance", "comment", "pointer"]
    data_brsma.columns = data_brsma.iloc[0]
    data_brsma = data_brsma[1:]
    data_brsma.reset_index(drop=True, inplace=True)
    return data_brsma

# Remplacer les virgules par des points pour la conversion en float
def process_data_brsma(data_brsma):
    df = pd.DataFrame(data_brsma)
    df.columns = ["dateOp", "dateVal", "label", "category", "categoryParent", "supplierFound", "amount", "accountNum", "accountLabel", "accountBalance", "comment", "pointer"]
    filtered_df = df.loc[df['dateOp'] != 'dateOp'].copy()
    filtered_df.reset_index(drop=True, inplace=True)
    
    df = filtered_df.rename(columns={
        "dateOp": "dateOp", 
        "dateVal": "dateVal",
        "label": "type_operation",
        "category": "categorie",
        "categoryParent": "categorie_parent",
        "supplierFound": "organisme",
        "amount": "montant",
        "accountNum": "numero_compte",
        "accountLabel": "etiquette_compte",
        "accountBalance": "solde_actuel_compte",
        "comment": "commentaire",
        "pointer": "pointeur"
    })
    
    df['dateOp'] = pd.to_datetime(df['dateOp'], errors='coerce').dt.strftime('%Y-%m-%d')
    df['dateVal'] = pd.to_datetime(df['dateVal'], errors='coerce').dt.strftime('%Y-%m-%d')
    
    df['type_operation'] = df['type_operation'].astype('object')
    df['categorie'] = df['categorie'].astype('object')
    df['categorie_parent'] = df['categorie_parent'].astype('object')
    df['organisme'] = df['organisme'].astype('object')
    df['montant'] = pd.to_numeric(df['montant'].str.replace(',', '.'), errors='coerce').fillna(0)
    df['numero_compte'] = df['numero_compte'].astype('object')
    df['etiquette_compte'] = df['etiquette_compte'].astype('object')
    df['solde_actuel_compte'] = pd.to_numeric(df['solde_actuel_compte'].str.replace(',', '.'), errors='coerce').fillna(0)
    df['commentaire'] = df['commentaire'].astype(str)
    df['pointeur'] = df['pointeur'].astype(str)
    
    ## Transformation de 'type operation' en minuscules
    df['type_operation'] = df['type_operation'].str.lower()
    df['categorie'] = df['categorie'].str.lower()
    df['categorie_parent'] = df['categorie_parent'].str.lower()
    df['organisme'] = df['organisme'].str.lower()
    df['etiquette_compte'] = df['etiquette_compte'].str.lower()
    
    ## Traitement des valeurs manquantes "NA"
    df = df.fillna(value={'commentaire': 'blank', 'pointeur': ''})
    return df
