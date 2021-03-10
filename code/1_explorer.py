import json
import csv
import os
import ssl
import requests
import time

# Downloads a remote resource pointed by url into path
def get_from_sonarcloud(url, path, save_to_fs, field_to_check):
    response = requests.get(url)
    if response.status_code != 400:
        data = response.json()
        if(field_to_check is not None and not data[field_to_check]):
            return False
        if save_to_fs:
            save(path, data)
        else:
            return data
        return True
    else:
        print(response)
        return False

# Save JSON data into the given filePath
def save(file_path, data):
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile, indent=4, default=str)

def download_projects(sort_by, ascending_string):
    print('Start downloading projects for: ' + sort_by + ' --- ' + ascending_string)

    base_url = 'https://sonarcloud.io/api/components/search_projects?boostNewProjects=false&facets=ncloc%2Clanguages&p=PAGE_NUM&ps=10&f=organizations&filter=ncloc%20%3E%3D%201000&s=SORT_BY&asc=ASCENDING'

    page_num = 1

    reached_limit = False
    while(not reached_limit):
        url = base_url.replace('PAGE_NUM', str(page_num)).replace('ASCENDING', ascending_string).replace('SORT_BY', sort_by)
        reached_limit = not get_from_sonarcloud(url, './data/projects/projects_' + sort_by + '_' + ascending_string + '_' + str(page_num) + '.json', True, None)
        page_num += 1

def download_issues(org, project_key, sort_by, ascending_string):

    print('Start downloading issues for: ' + project_key + ' --- ' + sort_by + ' --- ' + ascending_string)

    base_url = 'https://sonarcloud.io/api/issues/search?p=PAGE_NUM&ps=10&s=SORT_BY&asc=ASCENDING&projectKeys=PROJECT_KEY'

    page_num = 1

    reached_limit = False
    while(not reached_limit):
        url = base_url.replace('PAGE_NUM', str(page_num)).replace('ASCENDING', ascending_string).replace('SORT_BY', sort_by).replace('PROJECT_KEY', project_key)
        reached_limit = not get_from_sonarcloud(url, './data/issues/issues_' + org + '_' + project_key + '_' + sort_by + '_' + ascending_string + '_' + str(page_num) + '.json', True, 'issues')
        page_num += 1


def merge_crawled_files(directory, prefix, suffix, field, target_file):

    print('Start merging files...')
    
    items = list()
    counter = 1

    dir_contents = os.listdir(directory)
    total = str(len(dir_contents))

    for f in dir_contents:
        print('Merging file ' + str(counter) + '/' + total)
        counter += 1
        filename = f
        if filename.startswith(prefix) and filename.endswith(suffix): 
            file_contents = json.load(open(os.path.join(directory, filename), 'r'))
            if field  in file_contents:
                items_in_file = file_contents[field]
                items.extend(items_in_file)
    
    merged_items = {}
    for p in items:
        merged_items[p['key']] = p
    
    save(target_file, merged_items)

def sort_organizations():
    organizations = {}

    projects = json.load(open('./data/merged_projects.json', 'r'))
    for p in projects:
        if not p['organization'] in organizations:
            organizations[p['organization']] = {'projects': 0, 'repos': 0}
        organizations[p['organization']]['projects'] += 1
        if 'repo_url' in p:
            organizations[p['organization']]['repos'] += 1

    sorted_organizations = {k: v for k, v in sorted(organizations.items(), key=lambda item: item[1]['projects'])}
    save('./data/sorted_organizations.json', sorted_organizations)
    return sorted_organizations


def download_all():
    download_projects('analysisDate', 'true')
    download_projects('alert_status', 'true')
    download_projects('coverage', 'true')
    download_projects('duplicated_lines_density', 'true')
    download_projects('lines', 'true')
    download_projects('name', 'true')
    download_projects('ncloc', 'true')
    download_projects('ncloc_language_distribution', 'true')
    download_projects('new_coverage', 'true')
    download_projects('new_duplicated_lines_density', 'true')
    download_projects('new_lines', 'true')
    download_projects('new_maintainability_rating', 'true')
    download_projects('new_reliability_rating', 'true')
    download_projects('new_security_rating', 'true')
    download_projects('reliability_rating', 'true')
    download_projects('security_rating', 'true')
    download_projects('sqale_rating', 'true')
    
    download_projects('analysisDate', 'false')
    download_projects('alert_status', 'false')
    download_projects('coverage', 'false')
    download_projects('duplicated_lines_density', 'false')
    download_projects('lines', 'false')
    download_projects('name', 'false')
    download_projects('ncloc', 'false')
    download_projects('ncloc_language_distribution', 'false')
    download_projects('new_coverage', 'false')
    download_projects('new_duplicated_lines_density', 'false')
    download_projects('new_lines', 'false')
    download_projects('new_maintainability_rating', 'false')
    download_projects('new_reliability_rating', 'false')
    download_projects('new_security_rating', 'false')
    download_projects('reliability_rating', 'false')
    download_projects('security_rating', 'false')
    download_projects('sqale_rating', 'false')

def check_github():
    projects = json.load(open('./data/merged_projects.json', 'r'))
    to_save = list()
    for p in projects.values():
        url = 'https://sonarcloud.io/api/navigation/component?component=' + p['key']
        data = get_from_sonarcloud(url, None, False, None)
        if 'alm' in data:
            repo_url = (data['alm']['url'])
            p['repo_url'] = repo_url
        to_save.append(p)
    save('./data/merged_projects.json', to_save)
    print(len(to_save))

def find_all_projects(organization_id, all_projects):
    result = list()
    for p in all_projects:
        if(p['organization'] == organization_id):
            result.append(p)
    return result

def mine_issues(organization_ids):
    all_organizations = json.load(open('./data/sorted_organizations.json', 'r'))
    all_projects = json.load(open('./data/merged_projects.json', 'r'))
    counter = 1
    for org in organization_ids:
        if org in all_organizations:
            projects = find_all_projects(org, all_projects)
            for p in projects:
                print(p['key'] + ' --- ' + str(counter) + '/' + str(len(projects)))
                counter += 1
                # CREATION_DATE, UPDATE_DATE, CLOSE_DATE, ASSIGNEE, SEVERITY, STATUS, FILE_LINE
                issues = download_issues(org, p['key'], 'CREATION_DATE', 'false')
                issues = download_issues(org, p['key'], 'UPDATE_DATE', 'false')
                issues = download_issues(org, p['key'], 'CLOSE_DATE', 'false')
                # issues = download_issues(org, p['key'], 'ASSIGNEE', 'false')
                issues = download_issues(org, p['key'], 'SEVERITY', 'false')
                issues = download_issues(org, p['key'], 'STATUS', 'false')
                issues = download_issues(org, p['key'], 'FILE_LINE', 'false')

                issues = download_issues(org, p['key'], 'CREATION_DATE', 'true')
                issues = download_issues(org, p['key'], 'UPDATE_DATE', 'true')
                issues = download_issues(org, p['key'], 'CLOSE_DATE', 'true')
                # issues = download_issues(org, p['key'], 'ASSIGNEE', 'true')
                issues = download_issues(org, p['key'], 'SEVERITY', 'true')
                issues = download_issues(org, p['key'], 'STATUS', 'true')
                issues = download_issues(org, p['key'], 'FILE_LINE', 'true')
        else: 
            print('The following organization id does not exist: ' + org)
        
if __name__ == "__main__":
    
    # download_all()
    # merge_crawled_files('/data/projects', 'projects_', '.json', 'components', './data/merged_projects.json')
    # check_github()
    # sorted_organizations = sort_organizations()
    # mine_issues(['apache', 'onap'])
    # merge_crawled_files('./data/issues', 'issues_', '.json', 'issues', './data/merged_issues.json')
