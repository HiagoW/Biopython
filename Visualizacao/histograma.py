from Bio import SeqIO
import pylab

# Recebendo arquivo GBK
exemplo = SeqIO.read("NC_017108.gbk", "genbank")
tamanhos = []

# Obtendo quantidade de aminoácidos em sequencias
for i in exemplo.features:
    if i.type == 'CDS':
        tamanhos.append(len(i.qualifiers['translation'][0]))

# Gerando a figura
pylab.hist(tamanhos, bins=20)
pylab.title("Histograma - frequencia de sequencias")
pylab.xlabel("Tamanho de sequencia (bp)")
pylab.ylabel("Quantidade")
pylab.show()