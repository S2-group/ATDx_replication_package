# ATDx Report Summary
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
|||
|-|-|
|<p align="center">Project 1</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-jcr-repoinit.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-jcr-repoinit) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-jcr-repoinit) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-jcr-repoinit.json)</p>|<p align="center">Project 2</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-resourceresolver.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-resourceresolver) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-resourceresolver) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-resourceresolver.json)</p>
# ATDx project report summaries
## Project 1: _apache/sling-org-apache-sling-jcr-repoinit_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-jcr-repoinit.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-jcr-repoinit) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-jcr-repoinit) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-jcr-repoinit.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                  | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                   |
|:----------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:-----------------------------------------------------------------------------|
| AclVisitor.java             | 5              | 0             | 5           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/jcr/repoinit/impl/AclVisitor.java             |
| GroupMembershipVisitor.java | 2              | 0             | 2           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/jcr/repoinit/impl/GroupMembershipVisitor.java |
| UserVisitor.java            | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/jcr/repoinit/impl/UserVisitor.java            |
| DoNothingVisitor.java       | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/jcr/repoinit/impl/DoNothingVisitor.java       |
| AclUtil.java                | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/jcr/repoinit/impl/AclUtil.java                |
| NodePropertiesVisitor.java  | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/jcr/repoinit/impl/NodePropertiesVisitor.java  |
| UserUtil.java               | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/jcr/repoinit/impl/UserUtil.java               |
| -                           | -              | -             | -           | -      | -           | -           | -            | -                                                                            |
| -                           | -              | -             | -           | -      | -           | -           | -            | -                                                                            |
| -                           | -              | -             | -           | -      | -           | -           | -            | -                                                                            |

## Project 2: _apache/sling-org-apache-sling-resourceresolver_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-resourceresolver.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-resourceresolver) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-resourceresolver) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-resourceresolver.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                            |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                       |
|:--------------------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:-------------------------------------------------------------------------------------------------|
| URI.java                              |             57 |             1 |          54 |      1 |           1 |           0 |            0 | src/main/java/org/apache/sling/resourceresolver/impl/helper/URI.java                             |
| ResourceResolverFactoryActivator.java |              4 |             0 |           0 |      0 |           4 |           0 |            0 | src/main/java/org/apache/sling/resourceresolver/impl/ResourceResolverFactoryActivator.java       |
| MapEntries.java                       |              3 |             0 |           3 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/resourceresolver/impl/mapping/MapEntries.java                     |
| FactoryPreconditions.java             |              3 |             0 |           0 |      0 |           3 |           0 |            0 | src/main/java/org/apache/sling/resourceresolver/impl/FactoryPreconditions.java                   |
| ResourceChangeListenerInfo.java       |              2 |             1 |           0 |      1 |           0 |           0 |            0 | src/main/java/org/apache/sling/resourceresolver/impl/observation/ResourceChangeListenerInfo.java |
| ResourceProviderHandler.java          |              2 |             1 |           0 |      1 |           0 |           0 |            0 | src/main/java/org/apache/sling/resourceresolver/impl/providers/ResourceProviderHandler.java      |
| MapEntry.java                         |              2 |             1 |           0 |      1 |           0 |           0 |            0 | src/main/java/org/apache/sling/resourceresolver/impl/mapping/MapEntry.java                       |
| ResourceResolverImpl.java             |              2 |             0 |           2 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/resourceresolver/impl/ResourceResolverImpl.java                   |
| URIException.java                     |              2 |             0 |           2 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/resourceresolver/impl/helper/URIException.java                    |
| MapConfigurationProvider.java         |              2 |             1 |           0 |      1 |           0 |           0 |            0 | src/main/java/org/apache/sling/resourceresolver/impl/mapping/MapConfigurationProvider.java       |

