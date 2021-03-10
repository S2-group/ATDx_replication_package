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
|<p align="center">Project 1</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_appc.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/appc) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_appc) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_appc.json)</p>|<p align="center">Project 2</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_clamp.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/clamp) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_clamp) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_clamp.json)</p>|<p align="center">Project 3</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_portal.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/portal) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_portal) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_portal.json)</p>
 | |
|<p align="center">Project 4</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_sdc.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/sdc) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_sdc) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_sdc.json)</p>|<p align="center">Project 5</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_so.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/so) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_so) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_so.json)</p>
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

## Project 2: _onap/clamp_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_clamp.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/clamp) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_clamp) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_clamp.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                               |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                          |
|:-----------------------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:------------------------------------------------------------------------------------|
| DcaeInventoryResponse.java               |              2 |             1 |           0 |      1 |           0 |           0 |            0 | src/main/java/org/onap/clamp/clds/model/dcae/DcaeInventoryResponse.java             |
| ToscaYamlToJsonConvertor.java            |              1 |             0 |           0 |      0 |           1 |           0 |            0 | src/main/java/org/onap/clamp/clds/tosca/ToscaYamlToJsonConvertor.java               |
| XmlTools.java                            |              1 |             0 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/onap/clamp/clds/util/XmlTools.java                                |
| PassDecoder.java                         |              1 |             0 |           0 |      0 |           1 |           0 |            0 | src/main/java/org/onap/clamp/util/PassDecoder.java                                  |
| SvgLoopGenerator.java                    |              1 |             0 |           0 |      0 |           1 |           0 |            0 | src/main/java/org/onap/clamp/clds/util/drawing/SvgLoopGenerator.java                |
| SecureServicePermissionDeserializer.java |              1 |             0 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/onap/clamp/authorization/SecureServicePermissionDeserializer.java |
| SemanticVersioning.java                  |              1 |             0 |           0 |      0 |           1 |           0 |            0 | src/main/java/org/onap/clamp/util/SemanticVersioning.java                           |
| DcaeDeployParameters.java                |              1 |             0 |           0 |      0 |           1 |           0 |            0 | src/main/java/org/onap/clamp/loop/deploy/DcaeDeployParameters.java                  |
| CsarInstaller.java                       |              1 |             0 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/onap/clamp/loop/CsarInstaller.java                                |
| ToscaMetadataProcess.java                |              1 |             0 |           0 |      0 |           1 |           0 |            0 | src/main/java/org/onap/clamp/clds/tosca/update/execution/ToscaMetadataProcess.java  |

## Project 3: _onap/portal_
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

## Project 4: _onap/sdc_
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

## Project 5: _onap/so_
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

