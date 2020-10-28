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

# ------------------------ BLAST Tabular ----------------------
# atributos: qlen, qstart, qend, slen, sstart, send, positive, gaps, mismatch e pident.

comando_blastn = NcbiblastnCommandline(\
    query="exemplo.fasta", subject="exemplo2.fasta",\
        outfmt='6 qlen qstart qend slen sstart send \
            positive gaps mismatch pident', out="out.txt")

print(comando_blastn)

stdout, stderr = comando_blastn()

blast_result = open("out.txt","r")

linhas = blast_result.read()
print(linhas)

#------------------ Criando BD local ----------------
'''
Executar o seguinte comando no terminal:

- Converte o arquivo exemplo.fasta em um banco de dados

makeblastdb -in exemplo.fasta -dbtype nucl -out exemplo_db -title exemplo_db

Erro de espaço insuficiente:
criar variável de ambiente: BLASTDB_LMDB_MAP_SIZE=1000000
https://www.biostars.org/p/413294/

'''

comando_blastn = NcbiblastnCommandline(\
    query="exemplo2.fasta", db="exemplo_db",\
        outfmt='6 qlen qstart qend slen sstart send \
            positive gaps mismatch pident', out="out.txt")

print(comando_blastn)

stdout, stderr = comando_blastn()

blast_result = open("out.txt","r")

linhas = blast_result.read()
print(linhas)