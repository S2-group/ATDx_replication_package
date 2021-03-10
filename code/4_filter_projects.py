import json
import csv
import os
import ssl
import requests
import time

# Save JSON data into the given filePath
def save(file_path, data):
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile, indent=4, default=str)

def save_csv(file_path, data):
    with open(file_path, mode='w') as csv_file:
        
        fieldnames = list()
        for d in data:
            for f in d.keys():
                if not (f in fieldnames):
                    fieldnames.append(f)

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        
        for d in data:
            writer.writerow(d)

def filter_projects(projects_path, json_output_path, csv_output_path, projects):
        all_projects = json.load(open(projects_path, 'r'))
        filtered_projects = list()
        for p in all_projects:
            if p['organization'] in projects:
                filtered_projects.append(p)
        save(json_output_path, filtered_projects)
        save_csv(csv_output_path, filtered_projects)
        
if __name__ == "__main__":
    
    # filter_projects('./data/merged_projects.json', './data/filtered_projects.json', './data/filtered_projects.csv', ['onap', 'apache'])
