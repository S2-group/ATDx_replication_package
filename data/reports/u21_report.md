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
|<p align="center">Project 1</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_appc.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/appc) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_appc) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_appc.json)</p>|<p align="center">Project 2</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_ccsdk-sli-adaptors.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/ccsdk-sli-adaptors) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_ccsdk-sli-adaptors) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_ccsdk-sli-adaptors.json)</p>|<p align="center">Project 3</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_dmaap-messagerouter-dmaapclient.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/dmaap-messagerouter-dmaapclient) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_dmaap-messagerouter-dmaapclient) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_dmaap-messagerouter-dmaapclient.json)</p>
 | |
|<p align="center">Project 4</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_dmaap-messagerouter-msgrtr.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/dmaap-messagerouter-msgrtr) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_dmaap-messagerouter-msgrtr) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_dmaap-messagerouter-msgrtr.json)</p>|<p align="center">Project 5</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_music.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/music) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_music) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_music.json)</p>|<p align="center">Project 6</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_portal.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/portal) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_portal) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_portal.json)</p>
 | |
|<p align="center">Project 7</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_so.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/so) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_so) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_so.json)</p>|<p align="center">Project 8</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_usecase-ui-server.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/usecase-ui-server) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_usecase-ui-server) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_usecase-ui-server.json)</p>|<p align="center">Project 9</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_vnfsdk-ves-agent.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/vnfsdk-ves-agent) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_vnfsdk-ves-agent) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_vnfsdk-ves-agent.json)</p>

# ATDx project report summaries
## Project 1: _onap/appc_
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

## Project 2: _onap/ccsdk-sli-adaptors_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_ccsdk-sli-adaptors.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/ccsdk-sli-adaptors) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_ccsdk-sli-adaptors) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_ccsdk-sli-adaptors.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                  |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                                 |
|:----------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:-----------------------------------------------------------------------------------------------------------|
| ResourceRequest.java        |             23 |             0 |           0 |      0 |          23 |           0 |            0 | resource-assignment/provider/src/main/java/org/onap/ccsdk/sli/adaptors/ra/comp/ResourceRequest.java        |
| ResourceRule.java           |             11 |             0 |           0 |      0 |          11 |           0 |            0 | resource-assignment/provider/src/main/java/org/onap/ccsdk/sli/adaptors/ra/rule/data/ResourceRule.java      |
| RangeAllocationRequest.java |             10 |             0 |           0 |      0 |          10 |           0 |            0 | resource-assignment/provider/src/main/java/org/onap/ccsdk/sli/adaptors/rm/data/RangeAllocationRequest.java |
| AllocationItem.java         |             10 |             0 |           0 |      0 |          10 |           0 |            0 | resource-assignment/provider/src/main/java/org/onap/ccsdk/sli/adaptors/rm/dao/jdbc/AllocationItem.java     |
| ResourceResponse.java       |              9 |             0 |           0 |      0 |           9 |           0 |            0 | resource-assignment/provider/src/main/java/org/onap/ccsdk/sli/adaptors/ra/comp/ResourceResponse.java       |
| AllocationRequest.java      |              9 |             0 |           0 |      0 |           9 |           0 |            0 | resource-assignment/provider/src/main/java/org/onap/ccsdk/sli/adaptors/rm/data/AllocationRequest.java      |
| Resource.java               |              8 |             0 |           0 |      0 |           8 |           0 |            0 | resource-assignment/provider/src/main/java/org/onap/ccsdk/sli/adaptors/rm/dao/jdbc/Resource.java           |
| ResourceData.java           |              8 |             0 |           0 |      0 |           8 |           0 |            0 | resource-assignment/provider/src/main/java/org/onap/ccsdk/sli/adaptors/ra/comp/ResourceData.java           |
| ResourceAllocator.java      |              8 |             0 |           8 |      0 |           0 |           0 |            0 | resource-assignment/provider/src/main/java/org/onap/ccsdk/sli/adaptors/ra/ResourceAllocator.java           |
| AAIDeclarations.java        |              7 |             0 |           4 |      0 |           0 |           0 |            3 | aai-service/provider/src/main/java/org/onap/ccsdk/sli/adaptors/aai/AAIDeclarations.java                    |

## Project 3: _onap/dmaap-messagerouter-dmaapclient_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_dmaap-messagerouter-dmaapclient.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/dmaap-messagerouter-dmaapclient) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_dmaap-messagerouter-dmaapclient) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_dmaap-messagerouter-dmaapclient.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                   |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                               |
|:-----------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:-------------------------------------------------------------------------|
| MRBaseClient.java            |             18 |             0 |          17 |      0 |           1 |           0 |            0 | src/main/java/org/onap/dmaap/mr/client/impl/MRBaseClient.java            |
| MRClientFactory.java         |             18 |             0 |           7 |      0 |          11 |           0 |            0 | src/main/java/org/onap/dmaap/mr/client/MRClientFactory.java              |
| MRSimplerBatchPublisher.java |              6 |             0 |           1 |      0 |           3 |           2 |            0 | src/main/java/org/onap/dmaap/mr/client/impl/MRSimplerBatchPublisher.java |
| MRTopicManager.java          |              4 |             0 |           2 |      0 |           1 |           0 |            1 | src/main/java/org/onap/dmaap/mr/client/MRTopicManager.java               |
| MRConsumer.java              |              4 |             0 |           4 |      0 |           0 |           0 |            0 | src/main/java/org/onap/dmaap/mr/client/MRConsumer.java                   |
| SimpleExamplePublisher.java  |              4 |             0 |           4 |      0 |           0 |           0 |            0 | src/main/java/org/onap/dmaap/mr/test/clients/SimpleExamplePublisher.java |
| MRMetaClient.java            |              4 |             0 |           4 |      0 |           0 |           0 |            0 | src/main/java/org/onap/dmaap/mr/client/impl/MRMetaClient.java            |
| MRBatchPublisher.java        |              3 |             0 |           1 |      0 |           1 |           0 |            1 | src/main/java/org/onap/dmaap/mr/client/impl/MRBatchPublisher.java        |
| MRConsumerImpl.java          |              3 |             0 |           1 |      0 |           2 |           0 |            0 | src/main/java/org/onap/dmaap/mr/client/impl/MRConsumerImpl.java          |
| SimpleExamplePublisher.java  |              2 |             0 |           2 |      0 |           0 |           0 |            0 | src/main/java/org/onap/dmaap/mr/dme/client/SimpleExamplePublisher.java   |

## Project 4: _onap/dmaap-messagerouter-msgrtr_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_dmaap-messagerouter-msgrtr.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/dmaap-messagerouter-msgrtr) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_dmaap-messagerouter-msgrtr) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_dmaap-messagerouter-msgrtr.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                      |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                           |
|:--------------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:-------------------------------------------------------------------------------------|
| MMServiceImpl.java              |              6 |             0 |           6 |      0 |           0 |           0 |            0 | src/main/java/org/onap/dmaap/dmf/mr/service/impl/MMServiceImpl.java                  |
| ConfigurationReader.java        |              4 |             0 |           3 |      0 |           1 |           0 |            0 | src/main/java/org/onap/dmaap/dmf/mr/utils/ConfigurationReader.java                   |
| CambriaOutboundEventStream.java |              4 |             0 |           4 |      0 |           0 |           0 |            0 | src/main/java/org/onap/dmaap/dmf/mr/resources/CambriaOutboundEventStream.java        |
| EventsServiceImpl.java          |              4 |             0 |           4 |      0 |           0 |           0 |            0 | src/main/java/org/onap/dmaap/dmf/mr/service/impl/EventsServiceImpl.java              |
| KafkaConsumerCache.java         |              3 |             0 |           0 |      0 |           0 |           0 |            3 | src/main/java/org/onap/dmaap/dmf/mr/backends/kafka/KafkaConsumerCache.java           |
| TopicServiceImpl.java           |              3 |             0 |           3 |      0 |           0 |           0 |            0 | src/main/java/org/onap/dmaap/dmf/mr/service/impl/TopicServiceImpl.java               |
| DMaaPCambriaClientFactory.java  |              3 |             0 |           0 |      0 |           3 |           0 |            0 | src/main/java/org/onap/dmaap/dmf/mr/metrics/publisher/DMaaPCambriaClientFactory.java |
| UIServiceImpl.java              |              2 |             0 |           2 |      0 |           0 |           0 |            0 | src/main/java/org/onap/dmaap/dmf/mr/service/impl/UIServiceImpl.java                  |
| TopicService.java               |              2 |             0 |           2 |      0 |           0 |           0 |            0 | src/main/java/org/onap/dmaap/dmf/mr/service/TopicService.java                        |
| CambriaPublisherUtility.java    |              2 |             0 |           1 |      0 |           1 |           0 |            0 | src/main/java/org/onap/dmaap/dmf/mr/metrics/publisher/CambriaPublisherUtility.java   |

## Project 5: _onap/music_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_music.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/music) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_music) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_music.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                  |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                     |
|:----------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:-------------------------------------------------------------------------------|
| RestMusicDataAPI.java       |             18 |             0 |           6 |      0 |          12 |           0 |            0 | music-rest/src/main/java/org/onap/music/rest/RestMusicDataAPI.java             |
| RestMusicLocksAPI.java      |             13 |             0 |           8 |      0 |           3 |           0 |            2 | music-rest/src/main/java/org/onap/music/rest/RestMusicLocksAPI.java            |
| MusicUtil.java              |              9 |             0 |           5 |      0 |           2 |           0 |            2 | music-core/src/main/java/org/onap/music/main/MusicUtil.java                    |
| CipherUtil.java             |              8 |             0 |           0 |      0 |           4 |           0 |            4 | music-core/src/main/java/org/onap/music/main/CipherUtil.java                   |
| RestMusicQAPI.java          |              7 |             0 |           0 |      0 |           7 |           0 |            0 | music-rest/src/main/java/org/onap/music/rest/RestMusicQAPI.java                |
| MusicCassaCore.java         |              6 |             0 |           0 |      0 |           3 |           0 |            3 | music-core/src/main/java/org/onap/music/service/impl/MusicCassaCore.java       |
| MusicDeadlockException.java |              4 |             0 |           4 |      0 |           0 |           0 |            0 | music-core/src/main/java/org/onap/music/exceptions/MusicDeadlockException.java |
| JsonInsert.java             |              2 |             0 |           0 |      0 |           2 |           0 |            0 | music-core/src/main/java/org/onap/music/datastore/jsonobjects/JsonInsert.java  |
| JsonSelect.java             |              2 |             0 |           0 |      0 |           2 |           0 |            0 | music-core/src/main/java/org/onap/music/datastore/jsonobjects/JsonSelect.java  |
| MusicServiceException.java  |              2 |             0 |           2 |      0 |           0 |           0 |            0 | music-core/src/main/java/org/onap/music/exceptions/MusicServiceException.java  |

## Project 6: _onap/portal_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_portal.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/portal) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_portal) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_portal.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                         |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                                   |
|:-----------------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:-------------------------------------------------------------------------------------------------------------|
| ExternalAccessRolesService.java    |             37 |             0 |          37 |      0 |           0 |           0 |            0 | ecomp-portal-BE-common/src/main/java/org/onap/portalapp/portal/service/ExternalAccessRolesService.java       |
| RolesController.java               |             28 |             0 |          28 |      0 |           0 |           0 |            0 | ecomp-portal-BE-common/src/main/java/org/onap/portalapp/portal/controller/RolesController.java               |
| UserRolesCommonServiceImpl.java    |             25 |             0 |          23 |      0 |           2 |           0 |            0 | ecomp-portal-BE-common/src/main/java/org/onap/portalapp/portal/service/UserRolesCommonServiceImpl.java       |
| OnboardingApp.java                 |             20 |             0 |           0 |      0 |          20 |           0 |            0 | ecomp-portal-BE-os/src/main/java/org/onap/portalapp/portal/transport/OnboardingApp.java                      |
| SharedContextRestController.java   |             12 |             0 |          12 |      0 |           0 |           0 |            0 | ecomp-portal-BE-common/src/main/java/org/onap/portalapp/portal/controller/SharedContextRestController.java   |
| RolesApprovalSystemController.java |              8 |             0 |           8 |      0 |           0 |           0 |            0 | ecomp-portal-BE-common/src/main/java/org/onap/portalapp/portal/controller/RolesApprovalSystemController.java |
| EPAppCommonServiceImpl.java        |              8 |             2 |           4 |      0 |           1 |           0 |            1 | ecomp-portal-BE-common/src/main/java/org/onap/portalapp/portal/service/EPAppCommonServiceImpl.java           |
| BasicAuthAccountService.java       |              7 |             0 |           7 |      0 |           0 |           0 |            0 | ecomp-portal-BE-common/src/main/java/org/onap/portalapp/portal/service/BasicAuthAccountService.java          |
| CommonSessionCookieUtil.java       |              6 |             0 |           2 |      0 |           4 |           0 |            0 | ecomp-portal-BE-common/src/main/java/org/onap/portalapp/util/CommonSessionCookieUtil.java                    |
| SchedulerController.java           |              6 |             0 |           5 |      0 |           0 |           1 |            0 | ecomp-portal-BE-common/src/main/java/org/onap/portalapp/portal/controller/SchedulerController.java           |

## Project 7: _onap/so_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_so.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/so) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_so) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_so.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                          |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                                 |
|:------------------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:-----------------------------------------------------------------------------------------------------------|
| BBInputSetup.java                   |             20 |             0 |          16 |      0 |           4 |           0 |            0 | bpmn/MSOCommonBPMN/src/main/java/org/onap/so/bpmn/servicedecomposition/tasks/BBInputSetup.java             |
| MsoNetworkAdapterImpl.java          |             14 |             0 |           1 |      0 |           9 |           0 |            4 | adapters/mso-openstack-adapters/src/main/java/org/onap/so/adapters/network/MsoNetworkAdapterImpl.java      |
| NetworkAdapterResources.java        |             12 |             0 |          10 |      0 |           2 |           0 |            0 | bpmn/so-bpmn-tasks/src/main/java/org/onap/so/client/orchestration/NetworkAdapterResources.java             |
| ResourceModelInfo.java              |             12 |            12 |           0 |      0 |           0 |           0 |            0 | bpmn/so-bpmn-tasks/src/main/java/org/onap/so/client/oof/beans/ResourceModelInfo.java                       |
| BBInputSetupUtils.java              |             10 |             0 |          10 |      0 |           0 |           0 |            0 | bpmn/MSOCommonBPMN/src/main/java/org/onap/so/bpmn/servicedecomposition/tasks/BBInputSetupUtils.java        |
| WorkflowAction.java                 |              9 |             0 |           6 |      0 |           3 |           0 |            0 | bpmn/so-bpmn-tasks/src/main/java/org/onap/so/bpmn/infrastructure/workflow/tasks/WorkflowAction.java        |
| SDNCConfigurationResources.java     |              8 |             0 |           8 |      0 |           0 |           0 |            0 | bpmn/so-bpmn-tasks/src/main/java/org/onap/so/client/orchestration/SDNCConfigurationResources.java          |
| MsoNetworkAdapter.java              |              7 |             0 |           0 |      0 |           7 |           0 |            0 | adapters/mso-openstack-adapters/src/main/java/org/onap/so/adapters/network/MsoNetworkAdapter.java          |
| VnfAdapterVfModuleObjectMapper.java |              6 |             0 |           5 |      0 |           1 |           0 |            0 | bpmn/so-bpmn-tasks/src/main/java/org/onap/so/client/adapter/vnf/mapper/VnfAdapterVfModuleObjectMapper.java |
| MsoRequestsDbAdapter.java           |              6 |             0 |           0 |      0 |           5 |           0 |            1 | adapters/mso-requests-db-adapter/src/main/java/org/onap/so/adapters/requestsdb/MsoRequestsDbAdapter.java   |

## Project 8: _onap/usecase-ui-server_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_usecase-ui-server.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/usecase-ui-server) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_usecase-ui-server) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_usecase-ui-server.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                         |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                          |
|:-----------------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:----------------------------------------------------------------------------------------------------|
| ResourceMgtServiceConvert.java     |              5 |             0 |           5 |      0 |           0 |           0 |            0 | server/src/main/java/org/onap/usecaseui/server/service/nsmf/impl/ResourceMgtServiceConvert.java     |
| ResourceMonitorServiceConvert.java |              4 |             0 |           4 |      0 |           0 |           0 |            0 | server/src/main/java/org/onap/usecaseui/server/service/nsmf/impl/ResourceMonitorServiceConvert.java |
| SotnServiceTemplateService.java    |              4 |             0 |           4 |      0 |           0 |           0 |            0 | server/src/main/java/org/onap/usecaseui/server/service/lcm/SotnServiceTemplateService.java          |
| DateUtils.java                     |              3 |             0 |           2 |      0 |           1 |           0 |            0 | server/src/main/java/org/onap/usecaseui/server/util/DateUtils.java                                  |
| CommonConstant.java                |              2 |             0 |           0 |      0 |           2 |           0 |            0 | server/src/main/java/org/onap/usecaseui/server/constant/CommonConstant.java                         |
| Constant.java                      |              2 |             0 |           0 |      0 |           2 |           0 |            0 | server/src/main/java/org/onap/usecaseui/server/constant/Constant.java                               |
| SotnServiceLcmController.java      |              2 |             0 |           2 |      0 |           0 |           0 |            0 | server/src/main/java/org/onap/usecaseui/server/controller/lcm/SotnServiceLcmController.java         |
| UuiServerApplication.java          |              1 |             0 |           0 |      0 |           1 |           0 |            0 | server/src/main/java/org/onap/usecaseui/server/UuiServerApplication.java                            |
| AlarmsHeader.java                  |              1 |             0 |           0 |      0 |           1 |           0 |            0 | server/src/main/java/org/onap/usecaseui/server/bean/AlarmsHeader.java                               |
| ServiceTemplateInput.java          |              1 |             0 |           0 |      0 |           1 |           0 |            0 | server/src/main/java/org/onap/usecaseui/server/bean/lcm/ServiceTemplateInput.java                   |

## Project 9: _onap/vnfsdk-ves-agent_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_vnfsdk-ves-agent.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/vnfsdk-ves-agent) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_vnfsdk-ves-agent) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_vnfsdk-ves-agent.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                  |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                         |
|:----------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:-------------------------------------------------------------------|
| EvelMobileFlow.java         |              5 |             2 |           0 |      0 |           3 |           0 |            0 | src/main/java/evel_javalibrary/att/com/EvelMobileFlow.java         |
| EvelScalingMeasurement.java |              4 |             2 |           1 |      0 |           1 |           0 |            0 | src/main/java/evel_javalibrary/att/com/EvelScalingMeasurement.java |
| RingBuffer.java             |              4 |             0 |           0 |      0 |           4 |           0 |            0 | src/main/java/evel_javalibrary/att/com/RingBuffer.java             |
| EvelSipSignaling.java       |              3 |             2 |           0 |      0 |           1 |           0 |            0 | src/main/java/evel_javalibrary/att/com/EvelSipSignaling.java       |
| EvelThresholdCross.java     |              3 |             2 |           0 |      0 |           1 |           0 |            0 | src/main/java/evel_javalibrary/att/com/EvelThresholdCross.java     |
| AgentMain.java              |              3 |             0 |           0 |      0 |           3 |           0 |            0 | src/main/java/evel_javalibrary/att/com/AgentMain.java              |
| EvelVoiceQuality.java       |              3 |             2 |           0 |      0 |           1 |           0 |            0 | src/main/java/evel_javalibrary/att/com/EvelVoiceQuality.java       |
| EvelFault.java              |              3 |             2 |           0 |      0 |           1 |           0 |            0 | src/main/java/evel_javalibrary/att/com/EvelFault.java              |
| EvelSyslog.java             |              2 |             2 |           0 |      0 |           0 |           0 |            0 | src/main/java/evel_javalibrary/att/com/EvelSyslog.java             |
| EvelPnfRegistration.java    |              2 |             2 |           0 |      0 |           0 |           0 |            0 | src/main/java/evel_javalibrary/att/com/EvelPnfRegistration.java    |

