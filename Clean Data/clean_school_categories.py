'''Further clean categorization of schools data'''
import csv

files = ["cleaned_Assessmentoptions.csv", "cleaned_Assessmentcombo.csv", "cleaned_Assessment912.csv"]
magnets = ["DISNEY II HS", "VON STEUBEN HS", "CHICAGO AGRICULTURE HS", "CRANE MEDICAL HS", "DEVRY HS", "CURIE HS", "CLARK HS"]
se = ["BROOKS HS", "JONES HS", "KING HS", "LANE TECH HS", "LINDBLOM HS", "NORTHSIDE PREP HS", "PAYTON HS", "SOUTH SHORE INTL HS", "WESTINGHOUSE HS", "YOUNG HS" ]

def rename_categories(files,magnets):
    for f in files:
        print(f)
        new = f[:-4] + "_final.csv"
        with open(f) as fin, open(new, 'w') as f1:
            dr = csv.DictReader(fin,fieldnames=["School ID","School Name","Network","Rating"])
            writer = csv.writer(f1)
            for i in dr:
                category = i["Network"].title()
                if i["School Name"] == "LINDBLOM HS":
                    print(i)
                if "NETWORK" in i["Network"]:
                    print(i["School Name"])
                    category = "Neighborhood"
                if i["Network"] == "SERVICE LEADERSHIP ACADEMIES":
                    category = "Military Academy"
                if i['School Name'] in magnets:
                    category = "Magnet"
                if i['School Name'] in se:
                    category = "Selective Enrollment"
                if i["School Name"][-2:] == "HS":
                    name = i["School Name"][:-3].title() + " High School"
                else:
                    name = i["School Name"].title() + "High School"
               
                line = [i['School ID'],name, category, i['Rating']]            
                writer.writerow(line)
