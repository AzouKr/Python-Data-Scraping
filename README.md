# Python-Data-Scraping

Vidal data scraping is a project based on data scrapping using Unitex and python to extract Drug (medics) information from [VIDAL](https://www.vidal.fr) website 
and match them with their prescriptions given to different patients . these last are saved in a big medical Corpus data file named 'corpus-medical.txt'. 

# Execution

To execute the project do the following steps :

 - Execute the python script **projetpy** to exctract drugs substances from [VIDAL](https://www.vidal.fr) Website
	 -  \>>python **projetpy. py**  letter1-letter2
	- letter1-letter2 arguments represent the range of characters : example 'A-Z'
	- the script will output two files **Subst.dic** and **info.txt**
	- subst.dic contains all substances extracted with the Unitex dictionary suffix added to fits Unitex dictionary format
	- info.txt contains extraction statistics 
	
 - Execute the python script **enrch. py** to ENRICH **subst.dic** dictionary by adding new substances from the file **corpus-medical.txt** into new dictionnary also it will delete duplicated occurrences and sort from **subst.dic** in the end 
	 -  \>>python **enrch. py** corpus-medical.txt 
	 - it outputs the results in **subst_enri.dic** and alters **subst.dic**
## **Unitex** Part
 - Open unitex in french

 - Move the files **subset_enri.dic**  **subset.dic** to the path of Unitex **DELA** folder located in User's documents folder 
	 - example of my path :

		>D:\Users\Asus\Documents\Unitex-GramLab\Unitex\French\Dela 
 - Apply preprocessing & lexical parsing to **corpus-medical.txt** 
 - Open **subset_enri.dic** in DELA and compress the dictionary into FST 
	 - you should see **subst_enri.bin** and **subs_enri.inf** as new files in DELA folder
 - do the same for **subset.dic**
 - (optional) Open **projetpy.grf** in FSgraph to visualize to visualize extraction graphs schema
 - Apply lexical ressources to the preprocessed text previously 
	 -select  **subst_enri.bin** and **subst.bin** in user ressources and **dela. fr** in system ressources
	 
