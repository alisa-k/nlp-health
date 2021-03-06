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
import csv 
#from Bio.Entrez import efetch 

def searchPubMed(query, num_of_results):
    #Pubmed needs your email to warn you for searching for too many articles at once
    Entrez.email = 'k.alisa@columbia.edu' 
    if num_of_results > 1000:
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
    Entrez.email = 'k.alisa@columbia.edu' 
    if num_of_results > 20:
        raise ValueError('Search for less results! - \
                         Change the value in the num_of_results in \
                         searchPubMed function')
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
    #creates the file wherever this file is saved
    f = open(str(fileName), 'w')  
    for item in listOfAbstracts: 
        f.write("%s\n" % item)
    f.close()
    print('list converted to .txt file')

def list_to_csv(listOfAbstracts, fileName):
    #creates the file wherever this file is saved 
    f = open(str(fileName), 'w') 
    wr = csv.writer(f)
    wr.writerow(listOfAbstracts)
    f.close()
    print('list converted to .csv file')

#def PMID_list_to_txt(listofPMIDs, fileName):
    
if __name__ == '__main__':
    # get list of PMIDs
    results = searchPubMed("feet", 10)
    id_list = results.get('IdList')
    print(id_list) #this is the list of PMIDs
    
    #input your pmid below (as an integer)
    abstract = pmid_to_abstract(id_list[0])
    abstractsFromPMIDList = listPMID_to_abstract(id_list)
    #list_to_txt(abstractsFromPMIDList, 'abstracts')
    
    #create a list of searches of abstracts 
    #abstractSearchList = search_to_abstract('clinical notes', 5)

#    PMIDList = [26944234, 26944233, 26944229]
#    abstractsFromPMIDList = listPMID_to_abstract(id_list)
#    list_to_txt(abstractsFromPMIDList, 'abstracts')
#    
#    f = open('abstracts.txt', 'r')
#    contents = [line.split('\n') for line in f.readlines()]
#    #print(type(contents))
#    #print(contents)
#    #print(contents[0][0])
#    f.close()
    
#    
#    list_to_csv(abstractsFromPMIDList, 'test131')
#    
#    f1 = open('/Users/hannah/Documents/NLPHealth/WCM-Course/test131.csv', 'r')
#    contents2 = f1.read().splitlines()
#    print(type(contents2))
#    print(contents2)
#    
#    f2 = open('/Users/hannah/Documents/NLPHealth/WCM-Course/test131.csv', 'r')
#    reader = csv.reader(f2, delimiter = ',')
#    reopenedList = list(reader)
#    print(reopenedList[0][0])
    
#   f1.close()



