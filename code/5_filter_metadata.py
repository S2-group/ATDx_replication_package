import csv
import json
import re
import pandas as pd

def csv_join(csv1, csv2):
    df1=pd.read_csv(csv1)
    df2=pd.read_csv(csv2)
    result=df1.merge(df2,on="projectKey", how="outer")
    result.to_csv("ATDx_input.csv")

def filter_metadata(project_metadata, organization, ar_issues_path):
    counted_ar_issues = {}
 
    project_values = []

    metrics = ['files', 'classes', 'functions', 'ncloc_language_distribution']

    j = 0

    for i in project_metadata:
        files = 0
        classes =0
        functions = 0
        ncloc_java = 0

        project = i['component']
        projectKey = project['key']
        
        for current_measure in project['measures']:

            if current_measure['metric'] in metrics:


                if current_measure['metric'] == 'ncloc_language_distribution':
                    
                    try:
                        ncloc_java = re.search('java=([0-9]*)', current_measure['value']).group(1)
                        
                    except AttributeError:
                        ncloc_java = '0'

                if current_measure['metric'] == 'files':
                    files = current_measure['value']

                if current_measure['metric'] == 'classes':
                    classes = current_measure['value']

                if current_measure['metric'] == 'functions':
                    functions = current_measure['value']   

        project_values.append([projectKey, ncloc_java, files, classes, functions])
        print(project_values[j])               

        j += 1

    with open("./data/onap_metadata.csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(project_values)

    
if __name__ == "__main__":
    #project_metadata = json.load(open('./dataonap_mined_project_measures.json', 'r'))
    #filter_metadata(project_metadata, 'onap', './data/onap_ar_issues.csv')
    csv_join("./data/onap_metadata.csv", "./data/onap_ar_issues.csv")
