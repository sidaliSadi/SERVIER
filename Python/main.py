import analyse as an
import adhoc as ad

if __name__ == "__main__":
    #Chargements des fichiers
    drugs = an.load_data('data/drugs.csv')
    publications = an.load_data('data/pubmed.csv')
    trials = an.load_data('data\clinical_trials.csv')

    
    pub_title_journal = list(zip(publications['title'], publications['journal'], publications['date']))
    drugs_name = drugs['drug'].tolist()
    trials_title_date = list(zip(trials['scientific_title'], trials['date']))
    journaux = publications['journal'].tolist()
    
    drug_trials = an.get_trials(drugs_name, trials_title_date)
    drug_publications = an.get_publications_journal(drugs_name, pub_title_journal)
    into_json = list( zip(drugs_name, drug_publications, drug_trials))

    an.write_res(into_json)
    print(ad.get_max(journaux, "sample.json"))