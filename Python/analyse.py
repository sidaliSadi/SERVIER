import pandas as pd
import json

def load_data(file):
    """
    input : file path
    output: dataframe

    """
    return pd.read_csv(file, sep = ",")

def get_publications_journal(drugs, publications_journal):
    """
    input: 
        drugs: liste de noms des medicaments
        publications_journal: liste de tuples [(publicationTitle, Journal, data)]

        Output:
            Une liste de liste, pour chaque medicament renvoyer les titres de publications les journaux ainsi que les dates
            [[(titre 1, 'Journal A', '01/01/2019'), ('titre 2', 'Journal  D', '01/01/2019')], [(,,), (,,), .....], ......, ]
            chaque element de cette lisqte represente un médicament avec sa/ses publications
    """
    res = []
    for drug in drugs:
        pub_journal_about_drug = []
        for pub, journal, date in publications_journal:
            if drug.lower() in pub.lower():
                pub_journal_about_drug.append((pub, journal, date))
        res.append(pub_journal_about_drug)
        pub_journal_about_drug = []
    return res

def get_trials(drugs, trials):
    """
    input: 
        drugs: liste de noms des medicaments
        trials: liste de tuples [(trialTitle, data)]

        Output:
            Une liste de liste, pour chaque medicament renvoyer les titres des essais ainsi que les dates
            [[(titre 1, '01/01/2019'), ('titre 2', '01/01/2019')], [(,), (,), .....], ......, ]
            chaque element de cette liste represente un médicament avec son/ses essais
    """
    res = []
    for drug in drugs:
        trial_about_drug = []
        for trial, date in trials:
            if drug.lower() in trial.lower():
                trial_about_drug.append((trial, date))
        res.append(trial_about_drug)
        trial_about_drug = []
    return res

def write_res(liste, fileName):
    """
    Input: 
        liste de tuples: [(medicament, [liste de publications], [liste d'essais]]
        fileName: le nom de fichier de sortie

    Output: 
        convertir la liste en fichier json et le sauvegarder
    """
    output = []
    myDict = {}
    for drug, publications, trials in liste:
        myDict['drug'] = drug
        pubDict = {}
        tmp_list = []

        for pubTitle, journal, pubDate in publications:
            pubDict['pubTitle'] = pubTitle
            pubDict['journal'] = journal
            pubDict['pubDate'] = pubDate
            tmp_list.append(pubDict)
            pubDict = {}
        myDict['publications'] = tmp_list
        tmp_list = []
        trialDict = {}  
        for trialTitle, trialDate in trials:
            trialDict['trialTitle'] = trialTitle
            trialDict['trialDate'] = trialDate
            tmp_list.append(trialDict)
            trialDict = {}
        myDict['trials'] = tmp_list
        output.append(myDict)
        myDict = {}
    with open(fileName, "w") as outfile:
        json.dump(output,outfile, indent=4)

