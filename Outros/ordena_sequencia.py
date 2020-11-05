from Bio import SeqIO
from functools import cmp_to_key

def compara(a,b):
    return len(a)-len(b)

# Lendo sequencias
sequencias = list(SeqIO.parse("NC_017108.ffn","fasta"))

# Realizando o ordenamento
sequencias = sorted(sequencias, key=cmp_to_key(compara))

# Gravando o resultado
if SeqIO.write(sequencias, "sequencias_ordenadas.fasta", "fasta"):
    print("Sequencias ordenadas com sucesso.")
else:
    print("Um erro ocorreu.")