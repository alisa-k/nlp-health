"""
 Full discussion:
 https://marcobonzanini.wordpress.com/2015/01/12/searching-pubmed-with-python/
 
 IMPORTANT: 
 In order not to overload the E-utility servers, NCBI recommends that users 
 post no more than three URL requests per second and limit large jobs to either
 weekends or between 9:00 PM and 5:00 AM Eastern time during weekdays. Failure 
 to comply with this policy may result in an IP address being blocked from 
 accessing NCBI. If NCBI blocks an IP address, service will not be restored 
 unless the developers of the software accessing the E-utilities register values 
 of the tool and email parameters with NCBI. 
 (see more at https://www.ncbi.nlm.nih.gov/books/NBK25497/ )
"""

from Bio import Entrez
import csv 

def searchPubMed(query, num_of_results):
    #Pubmed needs your email to warn you for searching for too many articles at once
    Entrez.email = 'k.alisa@columbia.edu' 
    if num_of_results > 30:
        raise ValueError('Search for less results! - \
                         Change the value in the num_of_results in \
                         searchPubMed function')
    else: 
        handle = Entrez.esearch(db='pubmed', 
                            sort='relevance', 
                            retmax= num_of_results,
                            retmode='text', # 'xml' , 'text'
                            term=query)
        results = Entrez.read(handle)
    return results

def pmid_to_abstract2(pmid): 
    handle = Entrez.efetch(db="pubmed", id=pmid,
                       rettype="abstract", retmode="text")
    return handle.read()

def pmid_to_abstract(pmid): 
    '''Just gets abstract text'''
    handle = Entrez.efetch(db="pubmed", id=pmid ,
                       rettype="xml", retmode="text")
    records = Entrez.read(handle)
    try:
        abstractlist = records['PubmedArticle'][0]['MedlineCitation']['Article']['Abstract']['AbstractText']
        if len(abstractlist) > 1: 
            abstract = ''
            for eachsection in abstractlist: 
                abstract += str(eachsection)
            return abstract
        else: 
            return abstractlist[0]
    except KeyError:
        return "error"

def get_data_txt(search_term):
    results = searchPubMed(search_term, 10)
    pmid_list = results.get('IdList')
    
    f = open("data/" + search_term + ".txt", 'a')
    for i in range(len(pmid_list)):
        print(search_term + " " + str(i))
        #f.write(pmid_list[i] + ": %s\n" % pmid_to_abstract(pmid_list[i]))
        f.write("%s\n" % pmid_to_abstract(pmid_list[i]))
    f.close()
    
def get_data_csv(search_term):
    results = searchPubMed(search_term, 30)
    pmid_list = results.get('IdList')
    
    f = open("data/heart_attack.csv", "a")
    wr = csv.writer(f)
    for i in range(len(pmid_list)):
        if pmid_to_abstract(pmid_list[i]) != "error":
            print(search_term + " " + str(i))
            wr.writerow([pmid_list[i], search_term, pmid_to_abstract(pmid_list[i])])
    f.close()
        
if __name__ == '__main__':
    search_terms = ["heart attack"]
    f = open("data/heart_attack.csv", "w")
    wr = csv.writer(f)
    wr.writerow(["pmid", "label", "abstract"])
    f.close()
    for term in search_terms:
        get_data_csv(term)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
