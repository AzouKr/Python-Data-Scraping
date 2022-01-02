import re,sys
import urllib.request #définir les fonctions et les classes qui permet d'ouvrir les URLs
alphabet= "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z" 
a= alphabet.split(' ')
subst= open("subst.dic","w",encoding='utf-16-le')
subst.write('\ufeff\n') #génération du BOM
subst.close()
intervalle=sys.argv[1]
if not re.match(r'[A-Za-z][-][A-Za-z]', sys.argv[1]):
		print("\n\t\t\t Argument mal saisi.\n")
else:
	 print("START:")
t=intervalle.split("-")
DEBUT=t[0]
FIN=t[1]
port=sys.argv[2]
nbtotal=0 #compteur total
info1=open("infos1.txt",'w',encoding='utf-8') 
for i in a:
    if (i.lower()>=DEBUT.lower()) and (i.lower() <= FIN.lower()) :
        nbsub=0
        print("Traitement des substances dont le nom commence par la lettre "+i+".")
        url=urllib.request.urlopen("http://127.0.1.1:"+port+"/vidal/vidal-Sommaires-Substances-"+i+".htm")
        l=url.readlines()
        subst= open("Subst.dic","a",encoding='utf-16-le')
        for h in l:
            hh=str(h.decode("UTF-8"))
            temp=re.search("\\s+<a href=\"Substance.+>(.+)</a>",str(hh))
            if(temp!=None):
                subst.write(str(temp.group(1))+",.N+subst\n")
                nbsub+=1
        subst.close()
        info1.write("-Le nombre de substances de la lettre "+i+" est : "+str(nbsub)+".\n")
        nbtotal+=nbsub
print("\t\t\tEXTRAIRE terminée.")		
print("\n")		
info1.write("//****************RESULTAT****************//\n")
info1.write("Le nombre total de substances aspirees entre ses deux lettres est de : "+str(nbtotal)+".\n")
info1.close