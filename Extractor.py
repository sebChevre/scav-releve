#!/usr/bin/env python
# coding: utf-8

import argparse
import math
import numpy as np
import pandas as pd
import string
import unicodedata

################################# Internal Data ########################################
#Hard coded Commune Locality Distributeur Information
CommuneLocalityDistributeur = pd.DataFrame(
       np.array([['Boécourt', 'Boécourt', 'Conseil communal de Boécourt'],
       ['Boécourt', 'Séprais', 'Conseil communal de Boécourt'],
       ['Boécourt', 'Montavon', 'Conseil communal de Boécourt'],
       ['Bourrignon', 'Bourrignon', 'Conseil communal de Bourrignon'],
       ['Châtillon', 'Châtillon', 'Conseil communal de Châtillon'],
       ['Courrendlin', 'Courrendlin', 'Conseil communal de Courrendlin'],
       ['Courrendlin', 'Vellerat', 'Conseil communal de Courrendlin'],
       ['Courrendlin', 'Rebeuvelier', 'Conseil communal de Courrendlin'],
       ['Courroux', 'Courroux', 'Conseil communal de Courroux'],
       ['Courroux', 'Courcelon', 'Conseil communal de Courroux'],
       ['Courtételle', 'Courtételle', 'Conseil communal de Courtételle'],
       ['Delémont', 'Delémont', 'Conseil communal de Delémont /SID'],
       ['Develier', 'Develier', 'Conseil communal de Develier'],
       ['Ederswiler', 'Ederswiler', 'GWER '],
       ['Haute-Sorne', 'Bassecourt', 'Conseil communal de Haute-Sorne'],
       ['Haute-Sorne', 'Courfaivre', 'Conseil communal de Haute-Sorne'],
       ['Haute-Sorne', 'Glovelier', 'Conseil communal de Haute-Sorne'],
       ['Haute-Sorne', 'Soulce', 'Conseil communal de Haute-Sorne'],
       ['Haute-Sorne', 'Undervelier', 'Conseil communal de Haute-Sorne'],
       ['Mettembert', 'Mettembert', 'Conseil communal de Mettembert'],
       ['Movelier', 'Movelier', 'Conseil communal de Movelier'],
       ['Pleigne', 'Pleigne', 'Conseil communal de Pleigne'],
       ['Rossemaison', 'Rossemaison', 'Conseil communal de Rossemaison'],
       ['Saulcy', 'Saulcy', 'Conseil communal de Saulcy'],
       ['Soyhières', 'Soyhières', 'Conseil communal de Soyhières'],
       ['Val Terbi', 'Vicques', 'SEVT'],
       ['Val Terbi', 'Vermes', 'Conseil communal de Val Terbi'],
       ['Mervelier', 'Mervelier', 'SEVT'],
       ['Montsevelier', 'Montsevelier', 'SEVT'],
       ['Courchapoix', 'Courchapoix', 'SEVT'],
       ['Corban', 'Corban', 'SEVT'],
       ['Alle', 'Alle', 'Conseil communal de Alle'],
       ['La Baroche', 'Charmoille', 'Conseil communal de La Baroche'],
       ['La Baroche', 'Fregiécourt', 'Conseil communal de La Baroche'],
       ['La Baroche', 'Miécourt', 'Conseil communal de La Baroche'],
       ['La Baroche', 'Pleujouse', 'Conseil communal de La Baroche'],
       ['La Baroche', 'Asuel', 'Conseil communal de La Baroche'],
       ['Basse-Allaine', 'Courtemaîche',
        'Conseil communal de Basse-Allaine'],
       ['Basse-Allaine', 'Buix', 'Conseil communal de Basse-Allaine'],
       ['Basse-Allaine', 'Montignez',
        'Conseil communal de Basse-Allaine'],
       ['Beurnevésin', 'Beurnevésin', 'SEV'],
       ['Boncourt', 'Boncourt', 'Conseil communal de Boncourt'],
       ['Bonfol', 'Bonfol', 'SEV'],
       ['Bure', 'Bure', 'Conseil communal de Bure'],
       ['Clos-du-Doubs', 'St-Ursanne',
        'Conseil communal de Clos-du-Doubs'],
       ['Clos-du-Doubs', 'Montenol', 'Conseil communal de Clos-du-Doubs'],
       ['Clos-du-Doubs', 'Epauvillers',
        'Conseil communal de Clos-du-Doubs'],
       ['Clos-du-Doubs', 'Montenol', 'Conseil communal de Clos-du-Doubs'],
       ['Clos-du-Doubs', 'Epiquerez',
        'Conseil communal de Clos-du-Doubs'],
       ['Clos-du-Doubs', 'Ocourt', 'Conseil communal de Clos-du-Doubs'],
       ['Clos-du-Doubs', 'Seleute', 'Conseil communal de Clos-du-Doubs'],
       ['Coeuve', 'Coeuve', 'SEV'],
       ['Cornol', 'Cornol', 'Conseil communal de Cornol'],
       ['Courchavon', 'Courchavon', 'Conseil communal de Courchavon'],
       ['Courgenay', 'Courgenay', 'Conseil communal de Courgenay'],
       ['Courtedoux', 'Courtedoux', 'Conseil communal de Courtedoux'],
       ['Damphreux', 'Damphreux', 'SEV'],
       ['Fahy', 'Fahy', 'Conseil communal de Fahy'],
       ['Fontenais', 'Fontenais', 'Conseil communal de Fontenais'],
       ['Fontenais', 'Bressaucourt', 'Conseil communal de Fontenais'],
       ['Grandfontaine', 'Grandfontaine',
        'Conseil communal de Grandfontaine'],
       ['Haute-Ajoie', 'Chevenez', 'Conseil communal de Haute-Ajoie'],
       ['Haute-Ajoie', 'Rocourt', 'Conseil communal de Haute-Ajoie'],
       ['Haute-Ajoie', 'Damvant', 'Conseil communal de Haute-Ajoie'],
       ['Haute-Ajoie', "Roche d'Or", 'Conseil communal de Haute-Ajoie'],
       ['Lugnez', 'Lugnez', 'SEV'],
       ['Porrentruy', 'Porrentruy', 'Conseil communal de Porrentruy'],
       ['Vendlincourt', 'Vendlincourt', 'SEV'],
       ['Le Bémont', 'Le Bémont', 'Conseil communal du Bémont '],
       ['Les Bois', 'Les Bois', 'Conseil communal des Bois '],
       ['Les Breuleux', 'Les Breuleux', 'Conseil communal des Breuleux '],
       ['La Chaux-des-Breuleux', 'La Chaux-des-Breuleux',
        'Conseil communal de la Chaux-des-Breuleux'],
       ['Les Enfers', 'Les Enfers', 'Conseil communal des Enfers'],
       ['Les Genevez', 'Les Genevez', 'Conseil communal des Genevez'],
       ['Lajoux', 'Lajoux', 'Conseil communal de Lajoux'],
       ['Montfaucon', 'Montfaucon', 'Conseil communal de Montfaucon'],
       ['Muriaux', 'Muriaux', 'Conseil communal de Muriaux'],
       ['Muriaux', 'Les Emibois', 'Conseil communal de Muriaux'],
       ['Le Noirmont', 'Le Noirmont', 'Conseil communal du Noirmont'],
       ['Saignelégier', 'Saignelégier',
        'Conseil communal du Saignelégier'],
       ['St-Brais', 'St-Brais', 'Conseil communal de St-Brais'],
       ['Soubey', 'Soubey', 'Conseil communal de Soubey']], dtype=object)
    , columns=["Commune", "Localite", "Distributeur"])
#########################################################################################


# Input: input_str : input string
# Output: final_str : input string without any accents
def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    final_str = only_ascii.decode('utf-8')
    return final_str

def get_commune(x, listing):
    commune = x
    village = None
    distributeur = None
    
    if x in listing.Commune.values:
        locs = listing[listing.Commune == x].Localite.values
        if x in locs:
            village = x
        elif len(locs) == 1:
            village = locs[0]
        else:
            pass
    elif x in listing.Localite.values:
        village = x
        commune = list(listing[listing.Localite == x].Commune.values)[0]
    
    distributeur = list(listing[listing.Commune == commune].Distributeur.values)[0] if len(listing[listing.Commune == commune]) > 0 else commune
    
    return village, commune, distributeur


def from_relational_table_to_df(df_Analysis, df_Parameter, df_Echantillon, df_Location, df_Sampler):
    df_Analysis_Parameter = pd.merge(df_Analysis, df_Parameter, left_on="ParamID", right_on="ID", how="inner").drop(columns=["ParamID", "ID_y"]).rename(columns={"ID_x": "ID"})
    df_Echantillon_Location = pd.merge(df_Echantillon, df_Location, left_on="AddressID", right_on="ID", how="inner").drop(columns=["AddressID", "ID_y"]).rename(columns={"ID_x": "ID"})
    df_Echantillon_Location_Sampler = pd.merge(df_Echantillon_Location, df_Sampler, left_on="SamplerID", right_on="ID", how="inner").drop(columns=["SamplerID", "ID_y"]).rename(columns={"ID_x": "ID"})
    merged = pd.merge(df_Analysis_Parameter, df_Echantillon_Location_Sampler, left_on="EchantillonID", right_on="ID", how="inner").drop(columns=["EchantillonID", "ID_y"]).rename(columns={"ID_x": "ID"})

    merged["Sampler"] = merged.FirstName.map(lambda x: x + " ") + merged.LastName
    merged.Sampler.map(lambda x: str(x).replace('None', "").strip())
    merged.Sampler = merged.Sampler.map(lambda x: None if x == "None None" else x)
    merged.drop(columns=["FirstName", "LastName"], inplace=True)
    
    merged = merged.rename(columns={"Nom": "Parametre"})
    
    merged.drop(columns=["ID"], inplace=True)
    
    return merged


    
def from_df_to_relational_table(df):
    col_Analysis = ["ID", "ParamID", "EchantillonID", "Valeur", "AnalysisTime"]
    col_Parameter = ["ID", "Nom", "Group", "Unit", "Limit"]
    col_Echantillon = ["ID", "LocationID", "personID", "Code", "FloconsNb", "SamplingMethod", "Temperature"]
    col_Location = ["ID", "Address", "WaterType", "Treatment", "Village", "Commune", "Distributeur"]
    col_Sampler = ["ID", "SamplerName"]
    
    df_Parameter = df[["Parametre", "Group", "Unit", "Limit"]].drop_duplicates().reset_index(drop=True).reset_index(drop=False)
    df_Parameter = df_Parameter.rename(columns={"index": "ID", "Parametre": "Nom"})#, "Unite": "Unit"})
    df_Parameter = df_Parameter[col_Parameter]
    df_Parameter = df_Parameter.drop_duplicates().reset_index(drop=True)
    
    df_Location = df[["Address", "WaterType", "Treatment", "Village", "Commune", "Distributeur"]].drop_duplicates().reset_index(drop=True).reset_index(drop=False)
    df_Location = df_Location.rename(columns={"index": "ID"})
    df_Location = df_Location[col_Location]
    df_Location = df_Location.drop_duplicates().reset_index(drop=True)
    
    df_Sampler = df[["Sampler"]].drop_duplicates()
    df_Sampler["FirstName"] = df_Sampler.Sampler.map(lambda x: str(x).split()[0] if x else "None")
    df_Sampler["LastName"] = df_Sampler.Sampler.map(lambda x: str(x).split()[1] if x and len(str(x).split())>1 else "None")
    #df_Sampler = df_Sampler.drop(columns=["Sampler"]) # as needed keep for instance
    df_Sampler = df_Sampler.reset_index(drop=True).reset_index(drop=False).rename(columns={"index": "ID"})
    df_Sampler = df_Sampler.drop_duplicates().reset_index(drop=True)
    
    df_Echantillon = df[["Address", "Sampler", "Code", "FloconsNb", "Temperature"]].drop_duplicates().reset_index(drop=True).reset_index(drop=False)
    df_Echantillon = df_Echantillon.rename(columns={"index": "ID"})
    address_dict = {v: k for k, v in df_Location.set_index("ID").Address.to_dict().items()}
    sampler_dict = {v: k for k, v in df_Sampler.set_index("ID").Sampler.to_dict().items()}
    df_Echantillon = df_Echantillon.replace({"Address": address_dict, "Sampler": sampler_dict})
    df_Echantillon = df_Echantillon.rename(columns={"Address": "AddressID", "Sampler": "SamplerID"})
    df_Echantillon = df_Echantillon.drop_duplicates().reset_index(drop=True)
    
    df_Analysis = df[["Parametre", "Code", "Unit", "Limit", "Address", "Sampler", "Value", "Date"]].drop_duplicates().reset_index(drop=True).reset_index(drop=False)
    df_Analysis = df_Analysis.rename(columns={"index": "ID"})
    df_Analysis = df_Analysis.replace({"Address": address_dict, "Sampler": sampler_dict})
    df_Analysis = df_Analysis.rename(columns={"Address": "AddressID", "Sampler": "SamplerID"})
    Echantillon_keys = ["Code", "AddressID", "SamplerID"]
    df_Analysis = df_Analysis.merge(df_Echantillon[["ID"]+Echantillon_keys].rename(columns={"ID": "EchantillonID"}), on=Echantillon_keys, how="inner").drop(columns=Echantillon_keys)
    Parameter_keys = ["Nom", "Unit", "Limit"]
    df_Analysis = df_Analysis.rename(columns={"Parametre": "Nom"}).merge(df_Parameter[["ID"]+Parameter_keys].rename(columns={"ID": "ParamID"}), on=Parameter_keys, how="inner").drop(columns=Parameter_keys)
    
    df_Analysis = df_Analysis.drop_duplicates().reset_index(drop=True)
    
    return df_Analysis.drop(columns=["ID"]), df_Parameter.drop(columns=["ID"]), df_Echantillon.drop(columns=["ID"]), df_Location.drop(columns=["ID"]), df_Sampler.drop(columns=["ID", "Sampler"])


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--filepath', required=True, help='path to the excel file to import')
    parser.add_argument('--locality', choices=['Alle', 'Asuel', 'Basse-Allaine', 'Bassecourt', 'Beurnevésin', 'Boncourt','Bonfol',
 'Bourrignon', 'Boécourt', 'Bressaucourt', 'Buix', 'Bure', 'Charmoille', 'Chevenez', 'Châtillon','Clos-du-Doubs', 'Coeuve',
 'Corban', 'Cornol', 'Courcelon', 'Courchapoix', 'Courchavon', 'Courfaivre', 'Courgenay', 'Courrendlin', 'Courroux', 'Courtedoux', 'Courtemaîche',
 'Courtételle', 'Damphreux', 'Damvant', 'Delémont', 'Develier', 'Ederswiler', 'Epauvillers', 'Epiquerez', 'Fahy', 'Fontenais',
 'Fregiécourt', 'Glovelier', 'Grandfontaine', 'Haute-Ajoie', 'Haute-Sorne', 'La Baroche', 'La Chaux-des-Breuleux', 'Lajoux',
 'Le Bémont', 'Le Noirmont', 'Les Bois', 'Les Breuleux', 'Les Emibois', 'Les Enfers', 'Les Genevez', 'Lugnez', 'Mervelier',
 'Mettembert', 'Miécourt', 'Montavon', 'Montenol', 'Montfaucon', 'Montignez', 'Montsevelier', 'Movelier', 'Muriaux', 'Ocourt',
 'Pleigne', 'Pleujouse', 'Porrentruy', 'Rebeuvelier', "Roche d'Or", 'Rocourt', 'Rossemaison', 'Saignelégier', 'Saulcy',
 'Seleute', 'Soubey', 'Soulce', 'Soyhières', 'St-Brais', 'St-Ursanne', 'Séprais', 'Undervelier', 'Val Terbi', 'Vellerat',
 'Vendlincourt', 'Vermes', 'Vicques'], required=True, help='commune/locality information')
    args = parser.parse_args()
    
    # Input data : New excel file
    df = pd.read_excel(args.filepath)
    
    # Remove accents for Parametre and WaterType
    df.Parametre = df.Parametre.map(lambda x: remove_accents(str(x)))
    df.WaterType = df.WaterType.map(lambda x: remove_accents(str(x)))
    
    # Input data : Previous database tables
    df_Analysis = pd.read_excel("Analysis.xlsx")
    df_Analysis.columns = ["ID", "Value", "Date", "EchantillonID", "ParamID"]
    df_Parameter = pd.read_excel("Parameter.xlsx")
    df_Parameter.columns = ["ID", "Nom", "Group", "Unit", "Limit"]
    df_Echantillon = pd.read_excel("Echantillon.xlsx")
    df_Echantillon.columns = ["ID", "AddressID", "SamplerID", "Code", "FloconsNb", "Temperature"]
    df_Location = pd.read_excel("Location.xlsx")
    df_Location.columns = ["ID", "Address", "WaterType", "Treatment", "Village", "Commune", "Distributeur"]
    df_Sampler = pd.read_excel("Sampler.xlsx")
    df_Sampler.columns = ["ID", "FirstName", "LastName"]
    
    df_orig = from_relational_table_to_df(df_Analysis, df_Parameter, df_Echantillon, df_Location, df_Sampler)
    
    # Handle empty values in New data
    df.rename(columns={"Unite": "Unit"}, inplace=True)
    df["Group"] = None
    df.Unit.fillna(value="None", inplace=True)
    df.Code.fillna(value=999, inplace=True)
    df.WaterType.fillna(value="None", inplace=True)
    df.Treatment.fillna(value="None", inplace=True)
    df.Sampler.fillna(value="None", inplace=True)

    for i, row in df.iterrows():
        if math.isnan(row.Limit):
            if row.Parametre in list(df_Parameter.Nom):
                df.at[i, "Limit"] = df_Parameter[df_Parameter.Nom == row.Parametre].Limit.values[0]
    df.Limit.fillna(value=999, inplace=True)

    # Extract the corresponding village, commune, distributeur information and integrate in in the dataframe
    df["Village"] = [get_commune(args.locality, CommuneLocalityDistributeur) for _ in range(len(df))]
    df["Commune"] = df["Village"].map(lambda x: x[1])
    df["Distributeur"] = df["Village"].map(lambda x: x[2])
    df["Village"] = df["Village"].map(lambda x: x[0])

    # Concat the original and the new data
    df_new = pd.concat([df_orig, df])
    
    # Split the dataframe into 5 relational tables
    df_Analysis, df_Parameter, df_Echantillon, df_Location, df_Sampler = from_df_to_relational_table(df_new)

    df_Analysis.to_excel("new_analysis.xlsx", index=False)
    df_Parameter.to_excel("new_parameter.xlsx", index=False)
    df_Echantillon.to_excel("new_echantillon.xlsx", index=False)
    df_Location.to_excel("new_location.xlsx", index=False)
    df_Sampler.to_excel("new_sampler.xlsx", index=False)

