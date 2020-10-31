from Bio.PDB import *
 
parser = PDBParser()

estrutura = parser.get_structure('BGA', '1BGA.pdb')

for modelo in estrutura:
    print("Modelo: ", modelo.id)
    for cadeia in modelo:
        print("\t - Cadeia:",cadeia.id)
        # Reescreve numeração de resíduos não continuos
        i = 1
        for residuo in cadeia:
            # Remove heteroatomos
            if residuo.id[0] != ' ':
                cadeia.detach_child(residuo.id)
            else:
                residuo.id= (' ',i,' ')
                i += 1
                print("\t\t - Resíduo: ", residuo.resname, \
                    "(",residuo.id[1],")")
                for atomo in residuo:
                    print("\t\t\t - Atomo: ",atomo.name, \
                        "-> Coordenadas: ( X:",atomo.coord[0], \
                            "- Y:",atomo.coord[1],"- Z:", \
                                atomo.coord[2],")")

#Salvando alterações

w = PDBIO()

w.set_structure(estrutura)
w.save('nova_1BGA.pdb')

'''
# ATOMOS 
a.get_name()      # nome do atomo
a.get_id()        # id
a.get_coord()     # coordenadas atomicas
a.get_vector()    # coordenadas como vetor
a.get_bfactor()   # fator B 
a.get_occupancy() # ocupancia
a.get_altloc()    # localizacao alternativa
a.get_sigatm()    # parametros atomicos
a.get_anisou()    # fator B anisotropico
a.get_fullname()  # nome completo do atomo
 
# RESIDUOS
r.get_resname()   # retorna o nome do residuo
r.has_id(name)    # testa se ha certo atomo
'''