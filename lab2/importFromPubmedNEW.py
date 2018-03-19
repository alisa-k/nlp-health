# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 13:24:27 2018

@author: ham2026


 you need to install Biopython:
 pip install biopython

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
#from Bio.Entrez import efetch 

def searchPubMed(query, num_of_results):
    #Pubmed needs your email to warn you for searching for too many articles at once
    Entrez.email = 'k.alisa@columbia.edu' 
    if num_of_results > 20:
        raise ValueError('Search for less results! - Change the value in the num_of_results in searchPubMed function')
    else: 
        handle = Entrez.esearch(db='pubmed', 
                            sort='relevance', 
                            retmax= num_of_results,
                            retmode='text', # 'xml' , 'text'
                            term=query)
        #print(handle.url)
        results = Entrez.read(handle)
    return results

#bad output format
def pmid_to_abstract2(pmid): 
    handle = Entrez.efetch(db="pubmed", id=pmid,
                       rettype="abstract", retmode="text")
    return handle.read()

# try to get JUSt the abstract text 
def pmid_to_abstract(pmid): 
    handle = Entrez.efetch(db="pubmed", id=pmid ,
                       rettype="xml", retmode="text")
    records = Entrez.read(handle)
    abstractlist = records['PubmedArticle'][0]['MedlineCitation']['Article']['Abstract']['AbstractText']
    if len(abstractlist) > 1: 
        abstract = ''
        for eachsection in abstractlist: 
            abstract += str(eachsection)
        return abstract
    else: 
        return abstractlist[0]

def search_to_abstract(searchText, num_of_results):
    Entrez.email = 'yourEmail@med.cornell.edu' 
    if num_of_results > 20:
        raise ValueError('Search for less results! - Change the value in the num_of_results in searchPubMed function')
    else: 
        handle = Entrez.esearch(db='pubmed', 
                            sort='relevance', 
                            retmax= num_of_results,
                            retmode='text', # 'xml' , 'text'
                            term=searchText)
        
        results = Entrez.read(handle)
    abstractSearched = []
    for each in results.get('IdList'): 
        handle = Entrez.efetch(db="pubmed", id=each ,
                       rettype="xml", retmode="text")
        records = Entrez.read(handle)
        abstractlist = records['PubmedArticle'][0]['MedlineCitation']['Article']['Abstract']['AbstractText']
        if len(abstractlist) > 1: 
            abstract = ''
            for eachsection in abstractlist: 
                abstract += str(eachsection)
            abstractSearched.append(abstract)
        else: 
            abstractSearched.append(abstractlist[0])
    return abstractSearched
        
def listPMID_to_abstract(listOfPMID): 
    abstractSearched = []
    for each in listOfPMID: 
        handle = Entrez.efetch(db="pubmed", id=each ,
                       rettype="xml", retmode="text")
        records = Entrez.read(handle)
        abstractlist = records['PubmedArticle'][0]['MedlineCitation']['Article']['Abstract']['AbstractText']
        if len(abstractlist) > 1: 
            abstract = ''
            for eachsection in abstractlist: 
                abstract += str(eachsection)
            abstractSearched.append(abstract)
        else: 
            abstractSearched.append(abstractlist[0])
    return abstractSearched

# need to edit to allow for list object to be intact when opening 
def list_to_txt(listOfAbstracts, fileName):
    f = open(fileName, 'w')
    for each in listOfAbstracts:
        f.write(each + "\n")
    f.close()
    print('list converted to .txt file')

if __name__ == '__main__':
    num_of_results = 3
    results = searchPubMed("natural language processing", 3)
    id_list = results.get('IdList')
    print(id_list) #this is the list of PMIDs
    
    #create a list of searches of abstracts 
    abstractSearchList = search_to_abstract('clinical notes', 5)
    abstractsFromPMIDList = listPMID_to_abstract([26944234, 26944233, 26944229])
    list_to_txt(abstractsFromPMIDList, '../abstract.txt')




