# Get SonarCloud API

import requests
import json
import math
import csv

# Save JSON data into the given filePath
def save(file_path, data):
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile, indent=4, default=str)

def mine_measures(projects_path, measures_path, organization_name):

    with open(projects_path) as json_data:
        projects_dict = json.load(json_data,)

        filtered_projects = list()

        for r in projects_dict:
            if r["organization"] == organization_name:
                filtered_projects.append(r) 

        url = 'https://sonarcloud.io/api/measures/component?'

        j = 0

        spec_project_list = list()
    
        for p in filtered_projects:
            p_key = p['key']

            query = {'componentKey': p_key, 'metricKeys': 'duplicated_blocks,duplicated_lines,duplicated_lines_density,violations,false_positive_issues,open_issues,confirmed_issues,reopened_issues,code_smells,sqale_rating,sqale_index,sqale_debt_ratio,bugs,reliability_rating,reliability_remediation_effort,vulnerabilities,security_rating,classes,comment_lines,comment_lines_density,directories,files,lines,ncloc,ncloc_language_distribution,functions'}

            r = requests.get(url, params=query)
            project_specs_new = r.json()

            spec_project_list.append(project_specs_new)

            j += 1
            print('Mined measures for project number ' + str(j))

    save(measures_path, spec_project_list)

def massage(project_measures_path, output_path):
    project_measures = json.load(open(project_measures_path, 'r'))

#     with open('repos_spec.json') as json_data:
#     repos_dict = json.load(json_data,)

# for repo in repos_dict:

#     key = repo['component']['key']
    
#     measurement_iterator = 0

#     measurements_tuples = []

#     for measure in repo['component']['measures']:
#         metric = repo['component']['measures'][measurement_iterator]['metric']
#         value = repo['component']['measures'][measurement_iterator]['value']
        
#         # create array of tuples (metric, value)
#         measurements_tuples.append((metric, value))

#         measurement_iterator += 1 

#     # sort metrics alphabetically
#     measurements_tuples.sort()

#     # write row of measurements for csv file
#     repo_row.append([x[1] for x in measurements_tuples])

#     repo_number += 1

# with open('metadata_sonarcloud.csv', 'a') as csvFile:
#     writer = csv.writer(csvFile)
    
#     for row_number in range(0, repo_number):
#         writer.writerow(repo_row[row_number])

# csvFile.close()

    print(len(project_measures))


if __name__ == "__main__":

    # mine_measures('./data/merged_projects.json', './data/onap_mined_project_measures.json', 'onap') 
    # mine_measures('./data/merged_projects.json', './data/apache_mined_project_measures.json', 'apache')

    # massage('./data/onap_mined_project_measures.json', './data/onap_total_metadata.csv') 
    # massage('./data/apache_mined_project_measures.json', './data/apache_total_metadata.csv') 
