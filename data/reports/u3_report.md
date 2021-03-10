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
|<p align="center">Project 1</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_aaf-authz.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/aaf-authz) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_aaf-authz) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_aaf-authz.json)</p>|<p align="center">Project 2</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_aai-aai-common.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/aai-aai-common) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_aai-aai-common) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_aai-aai-common.json)</p>|<p align="center">Project 3</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_aai-esr-server.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/aai-esr-server) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_aai-esr-server) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_aai-esr-server.json)</p>
 | |
|<p align="center">Project 4</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_aai-event-client.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/aai-event-client) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_aai-event-client) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_aai-event-client.json)</p>|<p align="center">Project 5</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_aai-sparky-be.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/aai-sparky-be) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_aai-sparky-be) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_aai-sparky-be.json)</p>|<p align="center">Project 6</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_appc.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/appc) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_appc) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_appc.json)</p>
 | |
|<p align="center">Project 7</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_ccsdk-apps.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/ccsdk-apps) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_ccsdk-apps) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_ccsdk-apps.json)</p>|<p align="center">Project 8</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_ccsdk-dashboard.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/ccsdk-dashboard) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_ccsdk-dashboard) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_ccsdk-dashboard.json)</p>|<p align="center">Project 9</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_ccsdk-features.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/ccsdk-features) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_ccsdk-features) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_ccsdk-features.json)</p>

# ATDx project report summaries
## Project 1: _onap/aaf-authz_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_aaf-authz.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/aaf-authz) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_aaf-authz) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_aaf-authz.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name         |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                 |
|:-------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:---------------------------------------------------------------------------|
| LocateDAO.java     |             13 |             0 |           2 |      0 |          11 |           0 |            0 | auth/auth-cass/src/main/java/org/onap/aaf/auth/dao/cass/LocateDAO.java     |
| OAuthTokenDAO.java |             12 |             0 |           0 |      0 |          12 |           0 |            0 | auth/auth-cass/src/main/java/org/onap/aaf/auth/dao/cass/OAuthTokenDAO.java |
| ArtiDAO.java       |             11 |             0 |           0 |      0 |          11 |           0 |            0 | auth/auth-cass/src/main/java/org/onap/aaf/auth/dao/cass/ArtiDAO.java       |
| Agent.java         |              9 |             0 |           9 |      0 |           0 |           0 |            0 | cadi/aaf/src/main/java/org/onap/aaf/cadi/configure/Agent.java              |
| InXML.java         |              9 |             0 |           1 |      0 |           8 |           0 |            0 | misc/rosetta/src/main/java/org/onap/aaf/misc/rosetta/InXML.java            |
| Symm.java          |              8 |             0 |           2 |      0 |           3 |           0 |            3 | cadi/core/src/main/java/org/onap/aaf/cadi/Symm.java                        |
| Cred.java          |              8 |             0 |           0 |      0 |           8 |           0 |            0 | auth/auth-batch/src/main/java/org/onap/aaf/auth/batch/helpers/Cred.java    |
| FutureDAO.java     |              8 |             0 |           0 |      0 |           8 |           0 |            0 | auth/auth-cass/src/main/java/org/onap/aaf/auth/dao/cass/FutureDAO.java     |
| HistoryDAO.java    |              8 |             0 |           0 |      0 |           8 |           0 |            0 | auth/auth-cass/src/main/java/org/onap/aaf/auth/dao/cass/HistoryDAO.java    |
| CredDAO.java       |              8 |             0 |           0 |      0 |           8 |           0 |            0 | auth/auth-cass/src/main/java/org/onap/aaf/auth/dao/cass/CredDAO.java       |

## Project 2: _onap/aai-aai-common_
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

## Project 3: _onap/aai-esr-server_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_aai-esr-server.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/aai-esr-server) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_aai-esr-server) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_aai-esr-server.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                           |
|:--------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:-------------------------------------------------------------------------------------|
| RelationshipProvider.java | 1              | 0             | 1           | 0      | 0           | 0           | 0            | esr-mgr/src/main/java/org/onap/aai/esr/externalservice/aai/RelationshipProvider.java |
| EmsRegisterProvider.java  | 1              | 0             | 1           | 0      | 0           | 0           | 0            | esr-mgr/src/main/java/org/onap/aai/esr/externalservice/aai/EmsRegisterProvider.java  |
| VnfmRegisterProvider.java | 1              | 0             | 1           | 0      | 0           | 0           | 0            | esr-mgr/src/main/java/org/onap/aai/esr/externalservice/aai/VnfmRegisterProvider.java |
| PnfRegisterProvider.java  | 1              | 0             | 1           | 0      | 0           | 0           | 0            | esr-mgr/src/main/java/org/onap/aai/esr/externalservice/aai/PnfRegisterProvider.java  |
| VimRegisterProvider.java  | 1              | 0             | 1           | 0      | 0           | 0           | 0            | esr-mgr/src/main/java/org/onap/aai/esr/externalservice/aai/VimRegisterProvider.java  |
| NfvoRegisterProvider.java | 1              | 0             | 1           | 0      | 0           | 0           | 0            | esr-mgr/src/main/java/org/onap/aai/esr/externalservice/aai/NfvoRegisterProvider.java |
| -                         | -              | -             | -           | -      | -           | -           | -            | -                                                                                    |
| -                         | -              | -             | -           | -      | -           | -           | -            | -                                                                                    |
| -                         | -              | -             | -           | -      | -           | -           | -            | -                                                                                    |
| -                         | -              | -             | -           | -      | -           | -           | -            | -                                                                                    |

## Project 4: _onap/aai-event-client_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_aai-event-client.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/aai-event-client) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_aai-event-client) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_aai-event-client.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                 | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                               |
|:---------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:-----------------------------------------------------------------------------------------|
| EventPublisher.java        | 9              | 0             | 9           | 0      | 0           | 0           | 0            | event-client-api/src/main/java/org/onap/aai/event/api/EventPublisher.java                |
| EventConsumer.java         | 6              | 0             | 6           | 0      | 0           | 0           | 0            | event-client-api/src/main/java/org/onap/aai/event/api/EventConsumer.java                 |
| DMaaPEventPublisher.java   | 3              | 0             | 1           | 0      | 2           | 0           | 0            | event-client-dmaap/src/main/java/org/onap/aai/event/client/DMaaPEventPublisher.java      |
| DMaaPEventConsumer.java    | 3              | 0             | 0           | 0      | 3           | 0           | 0            | event-client-dmaap/src/main/java/org/onap/aai/event/client/DMaaPEventConsumer.java       |
| RabbitMqUtils.java         | 2              | 0             | 1           | 0      | 1           | 0           | 0            | event-client-rabbitmq/src/main/java/org/onap/aai/event/client/RabbitMqUtils.java         |
| RabbitMqEventConsumer.java | 1              | 1             | 0           | 0      | 0           | 0           | 0            | event-client-rabbitmq/src/main/java/org/onap/aai/event/client/RabbitMqEventConsumer.java |
| -                          | -              | -             | -           | -      | -           | -           | -            | -                                                                                        |
| -                          | -              | -             | -           | -      | -           | -           | -            | -                                                                                        |
| -                          | -              | -             | -           | -      | -           | -           | -            | -                                                                                        |
| -                          | -              | -             | -           | -      | -           | -           | -            | -                                                                                        |

## Project 5: _onap/aai-sparky-be_
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

## Project 6: _onap/appc_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_appc.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/appc) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_appc) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_appc.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                  |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                                                         |
|:----------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:-----------------------------------------------------------------------------------------------------------------------------------|
| DGGeneralDBService.java     |             25 |             0 |          25 |      0 |           0 |           0 |            0 | appc-config/appc-data-services/provider/src/main/java/org/onap/appc/data/services/db/DGGeneralDBService.java                       |
| DesignDBService.java        |             19 |             0 |          19 |      0 |           0 |           0 |            0 | appc-inbound/appc-design-services/provider/src/main/java/org/onap/appc/design/dbervices/DesignDBService.java                       |
| RequestValidator.java       |             11 |             0 |          10 |      0 |           1 |           0 |            0 | appc-inbound/appc-interfaces-service/bundle/src/main/java/org/onap/appc/interfaces/service/executor/RequestValidator.java          |
| ConfigComponentAdaptor.java |              8 |             0 |           6 |      0 |           2 |           0 |            0 | appc-config/appc-config-adaptor/provider/src/main/java/org/onap/appc/ccadaptor/ConfigComponentAdaptor.java                         |
| FlowSequenceGenerator.java  |              7 |             0 |           7 |      0 |           0 |           0 |            0 | appc-config/appc-flow-controller/provider/src/main/java/org/onap/appc/flow/controller/node/FlowSequenceGenerator.java              |
| RequestFailedException.java |              7 |             0 |           7 |      0 |           0 |           0 |            0 | appc-adapters/appc-iaas-adapter/appc-iaas-adapter-bundle/src/main/java/org/onap/appc/adapter/iaas/impl/RequestFailedException.java |
| UnmodifiableProperties.java |              6 |             2 |           1 |      1 |           1 |           0 |            1 | appc-core/appc-common-bundle/src/main/java/org/onap/appc/util/UnmodifiableProperties.java                                          |
| ArtificatTransformer.java   |              6 |             0 |           6 |      0 |           0 |           0 |            0 | appc-config/appc-config-params/provider/src/main/java/org/onap/sdnc/config/params/transformer/ArtificatTransformer.java            |
| ParseAdminArtifcat.java     |              6 |             0 |           6 |      0 |           0 |           0 |            0 | appc-config/appc-encryption-tool/provider/src/main/java/org/onap/appc/encryptiontool/fqdn/ParseAdminArtifcat.java                  |
| RequestFailedException.java |              5 |             0 |           5 |      0 |           0 |           0 |            0 | appc-adapters/appc-rest-adapter/appc-rest-adapter-bundle/src/main/java/org/onap/appc/adapter/rest/impl/RequestFailedException.java |

## Project 7: _onap/ccsdk-apps_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_ccsdk-apps.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/ccsdk-apps) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_ccsdk-apps) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_ccsdk-apps.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                   |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                         |
|:-----------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:---------------------------------------------------------------------------------------------------|
| SpringService.java           |              5 |             0 |           5 |      0 |           0 |           0 |            0 | ms/neng/src/main/java/org/onap/ccsdk/apps/ms/neng/core/service/SpringService.java                  |
| PolicyFinderServiceImpl.java |              5 |             0 |           5 |      0 |           0 |           0 |            0 | ms/neng/src/main/java/org/onap/ccsdk/apps/ms/neng/service/extinf/impl/PolicyFinderServiceImpl.java |
| PropertyOperator.java        |              5 |             0 |           5 |      0 |           0 |           0 |            0 | ms/neng/src/main/java/org/onap/ccsdk/apps/ms/neng/core/policy/PropertyOperator.java                |
| SpringServiceImpl.java       |              5 |             0 |           5 |      0 |           0 |           0 |            0 | ms/neng/src/main/java/org/onap/ccsdk/apps/ms/neng/core/service/SpringServiceImpl.java              |
| VlantagApiService.java       |              4 |             0 |           4 |      0 |           0 |           0 |            0 | ms/vlantag-api/src/main/java/org/onap/ccsdk/apps/ms/vlantagapi/core/service/VlantagApiService.java |
| PolicyParameters.java        |              3 |             0 |           3 |      0 |           0 |           0 |            0 | ms/neng/src/main/java/org/onap/ccsdk/apps/ms/neng/core/policy/PolicyParameters.java                |
| RestService.java             |              2 |             0 |           2 |      0 |           0 |           0 |            0 | ms/neng/src/main/java/org/onap/ccsdk/apps/ms/neng/core/service/rs/RestService.java                 |
| SequenceGenerator.java       |              2 |             0 |           2 |      0 |           0 |           0 |            0 | ms/neng/src/main/java/org/onap/ccsdk/apps/ms/neng/core/seq/SequenceGenerator.java                  |
| DbNameValidator.java         |              2 |             0 |           2 |      0 |           0 |           0 |            0 | ms/neng/src/main/java/org/onap/ccsdk/apps/ms/neng/core/validator/DbNameValidator.java              |
| AaiServiceImpl.java          |              1 |             0 |           1 |      0 |           0 |           0 |            0 | ms/neng/src/main/java/org/onap/ccsdk/apps/ms/neng/service/extinf/impl/AaiServiceImpl.java          |

## Project 8: _onap/ccsdk-dashboard_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_ccsdk-dashboard.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/ccsdk-dashboard) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_ccsdk-dashboard) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_ccsdk-dashboard.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                         |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                            |
|:-----------------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:------------------------------------------------------------------------------------------------------|
| CommonApiController.java           |             22 |             0 |          22 |      0 |           0 |           0 |            0 | ccsdk-app-common/src/main/java/org/onap/ccsdk/dashboard/controller/CommonApiController.java           |
| CloudifyController.java            |             19 |             0 |          19 |      0 |           0 |           0 |            0 | ccsdk-app-common/src/main/java/org/onap/ccsdk/dashboard/controller/CloudifyController.java            |
| ServiceTypeRequest.java            |             13 |             0 |           0 |      0 |          13 |           0 |            0 | ccsdk-app-common/src/main/java/org/onap/ccsdk/dashboard/model/inventory/ServiceTypeRequest.java       |
| ConsulController.java              |             11 |             0 |          11 |      0 |           0 |           0 |            0 | ccsdk-app-common/src/main/java/org/onap/ccsdk/dashboard/controller/ConsulController.java              |
| InventoryController.java           |             10 |             0 |          10 |      0 |           0 |           0 |            0 | ccsdk-app-common/src/main/java/org/onap/ccsdk/dashboard/controller/InventoryController.java           |
| ServiceComponent.java              |              9 |             0 |           0 |      0 |           9 |           0 |            0 | ccsdk-app-common/src/main/java/org/onap/ccsdk/dashboard/model/inventory/ServiceComponent.java         |
| Link.java                          |              8 |             0 |           0 |      0 |           8 |           0 |            0 | ccsdk-app-common/src/main/java/org/onap/ccsdk/dashboard/model/inventory/Link.java                     |
| CloudifyExecutionRequest.java      |              6 |             0 |           0 |      0 |           6 |           0 |            0 | ccsdk-app-common/src/main/java/org/onap/ccsdk/dashboard/model/CloudifyExecutionRequest.java           |
| ServiceTypeUploadRequest.java      |              6 |             0 |           0 |      0 |           6 |           0 |            0 | ccsdk-app-common/src/main/java/org/onap/ccsdk/dashboard/model/inventory/ServiceTypeUploadRequest.java |
| ControllerEndpointCredentials.java |              6 |             0 |           2 |      0 |           4 |           0 |            0 | ccsdk-app-common/src/main/java/org/onap/ccsdk/dashboard/model/ControllerEndpointCredentials.java      |

## Project 9: _onap/ccsdk-features_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_ccsdk-features.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/ccsdk-features) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_ccsdk-features) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_ccsdk-features.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name          |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                                               |
|:--------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:-------------------------------------------------------------------------------------------------------------------------|
| Program.java        |             12 |             0 |          12 |      0 |           0 |           0 |            0 | sdnr/wt/data-provider/setup/src/main/java/org/onap/ccsdk/features/sdnr/wt/dataprovider/setup/Program.java                |
| MessageDaoImpl.java |              8 |             0 |           8 |      0 |           0 |           0 |            0 | lib/doorman/src/main/java/org/onap/ccsdk/features/lib/doorman/dao/MessageDaoImpl.java                                    |
| MyOdluxBundle.java  |              8 |             8 |           0 |      0 |           0 |           0 |            0 | sdnr/wt/odlux/apps/maintenanceApp/src2/main/java/org/onap/ccsdk/features/sdnr/wt/odlux/bundles/MyOdluxBundle.java        |
| MyOdluxBundle.java  |              8 |             8 |           0 |      0 |           0 |           0 |            0 | sdnr/wt/odlux/apps/apiDemo/src2/main/java/org/onap/ccsdk/features/sdnr/wt/odlux/bundles/MyOdluxBundle.java               |
| MyOdluxBundle.java  |              8 |             8 |           0 |      0 |           0 |           0 |            0 | sdnr/wt/odlux/apps/mediatorApp/src2/main/java/org/onap/ccsdk/features/sdnr/wt/odlux/bundles/MyOdluxBundle.java           |
| MyOdluxBundle.java  |              8 |             8 |           0 |      0 |           0 |           0 |            0 | sdnr/wt/odlux/apps/performanceHistoryApp/src2/main/java/org/onap/ccsdk/features/sdnr/wt/odlux/bundles/MyOdluxBundle.java |
| MyOdluxBundle.java  |              8 |             8 |           0 |      0 |           0 |           0 |            0 | sdnr/wt/odlux/apps/configurationApp/src2/main/java/org/onap/ccsdk/features/sdnr/wt/odlux/bundles/MyOdluxBundle.java      |
| MyOdluxBundle.java  |              8 |             8 |           0 |      0 |           0 |           0 |            0 | sdnr/wt/odlux/apps/connectApp/src2/main/java/org/onap/ccsdk/features/sdnr/wt/odlux/bundles/MyOdluxBundle.java            |
| MyOdluxBundle.java  |              8 |             8 |           0 |      0 |           0 |           0 |            0 | sdnr/wt/odlux/apps/inventoryApp/src2/main/java/org/onap/ccsdk/features/sdnr/wt/odlux/bundles/MyOdluxBundle.java          |
| MyOdluxBundle.java  |              8 |             8 |           0 |      0 |           0 |           0 |            0 | sdnr/wt/odlux/apps/minimumApp/src2/main/java/org/onap/ccsdk/features/sdnr/wt/odlux/bundles/MyOdluxBundle.java            |

