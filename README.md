# Python-Data-Scraping

Vidal data scraping is a project based on data scrapping using Unitex and python to extract Drug (medics) information from [VIDAL](https://www.vidal.fr) website 
and match them with their prescriptions given to different patients . these last are saved in a big medical Corpus data file named 'corpus-medical.txt'. 

# Execution

To execute the project do the following steps :

 - Execute the python script **EXTRAIRE.py** to exctract drugs substances from [VIDAL](https://www.vidal.fr) Website
	 -  \>>python **EXTRAIRE.py**  letter1-letter2 Port
	- letter1-letter2 arguments represent the range of characters : example 'A-Z'
	- Port arguments represent Port http : by default 80
	- the script will output two files **Subst.dic** and **info1.txt**
	- subst.dic contains all substances extracted with the Unitex dictionary suffix added to fits Unitex dictionary format
	- info.txt contains extraction statistics 
	
 - Execute the python script **ENRICHI.py** to ENRICH **subst.dic** dictionary by adding new substances from the file **corpus-medical.txt** into new dictionnary also it will delete duplicated occurrences and sort from **subst.dic** in the end 
	 -  \>>python **ENRICHI.py** corpus-medical.txt 
	 - it outputs the results in **subst_enri.dic** and alters **subst.dic**
	 - it outputs **info2.txt** and **info3.txt**
## **Unitex** Part
  -  \>>python **UNITEX.py**
 - script that calls unitex. To be able to unitize UnitexToolLogger, you must copy Unitex-GramLab \ App UnitexToolLogger.exe in Unitex-GramLab \ French
 
## **Data Base** Part 
  -  \>>python **SQLITE.py**
- script to inject the contents of the "concord.html" file into a SQLite database named "extraction.db", using Python's "sqlite3" module.
