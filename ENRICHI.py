import re
import sys
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cormed=open(sys.argv[1],'r',encoding="utf-8").readlines()
subst_corpus=open("subst_corpus.dic",'w',encoding='utf-16-le')
subst_corpus.write('\ufeff\n') #génération du BOM
info3=open ("info3.txt",'w',encoding='utf-8')
info2=open ("info2.txt",'w',encoding='utf-8')
list=[]
list_inter=[]
cpt=0

# copier le contenu de subst dans une liste intermédiaire en cas il y aura des nouveaux medicaments apres l’enrichissement
subst=open("subst.dic",'r',encoding='utf-16-le').readlines()
for i in subst:
    list_inter.append(i)
list_inter=sorted(set(list_inter))


subst=open("subst.dic",'a',encoding='utf-16-le')

for i in cormed:
    x=re.search("^-? ?(\w+) :? ?(\d+|,)+ (mg|ml).+",i,re.I)
    if x!=None:
        cpt+=1
        subst.write(x.group(1).lower()+",.N+subst\n")
        subst_corpus.write(x.group(1).lower()+",.N+subst\n")
info2.write("-le nombre total de medicaments issus du corpus  "+str(cpt)+"\n") 
subst.close()
subst_corpus.close()
subst_corpus=open("subst_corpus.dic",'r',encoding='utf-16-le').readlines()
for lettre in alphabet:
    cpt=0
    for i in subst_corpus:
        
        if i.startswith(str(lettre)):
            cpt+=1
            
    info2.write("-le nombre de medicaments issus du corpus pour la lettre  "+lettre+"  est :"+str(cpt)+"\n")
subst=open("subst.dic",'r',encoding='utf-16-le')

#Trier par ordre croissant (a-z) les éléments du dictionnaire « subst.dic » enrichi:
for i in subst:
    list.append(i)
list=sorted(set(list))
subst.close()
#réecrire ses éléments dans le fichier mais triés:
subst=open("subst.dic",'w',encoding='utf-16-le')
for i in list:
    subst.write(i)
subst.close()

# Creation de fichier info3.txt
subst_corpus=open("subst_corpus.dic",'r',encoding='utf-16-le').readlines()
cpt=0
totale=0
for i in subst_corpus:
    list.append(i)
list=sorted(set(list))

for lettre in alphabet:
    cpt=0
    for i in list:
        if i not in list_inter: 
            if i.startswith(str(lettre)):
                cpt+=1
            
    info3.write("- le nombre total de médicaments issus de l’enrichissement pour la lettre  "+lettre+"  est :"+str(cpt)+"\n")
    totale=totale+cpt
    
info3.write("-le nombre total de medicaments issus de l’enrichissement  "+str(totale)+"\n") 
    