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
|<p align="center">Project 1</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_aai-aai-common.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/aai-aai-common) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_aai-aai-common) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_aai-aai-common.json)</p>|<p align="center">Project 2</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_aai-data-router.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/aai-data-router) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_aai-data-router) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_aai-data-router.json)</p>|<p align="center">Project 3</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_aai-graphadmin.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/aai-graphadmin) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_aai-graphadmin) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_aai-graphadmin.json)</p>
 | |
|<p align="center">Project 4</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_aai-resources.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/aai-resources) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_aai-resources) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_aai-resources.json)</p>|<p align="center">Project 5</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_aai-router-core.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/aai-router-core) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_aai-router-core) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_aai-router-core.json)</p>|<p align="center">Project 6</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_sdc.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/sdc) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_sdc) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_sdc.json)</p>
 | |

# ATDx project report summaries
## Project 1: _onap/aai-aai-common_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_aai-aai-common.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/aai-aai-common) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_aai-aai-common) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_aai-aai-common.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name              |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                             |
|:------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:---------------------------------------------------------------------------------------|
| HttpEntry.java          |             22 |             0 |          19 |      0 |           3 |           0 |            0 | aai-core/src/main/java/org/onap/aai/rest/db/HttpEntry.java                             |
| PojoUtils.java          |              9 |             0 |           9 |      0 |           0 |           0 |            0 | aai-core/src/main/java/org/onap/aai/util/PojoUtils.java                                |
| Auth.java               |              7 |             0 |           7 |      0 |           0 |           0 |            0 | aai-auth/src/main/java/org/onap/aaiauth/auth/Auth.java                                 |
| ErrorLogHelper.java     |              6 |             0 |           3 |      0 |           2 |           0 |            1 | aai-els-onap-logging/src/main/java/org/onap/aai/logging/ErrorLogHelper.java            |
| DBSerializer.java       |              6 |             0 |           5 |      0 |           1 |           0 |            0 | aai-core/src/main/java/org/onap/aai/serialization/db/DBSerializer.java                 |
| RestClient.java         |              5 |             0 |           5 |      0 |           0 |           0 |            0 | aai-rest/src/main/java/org/onap/aai/restclient/RestClient.java                         |
| AAIException.java       |              5 |             0 |           5 |      0 |           0 |           0 |            0 | aai-els-onap-logging/src/main/java/org/onap/aai/exceptions/AAIException.java           |
| OxmModelLoader.java     |              5 |             0 |           4 |      0 |           1 |           0 |            0 | aai-utils/src/main/java/org/onap/aaiutils/oxm/OxmModelLoader.java                      |
| RelationshipSchema.java |              4 |             0 |           4 |      0 |           0 |           0 |            0 | aai-schema-abstraction/src/main/java/org/onap/aai/schemaif/oxm/RelationshipSchema.java |
| Constants.java          |              4 |             0 |           0 |      0 |           4 |           0 |            0 | aai-els-onap-logging/src/main/java/org/onap/logging/filter/base/Constants.java         |

## Project 2: _onap/aai-data-router_
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

## Project 3: _onap/aai-graphadmin_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_aai-graphadmin.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/aai-graphadmin) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_aai-graphadmin) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_aai-graphadmin.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                             |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                     |
|:---------------------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:-------------------------------------------------------------------------------|
| PartialPropAndEdgeLoader.java          |             12 |             0 |          11 |      0 |           1 |           0 |            0 | src/main/java/org/onap/aai/datasnapshot/PartialPropAndEdgeLoader.java          |
| PartialPropAndEdgeLoader4HistInit.java |             12 |             0 |          11 |      0 |           1 |           0 |            0 | src/main/java/org/onap/aai/datasnapshot/PartialPropAndEdgeLoader4HistInit.java |
| DataSnapshot.java                      |             10 |             0 |          10 |      0 |           0 |           0 |            0 | src/main/java/org/onap/aai/datasnapshot/DataSnapshot.java                      |
| DataSnapshot4HistInit.java             |             10 |             0 |          10 |      0 |           0 |           0 |            0 | src/main/java/org/onap/aai/datasnapshot/DataSnapshot4HistInit.java             |
| DataGrooming.java                      |              6 |             0 |           2 |      0 |           4 |           0 |            0 | src/main/java/org/onap/aai/datagrooming/DataGrooming.java                      |
| DupeTool.java                          |              5 |             0 |           1 |      0 |           4 |           0 |            0 | src/main/java/org/onap/aai/dbgen/DupeTool.java                                 |
| UpdatePropertyTool.java                |              4 |             0 |           0 |      0 |           4 |           0 |            0 | src/main/java/org/onap/aai/dbgen/UpdatePropertyTool.java                       |
| PartialVertexLoader.java               |              4 |             0 |           4 |      0 |           0 |           0 |            0 | src/main/java/org/onap/aai/datasnapshot/PartialVertexLoader.java               |
| MigrateINVPhysicalInventory.java       |              4 |             0 |           4 |      0 |           0 |           0 |            0 | src/main/java/org/onap/aai/migration/v12/MigrateINVPhysicalInventory.java      |
| DataGroomingTasks.java                 |              3 |             0 |           2 |      0 |           0 |           1 |            0 | src/main/java/org/onap/aai/datagrooming/DataGroomingTasks.java                 |

## Project 4: _onap/aai-resources_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_aai-resources.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/aai-resources) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_aai-resources) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_aai-resources.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                    |
|:--------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:------------------------------------------------------------------------------|
| DataImportTasks.java      | 4              | 0             | 3           | 0      | 0           | 1           | 0            | aai-resources/src/main/java/org/onap/aai/TenantIsolation/DataImportTasks.java |
| BulkConsumer.java         | 3              | 0             | 3           | 0      | 0           | 0           | 0            | aai-resources/src/main/java/org/onap/aai/rest/BulkConsumer.java               |
| IncreaseNodesTool.java    | 3              | 0             | 2           | 0      | 1           | 0           | 0            | aai-resources/src/main/java/org/onap/aai/IncreaseNodesTool.java               |
| LegacyMoxyConsumer.java   | 2              | 0             | 0           | 0      | 2           | 0           | 0            | aai-resources/src/main/java/org/onap/aai/rest/LegacyMoxyConsumer.java         |
| AuthorizationService.java | 2              | 0             | 2           | 0      | 0           | 0           | 0            | aai-resources/src/main/java/org/onap/aai/service/AuthorizationService.java    |
| LogFormatTools.java       | 1              | 0             | 0           | 0      | 1           | 0           | 0            | aai-resources/src/main/java/org/onap/aai/rest/util/LogFormatTools.java        |
| Command.java              | 1              | 0             | 1           | 0      | 0           | 0           | 0            | aai-resources/src/main/java/org/onap/aai/dbgen/tags/Command.java              |
| PositiveNumValidator.java | 1              | 0             | 1           | 0      | 0           | 0           | 0            | aai-resources/src/main/java/org/onap/aai/util/PositiveNumValidator.java       |
| ResourcesApp.java         | 1              | 0             | 1           | 0      | 0           | 0           | 0            | aai-resources/src/main/java/org/onap/aai/ResourcesApp.java                    |
| -                         | -              | -             | -           | -      | -           | -           | -            | -                                                                             |

## Project 5: _onap/aai-router-core_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_aai-router-core.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/aai-router-core) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_aai-router-core) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_aai-router-core.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                        | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                          |
|:----------------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:--------------------------------------------------------------------|
| SchemaIngestPropertiesReader.java | 2              | 0             | 2           | 0      | 0           | 0           | 0            | src/main/java/org/onap/aai/schema/SchemaIngestPropertiesReader.java |
| RestClientEndpoint.java           | 1              | 1             | 0           | 0      | 0           | 0           | 0            | src/main/java/org/onap/aai/rest/RestClientEndpoint.java             |
| AbstractEventBusEndpoint.java     | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/onap/aai/event/AbstractEventBusEndpoint.java      |
| -                                 | -              | -             | -           | -      | -           | -           | -            | -                                                                   |
| -                                 | -              | -             | -           | -      | -           | -           | -            | -                                                                   |
| -                                 | -              | -             | -           | -      | -           | -           | -            | -                                                                   |
| -                                 | -              | -             | -           | -      | -           | -           | -            | -                                                                   |
| -                                 | -              | -             | -           | -      | -           | -           | -            | -                                                                   |
| -                                 | -              | -             | -           | -      | -           | -           | -            | -                                                                   |
| -                                 | -              | -             | -           | -      | -           | -           | -            | -                                                                   |

## Project 6: _onap/sdc_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_sdc.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/sdc) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_sdc) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_sdc.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                         |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                                |
|:-----------------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:----------------------------------------------------------------------------------------------------------|
| Logger.java                        |             42 |             0 |           0 |      0 |          21 |           0 |           21 | common-app-logging/src/main/java/org/openecomp/sdc/common/log/wrappers/Logger.java                        |
| ArtifactsBusinessLogic.java        |             31 |             0 |           0 |      0 |          31 |           0 |            0 | catalog-be/src/main/java/org/openecomp/sdc/be/components/impl/ArtifactsBusinessLogic.java                 |
| ResourceBusinessLogic.java         |             22 |             3 |           0 |      0 |          19 |           0 |            0 | catalog-be/src/main/java/org/openecomp/sdc/be/components/impl/ResourceBusinessLogic.java                  |
| DistributionNotificationEvent.java |             11 |            10 |           0 |      0 |           1 |           0 |            0 | catalog-dao/src/main/java/org/openecomp/sdc/be/resources/data/auditing/DistributionNotificationEvent.java |
| ResourceAdminEvent.java            |             11 |            10 |           0 |      0 |           1 |           0 |            0 | catalog-dao/src/main/java/org/openecomp/sdc/be/resources/data/auditing/ResourceAdminEvent.java            |
| CategoryEvent.java                 |             10 |            10 |           0 |      0 |           0 |           0 |            0 | catalog-dao/src/main/java/org/openecomp/sdc/be/resources/data/auditing/CategoryEvent.java                 |
| CompositionBusinessLogic.java      |             10 |             0 |           0 |      0 |           0 |           0 |           10 | catalog-be/src/main/java/org/openecomp/sdc/be/components/impl/CompositionBusinessLogic.java               |
| AuditingGetUebClusterEvent.java    |             10 |            10 |           0 |      0 |           0 |           0 |            0 | catalog-dao/src/main/java/org/openecomp/sdc/be/resources/data/auditing/AuditingGetUebClusterEvent.java    |
| UserAdminEvent.java                |             10 |            10 |           0 |      0 |           0 |           0 |            0 | catalog-dao/src/main/java/org/openecomp/sdc/be/resources/data/auditing/UserAdminEvent.java                |
| DistributionStatusEvent.java       |             10 |            10 |           0 |      0 |           0 |           0 |            0 | catalog-dao/src/main/java/org/openecomp/sdc/be/resources/data/auditing/DistributionStatusEvent.java       |

