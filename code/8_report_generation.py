import csv
import json
import pandas
from collections import defaultdict
from functools import partial


def cluster_issues_per_class(json_path):

    custom_string = "project,component,inheritance,exception,vmsmell,interface,threading,complexity,sum \n"

    inheritance_rules = ['java:S1113', 'java:S1161', 'java:S1182', 
                    'java:S1185', 'java:S1210', 'java:S2062', 
                    'java:S2157', 'java:S2638', 'java:S2975']


    exception_rules = ['java:S1130', 'java:S1165', 
                    'java:S2166', 'java:S112']


    vmsmell_rules = ['java:S1210', 'java:S1217', 'java:S2157',
                 'java:S2638', 'java:S2975']


    interface_rules = ['java:S107', 'java:S1104', 'java:S1118',
                    'java:S1133', 'java:S1610']


    threading_rules = ['java:S2222', 'java:S2236', 'java:S2273',
                    'java:S2276', 'java:S2885']


    complexity_rules = ['java:S1133', 'java:S1199']

    json_issues = json.load(open(json_path))

    D = defaultdict(dict)
    for obj in json_issues:
        D[json_issues[obj]['component']] = defaultdict(int)

    for obj in json_issues:        
        D[json_issues[obj]["component"]]['project'] = json_issues[obj]['project']
        D[json_issues[obj]["component"]][json_issues[obj]['rule']] += 1
        
        D[json_issues[obj]["component"]]['inheritance'] = 0
        D[json_issues[obj]["component"]]['exception'] = 0
        D[json_issues[obj]["component"]]['threading'] = 0
        D[json_issues[obj]["component"]]['vmsmell'] = 0
        D[json_issues[obj]["component"]]['interface'] = 0
        D[json_issues[obj]["component"]]['threading'] = 0
        D[json_issues[obj]["component"]]['complexity'] = 0
        D[json_issues[obj]["component"]]['issue_sum'] = 0

    for k, v in D.items():

        for k1, v1 in v.items():
            if k1 in inheritance_rules:
            #    print(k, k1, v1)
                D[k]['inheritance'] += v1
                D[k]['issue_sum'] += v1
            #    print(D[k])
            if k1 in exception_rules:
                D[k]['exception'] += v1
                D[k]['issue_sum'] += v1
            
            if k1 in vmsmell_rules:
                D[k]['vmsmell'] += v1
                D[k]['issue_sum'] += v1
            
            if k1 in interface_rules:
                D[k]['interface'] += v1
                D[k]['issue_sum'] += v1
            
            if k1 in threading_rules:
                D[k]['threading'] += v1
                D[k]['issue_sum'] += v1

            if k1 in complexity_rules:
                D[k]['complexity'] += v1
                D[k]['issue_sum'] += v1

        custom_string = custom_string + str(D[k]['project']) + ',' + str(k).split(":",1)[1] + 
                          ',' + str(D[k]['inheritance']) + ',' + str(D[k]['exception']) + ',' +
                          str(D[k]['vmsmell']) + ',' + str(D[k]['interface']) + ',' + str(D[k]['threading']) + 
                          ',' + str(D[k]['complexity']) + ',' + str(D[k]['issue_sum']) + '\n'

    print(custom_string)

def generate_max_dimensions_per_project(csv_location):
    class_ATD_values = pandas.read_csv(csv_location)
    
    max_class_sum = class_ATD_values.sort_values('sum', ascending=False).drop_duplicates(['project'])
    max_class_sum.insert(2, 'max_type', 'total')
    print (max_class_sum[max_class_sum['sum'] == 0])

    max_class_inheritance = class_ATD_values.sort_values('inheritance', ascending=False).drop_duplicates(['project'])
    max_class_inheritance.insert(2, 'max_type', 'inheritance')
    max_class_inheritance = max_class_inheritance[max_class_inheritance.inheritance != 0]

    max_class_exception = class_ATD_values.sort_values('exception', ascending=False).drop_duplicates(['project'])
    max_class_exception.insert(2, 'max_type', 'exception')
    max_class_exception = max_class_exception[max_class_exception.exception != 0]

    max_class_vmsmell = class_ATD_values.sort_values('vmsmell', ascending=False).drop_duplicates(['project'])
    max_class_vmsmell.insert(2, 'max_type', 'vmsmell')
    max_class_vmsmell = max_class_vmsmell[max_class_vmsmell.vmsmell != 0]

    max_class_interface = class_ATD_values.sort_values('interface', ascending=False).drop_duplicates(['project'])
    max_class_interface.insert(2, 'max_type', 'interface')
    max_class_interface = max_class_interface[max_class_interface.interface != 0]

    max_class_threading = class_ATD_values.sort_values('threading', ascending=False).drop_duplicates(['project'])
    max_class_threading.insert(2, 'max_type', 'threading')
    max_class_threading = max_class_threading[max_class_threading.threading != 0]

    max_class_complexity = class_ATD_values.sort_values('complexity', ascending=False).drop_duplicates(['project'])
    max_class_complexity.insert(2, 'max_type', 'complexity')
    max_class_complexity = max_class_complexity[max_class_complexity.complexity != 0]

    max_all_dimensions = pandas.concat([max_class_sum, max_class_inheritance, max_class_exception, max_class_vmsmell, 
        max_class_interface, max_class_threading, max_class_complexity])

    max_all_dimensions['max_type'] = pandas.Categorical(max_all_dimensions['max_type'], ['total', 'inheritance', 
        'exception', 'vmsmell', 'interface', 'threading', 'complexity'])

    grouped = max_all_dimensions.groupby('project')   

    for project in grouped:

        project_df = project[1]
        project_df = project_df.drop('project', axis=1)

        f = open('./tables/{0}.md'.format(project[0]), 'w')
        f.write('### Top classes with architectural debt'+ '\n' + project_df.to_markdown(index=False) + '\n')
        f.close()


def generate_max_sums_per_project(csv_location):
    class_ATD_values = pandas.read_csv(csv_location)

    # remove classes with less than 2 violations
    class_ATD_values = class_ATD_values[class_ATD_values['sum'] > 0]  

    # reduce to max 10 classes per project (files with higher value)
    class_ATD_values = class_ATD_values.sort_values(['project', 'sum'], ascending=False).groupby('project').head(10)

    class_ATD_values['class'] = class_ATD_values['component'].str.split('/').str[-1]

    # reorder columns to prepare for the markdown export
    class_ATD_values = class_ATD_values[['class', 'sum', 'inheritance', 'exception', 'vmsmell', 'interface'
        , 'threading', 'complexity', 'component', 'project']]

    # rename columns to prepare for the markdown export
    class_ATD_values.rename(columns={'class':'Class name', 'sum':'Total issues' , 'inheritance':'Inheritance',
        'exception':'Exception', 'vmsmell':'JVMS', 'interface':'Interface', 'threading':'Threading', 
        'complexity': 'Complexity', 'component':'Fully qualified class name'}, inplace=True)

    class_ATD_values = class_ATD_values.groupby('project')

    for project in class_ATD_values:

        project_df = project[1]
        project_name = project[0]

        project_df = project_df.drop('project', axis=1)

        row_count = project_df.shape[0]

        i = 0

        while i <= 9 - row_count:
            project_df.loc[i+row_count] = '-'
            i += 1


        f = open('./data/tables/{0}.md'.format(project_name), 'w')
        f.write('### Top classes with architectural debt violations'+ '\n' + project_df.to_markdown(index=False) + '\n')
        f.close()

def generate_report():
    
    host_repo = 'https://github.com/S2-group/ATDx_reports/blob/master'
    links = pandas.read_csv('./data/project_links.csv')
    users = pandas.read_csv('./data/clean_overlapping_devs_12_months.csv')

    report_header = """# ATDx Report Summary
Our ATDx analysis targets a portfolio of software projects and identifies the pain points of each project in terms of Architectural Technical Debt (ATD). This evaluation is based on a statistical analysis of the violations of SonarCloud rules.

## ATDx in a nutshell
![ATDx in a nutshell](https://raw.githubusercontent.com/S2-group/ATDx_reports/master/plots/atdx_in_a_nutshell.jpg)

ATDx works by comparing architectural debt metrics across the projects of a software portfolio. Intuitively, it ensures that measurements across different projects are comparable, and then evaluates the severity of Architectural Technical Debt by confronting the measurements across the projects.

The ATDx approach is by itself tool-independent, and can be customized according the analysis tools available, and the portfolio considered.
In the case of this report, we used an instance of ATDx based on the static analysis tool [SonarQube](https://www.sonarqube.org/).

The instance of ATDx used to analyze your projects provides an overview of the architectural technical debt in a project in 6 distinct dimensions:
* **Inheritance**: flaws concerning inheritance mechanisms between classes, such as overrides and inheritance of methods or fields
* **Exception**: flaws regarding the management of Java exceptions and the subclassing of the “Exception” Java class.
* **JVMS**: potential misuses of the Java Virtual Machine, e.g., the incorrect usage of the specific Java class “Serializable”
* **Threading**: flaws arising from the implementation of multiple execution threads, which could potentially lead to concurrency problems
* **Interface**: flaws related to the usage of Java interfaces
* **Complexity**: flaws derived from prominent complexity measures, such as McCabe’s cyclomatic complexity

For each project, the dimensions assume a value between 0 and 5, where 0 denotes minimum architectural debt of the project in that dimension, and 5 maximum architectural debt.

In the reminder of this report, we firstly provide a set of radar charts (one for each project). Then for each project we give:
1. The same radar chart as shown at the beginning
2. A table showing the top-10 classes of the project with the highest architectural technical debt.

Note that if numerous classes with 1 violation are reported, this might point to a widespread problem (only a maximum of 10 classes are provided per project for the sake of readability). Similarly, empty rows indicate that only a few classes are affected by ATDx violations.

If you are curious about more theoretical background on ATDx, you can have a look at [this scientific publication](https://robertoverdecchia.github.io/papers/ENASE_2020.pdf).

## ATDx radar charts of your projects
"""
    user_ID = 0

    for user in users['repo']:

        blocks = []
        table = ''
        report = report_header


        # generate blocks for the project overview (a block has the image and links of a single project)
        for i, repo in enumerate(user.split(',')):
            github_url = links.loc[links['repo_name'] == repo, 'repo_url'].iloc[0]
            sonarcloud_url = links.loc[links['repo_name'] == repo, 'sonarcloud_url'].iloc[0]
            plot_url = host_repo + '/plots/' + links.loc[links['repo_name'] == repo, 'key'].iloc[0] + '.jpg'
            json_url = host_repo + '/jsons/' + links.loc[links['repo_name'] == repo, 'key'].iloc[0] + '.json'

            block = '<p align="center">Project '+ str(i+1) +'</p><img src=\"' + plot_url + '\"/> <p style="text-align:left">[Project on Github](' + github_url + ') <br> [Project on SonarCloud ](' + sonarcloud_url + ') <br> [Complete issue report (JSON)](' + json_url + ')</p>'

            blocks.append(block)

            # if 9 projects included
            if i == 8:
                break

        # create table with overview of the projects
        if len(blocks) == 2:
            table = '|||\n|-|-|\n'
            table = table + '|' + blocks[0]
            table = table + '|' + blocks[1]

        else:  
            table = '||||\n|-|-|-|\n'

            for i in range(0, len(blocks)):
                table = table + '|' + blocks[i]

                if (i+1)%3 == 0:
                    if i == 8:
                        table = table + '\n'
                        break
                    else:
                        table = table + '\n | |\n'

        report = report + table + '\n'

        report = report + '# ATDx project report summaries\n'

        # create single project overview
        for i, repo in enumerate(user.split(',')):    

            github_url = links.loc[links['repo_name'] == repo, 'repo_url'].iloc[0]
            sonarcloud_url = links.loc[links['repo_name'] == repo, 'sonarcloud_url'].iloc[0]
            plot_url = host_repo + '/plots/' + links.loc[links['repo_name'] == repo, 'key'].iloc[0] + '.jpg'
            json_url = host_repo + '/jsons/' + links.loc[links['repo_name'] == repo, 'key'].iloc[0] + '.json'
            table_path = './data/tables/' + links.loc[links['repo_name'] == repo, 'key'].iloc[0] + '.md'


            with open(table_path, 'r') as file:
                report = report + '## Project ' + str(i+1) + ': _' + repo + '_' + '\n'
                report = report + '|<img src=\"' + plot_url + '\"/>|' + '<p style="text-align:left">[Project on Github](' + github_url + ') <br> [Project on SonarCloud ](' + sonarcloud_url + ') <br> [Complete issue report (JSON)](' + json_url + ')</p>\n'
                report = report + '|-|-|\n'
                report = report + file.read() + '\n'
                print(i)

            # if 9 projects included
            if i == 8:
               break       

        filename = './data/reports/u' + str(user_ID) + '_report.md'

        with open(filename, 'w') as file:
            file.write(report)



        user_ID += 1
    

if __name__ == "__main__":
    
    #cluster_issues_per_class('./data/arch_issues.json')
    #generate_max_sums_per_project('./data/classes_dimension_issues.csv')
    #generate_report()