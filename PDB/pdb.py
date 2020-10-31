from Bio.PDB import *

# Download estrutura 1BGA
pdb = PDBList()
pdb.retrieve_pdb_file('1BGA',file_format='pdb')

