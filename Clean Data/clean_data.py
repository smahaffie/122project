import csv
import subprocess
import json


def clean_data(collenrollpersist_filename, act_filename, freshontrack_filename, mainhs_filename, combohs_filename, optionshs_filename):
    '''
    Contains all the commands to clean all of the csvs required to build the data base
    '''

    '''
    Clean college enrollment and persistence data
    '''

    COMMAND = '''awk 'BEGIN {FS = "|"};{print $1"|"$3"|"$5"|"$10}' < collenrollpersist_filename > 'Data_Files/CEP.csv' '''
    subprocess.call(COMMAND, shell=True)
    with open("Data_Files/CEP.csv",'r') as f, open("Data_Files/cleaned_CEP.csv",'w') as f1:
        next(f) 
        for line in f:
            f1.write(line)

    '''
    Clean ACT data
    '''

    COMMAND = '''awk 'BEGIN {FS = "|"};{print $2"|"$4"|"$5"|"$7"|"$12"|"$17}' < act_filename > 'Data_Files/ACT.csv' '''
    subprocess.call(COMMAND, shell=True)
    with open("Data_Files/ACT.csv", 'r') as f, open("Data_Files/cleaned_ACT.csv",'w') as f1:
        next(f)
        next(f)
        f1.write("School ID|Category|Category Type|Year|Composite Score Mean|Total Tested" + '\n')
        for line in f:
            f1.write(line)

    '''
    Clean freshman on track data
    '''

    COMMAND = '''awk 'BEGIN {FS = "|"};{print $1"|"$3"|"$4}' < freshontrack_filename > 'Data_Files/FOT.csv' '''
    subprocess.call(COMMAND, shell=True)
    with open("Data_Files/FOT.csv", 'r') as f, open("Data_Files/cleaned_FOT.csv",'w') as f1:
        next(f)
        next(f)
        f1.write("School ID|On Track Rate|Total Number of Freshman" + '\n')
        for line in f:
            f1.write(line)

    '''
    Clean category and rating data contained in 3 csvs
    '''

    COMMAND = '''awk 'BEGIN {FS = "|"};{print $1"|"$2"|"$3"|"$5}' < mainhs_filename > 'Data_Files/Assessment912.csv' '''
    subprocess.call(COMMAND, shell=True)
    with open("Data_Files/Assessment912.csv", 'r') as f, open("Data_Files/cleaned_Assessment912.csv",'w') as f1:
        next(f)
        next(f)
        next(f)
        next(f)
        f1.write("School ID|School Name|Network|Rating" + '\n')
        for line in f:
            print(line)
            f1.write(line)

    COMMAND = '''awk 'BEGIN {FS = "|"};{print $1"|"$2"|"$3"|"$9}' < combohs_filename > 'Data_Files/Assessmentcombo.csv' '''
    subprocess.call(COMMAND, shell=True)
    with open("Data_Files/Assessmentcombo.csv", 'r') as f, open("Data_Files/cleaned_Assessmentcombo.csv",'w') as f1:
        next(f)
        next(f)
        next(f)
        next(f)
        f1.write("School ID|School Name|Network|Rating" + '\n')
        for line in f:
            f1.write(line)

    COMMAND = '''awk 'BEGIN {FS = "|"};{print $1"|"$2"|"$3"|"$5}' < optionshs_filename > 'Data_Files/Assessmentoptions.csv' '''
    subprocess.call(COMMAND, shell=True)
    with open("Data_Files/Assessmentoptions.csv", 'r') as f, open("Data_Files/cleaned_Assessmentoptions.csv",'w') as f1:
        next(f)
        next(f)
        next(f)
        next(f)
        f1.write("School ID|School Name|Network|Rating" + '\n')
        for line in f:
            print(line)
            f1.write(line)

def create_website_dict(website_csv_file):
    with open(website_csv_file,'r') as f, open("{}_cleaned.csv".format(website_csv_file[:-4]),"w") as f1:
        f.readline()
        reader = csv.DictReader(f,fieldnames = ["Schoolname","School ID", "Website"])
        writer = csv.writer(f1,delimiter = "|")
        for row in reader:
            line = [row["School ID"],row["Website"]]
            writer.writerow(line)