import pdftotext

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

def add_to_csv(account_dictionary):


    

