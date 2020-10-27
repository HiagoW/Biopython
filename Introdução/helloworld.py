from Bio.Seq import Seq

minha_sequencia = Seq("AGTACACTGGT")
print(minha_sequencia)

# Sequência complementar
print(minha_sequencia.complement())

# Sequência reverso complementar
print(minha_sequencia.reverse_complement())

# Transcrição
dna = Seq("ATGGCCATTCGCAAGGGTGCCCGATAG")
print("DNA:"+dna)

rna = dna.transcribe()
print("RNA:"+rna)

dna2 = rna.back_transcribe()
print("DNA:"+dna2)

# Tradução
print(rna.translate())
print(dna.translate())