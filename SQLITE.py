import sqlite3, re

concord = open('corpus-medical_snt/concord.html','r')
res = re.findall(r'<a href=\"[0-9 ]+\">.+</a>',concord.read())

for i in range(len(res)):
    res[i] = re.findall(r'>.+<',res[i])[0][1:-1]

conn = sqlite3.connect('extraction.db') 

#On crée la table (extraction) en utilisant les commandes SQL
conn.execute("CREATE TABLE extraction(id INTEGER , posologie TEXT)")
i=1

#On insere les POSOLOGIE dans la table (extraction)
for line in res:
     conn.execute("INSERT INTO extraction VALUES (?,?)",(str(i),line))
     i=i+1
  
    
conn.commit()
