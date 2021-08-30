import json
import operator

def get_max(journaux, filePath):
    """
    Input:
        journaux : liste des journaux
        filePath: le chemin vers le fichier json
    Output:
         le nom du journal qui mentionne le plus de médicaments différents
    """
    dic = dict.fromkeys(journaux, 0)
    with open(filePath) as f:
        data = json.load(f)
 
    # printing data after loading the json file
    for drug in data:
        journalSet = set()
        for pub in drug['publications']:
            journalSet.add(pub['journal'])
        for journal in journalSet:
            dic[journal] = dic[journal] + 1
    return max(dic.items(), key=operator.itemgetter(1))[0]