from Bio.PDB import *

# Cria objeto PDBParser
parser = PDBParser()

# Declara estrutura
estrutura = parser.get_structure('BGA', '1BGA.pdb')
cabecalho = parser.get_header()

# Método de determinação da estrutura
metodo = estrutura.header['structure_method']

# Resolução
resolucao = estrutura.header['resolution']

print("Método: ", metodo)
print("Resolução: ", resolucao)
