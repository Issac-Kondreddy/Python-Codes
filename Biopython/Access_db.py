from Bio import Entrez

Entrez.email = "issackondreddy@gmail.com"  # Always provide your email
search_term = "BioPython"

handle = Entrez.esearch(db="pubmed", term=search_term, retmax=10)
record = Entrez.read(handle)
handle.close()

print(f"Found {record['Count']} articles.")
print("IDs of the first 10 articles:", record['IdList'])
