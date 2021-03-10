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
|<p align="center">Project 1</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_aai-data-router.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/aai-data-router) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_aai-data-router) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_aai-data-router.json)</p>|<p align="center">Project 2</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_aai-search-data-service.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/aai-search-data-service) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_aai-search-data-service) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_aai-search-data-service.json)</p>|<p align="center">Project 3</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_aai-sparky-be.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/aai-sparky-be) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_aai-sparky-be) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_aai-sparky-be.json)</p>
 | |
|<p align="center">Project 4</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_aai-spike.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/aai-spike) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_aai-spike) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_aai-spike.json)</p>
# ATDx project report summaries
## Project 1: _onap/aai-data-router_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_aai-data-router.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/aai-data-router) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_aai-data-router) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_aai-data-router.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                             |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                          |
|:---------------------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:------------------------------------------------------------------------------------|
| AbstractSpikeEntityEventProcessor.java |              6 |             0 |           5 |      0 |           1 |           0 |            0 | src/main/java/org/onap/aai/datarouter/policy/AbstractSpikeEntityEventProcessor.java |
| AaiUiSvcPolicyUtil.java                |              5 |             0 |           4 |      0 |           1 |           0 |            0 | src/main/java/org/onap/aai/datarouter/util/AaiUiSvcPolicyUtil.java                  |
| POAAuditException.java                 |              3 |             0 |           3 |      0 |           0 |           0 |            0 | src/main/java/org/onap/aai/datarouter/exception/POAAuditException.java              |
| SearchServiceAgent.java                |              3 |             0 |           3 |      0 |           0 |           0 |            0 | src/main/java/org/onap/aai/datarouter/util/SearchServiceAgent.java                  |
| ChameleonErrorProcessor.java           |              2 |             0 |           2 |      0 |           0 |           0 |            0 | src/main/java/org/onap/aai/datarouter/query/ChameleonErrorProcessor.java            |
| GapEventTransformer.java               |              2 |             0 |           2 |      0 |           0 |           0 |            0 | src/main/java/org/onap/aai/datarouter/policy/GapEventTransformer.java               |
| EntityEventPolicy.java                 |              2 |             0 |           2 |      0 |           0 |           0 |            0 | src/main/java/org/onap/aai/datarouter/policy/EntityEventPolicy.java                 |
| SpikeEntityEventPolicy.java            |              2 |             0 |           2 |      0 |           0 |           0 |            0 | src/main/java/org/onap/aai/datarouter/policy/SpikeEntityEventPolicy.java            |
| AuditService.java                      |              2 |             0 |           2 |      0 |           0 |           0 |            0 | src/main/java/org/onap/aai/datarouter/service/AuditService.java                     |
| AaiEventEntity.java                    |              1 |             0 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/onap/aai/datarouter/entity/AaiEventEntity.java                    |

## Project 2: _onap/aai-search-data-service_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_aai-search-data-service.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/aai-search-data-service) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_aai-search-data-service) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_aai-search-data-service.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name       | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                             |
|:-----------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:-----------------------------------------------------------------------|
| Application.java | 1              | 0             | 1           | 0      | 0           | 0           | 0            | search-data-service-app/src/main/java/org/onap/aai/sa/Application.java |
| -                | -              | -             | -           | -      | -           | -           | -            | -                                                                      |
| -                | -              | -             | -           | -      | -           | -           | -            | -                                                                      |
| -                | -              | -             | -           | -      | -           | -           | -            | -                                                                      |
| -                | -              | -             | -           | -      | -           | -           | -            | -                                                                      |
| -                | -              | -             | -           | -      | -           | -           | -            | -                                                                      |
| -                | -              | -             | -           | -      | -           | -           | -            | -                                                                      |
| -                | -              | -             | -           | -      | -           | -           | -            | -                                                                      |
| -                | -              | -             | -           | -      | -           | -           | -            | -                                                                      |
| -                | -              | -             | -           | -      | -           | -           | -            | -                                                                      |

## Project 3: _onap/aai-sparky-be_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_aai-sparky-be.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/aai-sparky-be) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_aai-sparky-be) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_aai-sparky-be.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                         |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                                        |
|:-----------------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:------------------------------------------------------------------------------------------------------------------|
| SparkyConstants.java               |             24 |             0 |           0 |      0 |          24 |           0 |            0 | sparkybe-onap-service/src/main/java/org/onap/aai/sparky/viewandinspect/config/SparkyConstants.java                |
| BaseGizmoVisualizationContext.java |             12 |             0 |           1 |      0 |           0 |           0 |           11 | sparkybe-onap-service/src/main/java/org/onap/aai/sparky/viewandinspect/context/BaseGizmoVisualizationContext.java |
| GizmoAdapter.java                  |             10 |             0 |           8 |      0 |           0 |           0 |            2 | sparkybe-onap-service/src/main/java/org/onap/aai/sparky/dal/GizmoAdapter.java                                     |
| BaseVisualizationContext.java      |              9 |             0 |           1 |      0 |           0 |           0 |            8 | sparkybe-onap-service/src/main/java/org/onap/aai/sparky/viewandinspect/context/BaseVisualizationContext.java      |
| ActiveInventoryAdapter.java        |              7 |             0 |           5 |      0 |           0 |           0 |            2 | sparkybe-onap-service/src/main/java/org/onap/aai/sparky/dal/ActiveInventoryAdapter.java                           |
| RestOperationalStatistics.java     |              5 |             0 |           0 |      0 |           0 |           0 |            5 | sparkybe-onap-service/src/main/java/org/onap/aai/sparky/dal/rest/RestOperationalStatistics.java                   |
| EncryptConvertor.java              |              4 |             0 |           3 |      0 |           1 |           0 |            0 | sparkybe-onap-service/src/main/java/org/onap/aai/sparky/util/EncryptConvertor.java                                |
| SyncControllerImpl.java            |              4 |             0 |           2 |      0 |           0 |           0 |            2 | sparkybe-onap-service/src/main/java/org/onap/aai/sparky/sync/SyncControllerImpl.java                              |
| RestClientFactory.java             |              4 |             0 |           0 |      0 |           1 |           0 |            3 | sparkybe-onap-service/src/main/java/org/onap/aai/sparky/dal/rest/RestClientFactory.java                           |
| PortalRestAPIServiceImpl.java      |              3 |             0 |           1 |      0 |           1 |           0 |            1 | sparkybe-onap-service/src/main/java/org/onap/aai/sparky/security/portal/PortalRestAPIServiceImpl.java             |

## Project 4: _onap/aai-spike_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_aai-spike.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/aai-spike) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_aai-spike) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_aai-spike.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                 | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                         |
|:---------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:-------------------------------------------------------------------|
| RelationshipSchema.java    | 2              | 0             | 2           | 0      | 0           | 0           | 0            | src/main/java/org/onap/aai/spike/schema/RelationshipSchema.java    |
| OXMModelLoader.java        | 2              | 0             | 1           | 0      | 1           | 0           | 0            | src/main/java/org/onap/aai/spike/schema/OXMModelLoader.java        |
| EdgeRulesLoader.java       | 2              | 0             | 1           | 0      | 1           | 0           | 0            | src/main/java/org/onap/aai/spike/schema/EdgeRulesLoader.java       |
| SpikeConstants.java        | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/onap/aai/spike/util/SpikeConstants.java          |
| SpikeProperties.java       | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/onap/aai/spike/util/SpikeProperties.java         |
| GraphEventTransformer.java | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/onap/aai/spike/schema/GraphEventTransformer.java |
| SpikeService.java          | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/onap/aai/spike/service/SpikeService.java         |
| OffsetManager.java         | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/onap/aai/spike/event/incoming/OffsetManager.java |
| -                          | -              | -             | -           | -      | -           | -           | -            | -                                                                  |
| -                          | -              | -             | -           | -      | -           | -           | -            | -                                                                  |

