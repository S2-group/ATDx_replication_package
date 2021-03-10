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
||||
|-|-|-|
|<p align="center">Project 1</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-distribution-core.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-distribution-core) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-distribution-core) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-distribution-core.json)</p>|<p align="center">Project 2</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-feature-cpconverter.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-feature-cpconverter) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-feature-cpconverter) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-feature-cpconverter.json)</p>|<p align="center">Project 3</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-installer-core.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-installer-core) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-installer-core) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-installer-core.json)</p>
 | |

# ATDx project report summaries
## Project 1: _apache/sling-org-apache-sling-distribution-core_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-distribution-core.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-distribution-core) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-distribution-core) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-distribution-core.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                                   |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                                       |
|:---------------------------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:-----------------------------------------------------------------------------------------------------------------|
| ResourceQueue.java                           |             12 |             0 |          12 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/distribution/queue/impl/resource/ResourceQueue.java                               |
| ForwardDistributionAgentFactory.java         |              4 |             4 |           0 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/distribution/agent/impl/ForwardDistributionAgentFactory.java                      |
| SyncDistributionAgentFactory.java            |              4 |             4 |           0 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/distribution/agent/impl/SyncDistributionAgentFactory.java                         |
| ReverseDistributionAgentFactory.java         |              4 |             4 |           0 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/distribution/agent/impl/ReverseDistributionAgentFactory.java                      |
| QueueDistributionAgentFactory.java           |              4 |             4 |           0 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/distribution/agent/impl/QueueDistributionAgentFactory.java                        |
| SimpleDistributionAgentFactory.java          |              4 |             4 |           0 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/distribution/agent/impl/SimpleDistributionAgentFactory.java                       |
| DistributionPackageExporterServlet.java      |              3 |             0 |           3 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/distribution/servlet/DistributionPackageExporterServlet.java                      |
| RepositoryDistributionPackageImporter.java   |              3 |             0 |           3 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/distribution/packaging/impl/importer/RepositoryDistributionPackageImporter.java   |
| SimpleDistributionAgent.java                 |              2 |             0 |           0 |      0 |           2 |           0 |            0 | src/main/java/org/apache/sling/distribution/agent/impl/SimpleDistributionAgent.java                              |
| AgentDistributionPackageExporterFactory.java |              2 |             0 |           2 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/distribution/packaging/impl/exporter/AgentDistributionPackageExporterFactory.java |

## Project 2: _apache/sling-org-apache-sling-feature-cpconverter_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-feature-cpconverter.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-feature-cpconverter) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-feature-cpconverter) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-feature-cpconverter.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                                |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                         |
|:------------------------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:---------------------------------------------------------------------------------------------------|
| BaseVaultPackageScanner.java              |              3 |             0 |           3 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/feature/cpconverter/vltpkg/BaseVaultPackageScanner.java             |
| AbstractConfigurationEntryHandler.java    |              1 |             0 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/feature/cpconverter/handlers/AbstractConfigurationEntryHandler.java |
| DefaultFeaturesManager.java               |              1 |             0 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/feature/cpconverter/features/DefaultFeaturesManager.java            |
| EntryHandler.java                         |              1 |             0 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/feature/cpconverter/handlers/EntryHandler.java                      |
| DefaultAclManager.java                    |              1 |             0 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/feature/cpconverter/acl/DefaultAclManager.java                      |
| FeaturesManager.java                      |              1 |             0 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/feature/cpconverter/features/FeaturesManager.java                   |
| AbstractJcrNodeParser.java                |              1 |             0 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/feature/cpconverter/shared/AbstractJcrNodeParser.java               |
| ContentPackage2FeatureModelConverter.java |              1 |             0 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/feature/cpconverter/ContentPackage2FeatureModelConverter.java       |
| AbstractContentPackageHandler.java        |              1 |             0 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/feature/cpconverter/handlers/AbstractContentPackageHandler.java     |
| VaultPackageAssembler.java                |              1 |             0 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/feature/cpconverter/vltpkg/VaultPackageAssembler.java               |

## Project 3: _apache/sling-org-apache-sling-installer-core_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-installer-core.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-installer-core) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-installer-core) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-installer-core.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                  | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                     |
|:----------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:-------------------------------------------------------------------------------|
| OsgiInstallerImpl.java      | 5              | 0             | 0           | 0      | 5           | 0           | 0            | src/main/java/org/apache/sling/installer/core/impl/OsgiInstallerImpl.java      |
| Util.java                   | 4              | 0             | 0           | 0      | 4           | 0           | 0            | src/main/java/org/apache/sling/installer/core/impl/Util.java                   |
| InstallationContext.java    | 4              | 0             | 0           | 0      | 2           | 0           | 2            | src/main/java/org/apache/sling/installer/api/tasks/InstallationContext.java    |
| RegisteredResourceImpl.java | 2              | 0             | 1           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/installer/core/impl/RegisteredResourceImpl.java |
| Activator.java              | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/installer/core/impl/Activator.java              |
| InternalResource.java       | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/installer/core/impl/InternalResource.java       |
| FileDataStore.java          | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/installer/core/impl/FileDataStore.java          |
| BundleUtil.java             | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/installer/core/impl/tasks/BundleUtil.java       |
| -                           | -              | -             | -           | -      | -           | -           | -            | -                                                                              |
| -                           | -              | -             | -           | -      | -           | -           | -            | -                                                                              |

