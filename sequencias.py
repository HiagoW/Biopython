from Bio.Seq import Seq
from Bio import SeqIO

seq1 = Seq('AAA')
seq2 = Seq('TTT')
seq3 = Seq('CCC')
seq4 = Seq('GGG')

seq_final = seq1 + seq2 + seq3 + seq4

print(seq_final)

seq1 = Seq("AACCGGTT")
seq2 = Seq("AACCGGTT")
seq3 = Seq("TTCCAAGG")

if str(seq1) == str(seq2):
    print("seq1 igual a seq2")
else:
	print("seq1 diferente de seq2")

if str(seq1) == str(seq3):
	print("seq1 igual de seq3")
else:
	print("seq1 diferente de seq3")

#------------------FASTA (Leitura) ---------------------
for i in SeqIO.parse("arquivo.fasta","fasta"):

    # cabecalho
    print(i.id)

    # sequencia
    print(i.seq)

    # tamanho da sequencia
    print(len(i))

#---------------FASTA (Gravação) ----------------
entrada = open("arquivo1.fasta","r")
saida = open("arquivo2.fasta","w")

for i in SeqIO.parse(entrada,"fasta"):

    # Sequencias > 10pb e que começam com Citosina
    if len(i.seq)>10 and i.seq[0] == 'C':
        SeqIO.write(i, saida, "fasta")

saida.close()

#------------------GenBank------------------
for seq_record in SeqIO.parse("NC_009934.gbk","genbank"):

    print(seq_record.id)

    print(seq_record.seq)

    print(len(seq_record))

exemplo = SeqIO.read("NC_009934.gbk", "genbank")

# Imprime features (características do organismo)
for i in exemplo.features:
    print(i)

# Imprime nome de produtos codificados
for i in exemplo.features:
    if i.type == 'CDS':
        print(i.qualifiers['product'])

'''
Outras informações de features: 
tipo (type), 
localização (location), 
além de locus tag (qualifiers[‘locus_tag’]), 
id da proteína (qualifiers[protein_id]) e 
sequência traduzida (qualifiers[‘translation’]).
'''

#-----------Convertendo de GenBank para FASTA--------------
SeqIO.convert("NC_009934.gbk","genbank","NC_009934.fasta","fasta")