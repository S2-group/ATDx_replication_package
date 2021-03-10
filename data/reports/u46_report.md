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
|<p align="center">Project 1</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-api.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-api) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-api) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-api.json)</p>|<p align="center">Project 2</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-auth-core.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-auth-core) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-auth-core) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-auth-core.json)</p>|<p align="center">Project 3</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-commons-scheduler.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-commons-scheduler) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-commons-scheduler) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-commons-scheduler.json)</p>
 | |
|<p align="center">Project 4</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-discovery-oak.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-discovery-oak) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-discovery-oak) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-discovery-oak.json)</p>|<p align="center">Project 5</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-distribution-core.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-distribution-core) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-distribution-core) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-distribution-core.json)</p>
# ATDx project report summaries
## Project 1: _apache/sling-org-apache-sling-api_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-api.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-api) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-api) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-api.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                   |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                       |
|:-----------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:---------------------------------------------------------------------------------|
| ResourceUtil.java            |             13 |             0 |           0 |      0 |           7 |           0 |            6 | src/main/java/org/apache/sling/api/resource/ResourceUtil.java                    |
| ResourceProviderDTO.java     |             10 |             0 |           0 |      0 |          10 |           0 |            0 | src/main/java/org/apache/sling/api/resource/runtime/dto/ResourceProviderDTO.java |
| ResourceChange.java          |              8 |             0 |           0 |      0 |           4 |           0 |            4 | src/main/java/org/apache/sling/api/resource/observation/ResourceChange.java      |
| SlingConstants.java          |              7 |             0 |           0 |      0 |           4 |           0 |            3 | src/main/java/org/apache/sling/api/SlingConstants.java                           |
| ResourceMetadata.java        |              4 |             1 |           0 |      1 |           1 |           0 |            1 | src/main/java/org/apache/sling/api/resource/ResourceMetadata.java                |
| CompositeValueMap.java       |              4 |             2 |           0 |      0 |           1 |           0 |            1 | src/main/java/org/apache/sling/api/wrappers/CompositeValueMap.java               |
| ResourceProvider.java        |              4 |             0 |           0 |      0 |           2 |           0 |            2 | src/main/java/org/apache/sling/api/resource/ResourceProvider.java                |
| ResourceProviderFactory.java |              4 |             0 |           0 |      0 |           2 |           0 |            2 | src/main/java/org/apache/sling/api/resource/ResourceProviderFactory.java         |
| ResourceResolver.java        |              4 |             0 |           0 |      0 |           2 |           0 |            2 | src/main/java/org/apache/sling/api/resource/ResourceResolver.java                |
| NonExistingResource.java     |              3 |             3 |           0 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/api/resource/NonExistingResource.java             |

## Project 2: _apache/sling-org-apache-sling-auth-core_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-auth-core.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-auth-core) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-auth-core) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-auth-core.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                            | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                       |
|:--------------------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:---------------------------------------------------------------------------------|
| AbstractAuthenticationHandler.java    | 18             | 0             | 0           | 0      | 9           | 0           | 9            | src/main/java/org/apache/sling/auth/core/spi/AbstractAuthenticationHandler.java  |
| AuthenticationInfo.java               | 2              | 0             | 0           | 0      | 1           | 0           | 1            | src/main/java/org/apache/sling/engine/auth/AuthenticationInfo.java               |
| AuthenticationHandler.java            | 2              | 0             | 0           | 0      | 1           | 0           | 1            | src/main/java/org/apache/sling/engine/auth/AuthenticationHandler.java            |
| Authenticator.java                    | 2              | 0             | 0           | 0      | 1           | 0           | 1            | src/main/java/org/apache/sling/engine/auth/Authenticator.java                    |
| NoAuthenticationHandlerException.java | 2              | 0             | 0           | 0      | 1           | 0           | 1            | src/main/java/org/apache/sling/engine/auth/NoAuthenticationHandlerException.java |
| -                                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                |
| -                                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                |
| -                                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                |
| -                                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                |
| -                                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                |

## Project 3: _apache/sling-org-apache-sling-commons-scheduler_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-commons-scheduler.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-commons-scheduler) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-commons-scheduler) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-commons-scheduler.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                   | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                         |
|:-----------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:-----------------------------------------------------------------------------------|
| Scheduler.java               | 22             | 0             | 6           | 0      | 8           | 0           | 8            | src/main/java/org/apache/sling/commons/scheduler/Scheduler.java                    |
| WebConsolePrinter.java       | 9              | 0             | 0           | 0      | 9           | 0           | 0            | src/main/java/org/apache/sling/commons/scheduler/impl/WebConsolePrinter.java       |
| InternalScheduleOptions.java | 6              | 0             | 0           | 0      | 6           | 0           | 0            | src/main/java/org/apache/sling/commons/scheduler/impl/InternalScheduleOptions.java |
| QuartzScheduler.java         | 4              | 0             | 2           | 0      | 2           | 0           | 0            | src/main/java/org/apache/sling/commons/scheduler/impl/QuartzScheduler.java         |
| QuartzJobExecutor.java       | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/commons/scheduler/impl/QuartzJobExecutor.java       |
| SettingsSupport.java         | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/commons/scheduler/impl/SettingsSupport.java         |
| SchedulerServiceFactory.java | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/commons/scheduler/impl/SchedulerServiceFactory.java |
| GaugesSupport.java           | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/commons/scheduler/impl/GaugesSupport.java           |
| MetricsHelper.java           | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/commons/scheduler/impl/MetricsHelper.java           |
| -                            | -              | -             | -           | -      | -           | -           | -            | -                                                                                  |

## Project 4: _apache/sling-org-apache-sling-discovery-oak_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-discovery-oak.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-discovery-oak) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-discovery-oak) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-discovery-oak.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                 | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                      |
|:---------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:--------------------------------------------------------------------------------|
| OakDiscoveryService.java   | 4              | 0             | 2           | 0      | 1           | 0           | 1            | src/main/java/org/apache/sling/discovery/oak/OakDiscoveryService.java           |
| OakClusterViewService.java | 4              | 0             | 4           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/discovery/oak/cluster/OakClusterViewService.java |
| -                          | -              | -             | -           | -      | -           | -           | -            | -                                                                               |
| -                          | -              | -             | -           | -      | -           | -           | -            | -                                                                               |
| -                          | -              | -             | -           | -      | -           | -           | -            | -                                                                               |
| -                          | -              | -             | -           | -      | -           | -           | -            | -                                                                               |
| -                          | -              | -             | -           | -      | -           | -           | -            | -                                                                               |
| -                          | -              | -             | -           | -      | -           | -           | -            | -                                                                               |
| -                          | -              | -             | -           | -      | -           | -           | -            | -                                                                               |
| -                          | -              | -             | -           | -      | -           | -           | -            | -                                                                               |

## Project 5: _apache/sling-org-apache-sling-distribution-core_
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

