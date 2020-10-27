from Bio.Blast.Applications import *

# Alternativa se não achar o comando
# blastn = "/usr/local/ncbi/blast/bin/blastn"
# comando_blastn = NcbiblastnCommandline( cmd=blastn \ ...

comando_blastn = NcbiblastnCommandline( \
    query="exemplo.fasta", subject="exemplo2.fasta", \
        outfmt=0, out="out.txt")
print(comando_blastn)

# Executando
stdout, stderr = comando_blastn()

# Abrindo resultado
blast_result = open("out.txt","r")

linhas = blast_result.read()
print(linhas)