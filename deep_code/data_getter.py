from Bio import Entrez
from dotenv import load_dotenv
import os
from pathlib import Path


env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)


Entrez.email = os.getenv("NCBI_EMAIL")
Entrez.api_key = os.getenv("NCBI_API_KEY")


handle = Entrez.esearch(db="nucleotide", term="BRCA1[Gene]", retmax=10)
record = Entrez.read(handle)
handle.close()

print(record)