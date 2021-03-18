import pdftotext
import csv

def pdf_to_text(filename): # returns account number and amount in a dictionary maybe
    account_dict= {}
    with open(filename,"rb") as f:
        pdf = pdftotext.PDF(f)
    
    str = "\n\n".join(pdf) #reads all the text into one string
    splits = str.split #splits into words array
    for words in splits: # prints all the words. Change it later according to real pdf. search the pdf for account number or specific key word
        print(words)


# How many pages?
#print(len(pdf))

# Iterate over all the pages
#for page in pdf:
 #   print(page)

# Read some individual pages
#print(pdf[0])

def add_to_csv(account_dictionary): #turns dictionary into csv file. Change later to account for edge cases(same account number... etc)
    csv_columns= ['Account Number', 'Amount']
    csv_file= 'Accounts.csv'
    try:
        with open(csv_file,'w') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames== csv_columns)
            writer.writeheader()
            for accounts in account_dictionary:
                writer.writerow(accounts)
    except IOError



    

