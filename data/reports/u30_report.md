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
|<p align="center">Project 1</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_clamp.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/clamp) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_clamp) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_clamp.json)</p>|<p align="center">Project 2</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_policy-apex-pdp.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/policy-apex-pdp) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_policy-apex-pdp) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_policy-apex-pdp.json)</p>|<p align="center">Project 3</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_policy-drools-applications.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/policy-drools-applications) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_policy-drools-applications) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_policy-drools-applications.json)</p>
 | |
|<p align="center">Project 4</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_policy-drools-pdp.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/policy-drools-pdp) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_policy-drools-pdp) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_policy-drools-pdp.json)</p>|<p align="center">Project 5</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_policy-engine.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/policy-engine) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_policy-engine) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_policy-engine.json)</p>|<p align="center">Project 6</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_policy-models.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/policy-models) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_policy-models) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_policy-models.json)</p>
 | |

# ATDx project report summaries
## Project 1: _onap/clamp_
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

## Project 2: _onap/policy-apex-pdp_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_policy-apex-pdp.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/policy-apex-pdp) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_policy-apex-pdp) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_policy-apex-pdp.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name           | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                                        |
|:---------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:--------------------------------------------------------------------------------------------------|
| ApexModelImpl.java   | 3              | 2             | 0           | 1      | 0           | 0           | 0            | model/model-api/src/main/java/org/onap/policy/apex/model/modelapi/impl/ApexModelImpl.java         |
| ApexEditorApi.java   | 3              | 0             | 0           | 0      | 3           | 0           | 0            | model/model-api/src/main/java/org/onap/policy/apex/model/modelapi/ApexEditorApi.java              |
| AxStateTree.java     | 2              | 1             | 0           | 1      | 0           | 0           | 0            | model/policy-model/src/main/java/org/onap/policy/apex/model/policymodel/concepts/AxStateTree.java |
| ApexModel.java       | 2              | 1             | 0           | 1      | 0           | 0           | 0            | model/model-api/src/main/java/org/onap/policy/apex/model/modelapi/ApexModel.java                  |
| CollectionUtils.java | 1              | 0             | 0           | 0      | 1           | 0           | 0            | model/utilities/src/main/java/org/onap/policy/apex/model/utilities/CollectionUtils.java           |
| TreeMapUtils.java    | 1              | 0             | 0           | 0      | 1           | 0           | 0            | model/utilities/src/main/java/org/onap/policy/apex/model/utilities/TreeMapUtils.java              |
| -                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                                 |
| -                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                                 |
| -                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                                 |
| -                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                                 |

## Project 3: _onap/policy-drools-applications_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_policy-drools-applications.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/policy-drools-applications) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_policy-drools-applications) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_policy-drools-applications.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                           | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                                  |
|:-------------------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:--------------------------------------------------------------------------------------------|
| GuardContext.java                    | 2              | 0             | 0           | 0      | 2           | 0           | 0            | controlloop/m2/guard/src/main/java/org/onap/policy/guard/GuardContext.java                  |
| Util.java                            | 1              | 0             | 0           | 0      | 1           | 0           | 0            | controlloop/m2/base/src/main/java/org/onap/policy/m2/base/Util.java                         |
| DroolsSessionCommonSerializable.java | 1              | 1             | 0           | 0      | 0           | 0           | 0            | controlloop/m2/util/src/main/java/org/onap/policy/util/DroolsSessionCommonSerializable.java |
| -                                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                           |
| -                                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                           |
| -                                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                           |
| -                                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                           |
| -                                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                           |
| -                                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                           |
| -                                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                           |

## Project 4: _onap/policy-drools-pdp_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_policy-drools-pdp.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/policy-drools-pdp) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_policy-drools-pdp) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_policy-drools-pdp.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                     | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                                                   |
|:-------------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:-------------------------------------------------------------------------------------------------------------|
| Bucket.java                    | 11             | 2             | 1           | 2      | 0           | 0           | 6            | feature-server-pool/src/main/java/org/onap/policy/drools/serverpool/Bucket.java                              |
| Server.java                    | 8              | 1             | 4           | 1      | 0           | 0           | 2            | feature-server-pool/src/main/java/org/onap/policy/drools/serverpool/Server.java                              |
| TargetLock.java                | 7              | 0             | 1           | 0      | 0           | 0           | 6            | feature-server-pool/src/main/java/org/onap/policy/drools/serverpool/TargetLock.java                          |
| Leader.java                    | 5              | 1             | 0           | 1      | 1           | 0           | 2            | feature-server-pool/src/main/java/org/onap/policy/drools/serverpool/Leader.java                              |
| StateManagementFeatureApi.java | 4              | 0             | 4           | 0      | 0           | 0           | 0            | api-state-management/src/main/java/org/onap/policy/drools/statemanagement/StateManagementFeatureApi.java     |
| ServerPoolProperties.java      | 1              | 0             | 0           | 0      | 1           | 0           | 0            | feature-server-pool/src/main/java/org/onap/policy/drools/serverpool/ServerPoolProperties.java                |
| Util.java                      | 1              | 0             | 0           | 0      | 1           | 0           | 0            | feature-server-pool/src/main/java/org/onap/policy/drools/serverpool/Util.java                                |
| DroolsPdpIntegrityMonitor.java | 1              | 0             | 1           | 0      | 0           | 0           | 0            | feature-state-management/src/main/java/org/onap/policy/drools/statemanagement/DroolsPdpIntegrityMonitor.java |
| -                              | -              | -             | -           | -      | -           | -           | -            | -                                                                                                            |
| -                              | -              | -             | -           | -      | -           | -           | -            | -                                                                                                            |

## Project 5: _onap/policy-engine_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_policy-engine.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/policy-engine) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_policy-engine) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_policy-engine.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                     |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                    |
|:-------------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:----------------------------------------------------------------------------------------------|
| PolicyEngine.java              |             38 |             0 |           0 |      0 |          21 |           0 |           17 | PolicyEngineAPI/src/main/java/org/onap/policy/api/PolicyEngine.java                           |
| PolicyEngineServices.java      |             10 |             0 |           0 |      0 |           5 |           0 |            5 | ONAP-PDP-REST/src/main/java/org/onap/policy/pdp/rest/api/controller/PolicyEngineServices.java |
| ElkConnector.java              |              7 |             0 |           7 |      0 |           0 |           0 |            0 | ONAP-PAP-REST/src/main/java/org/onap/policy/pap/xacml/rest/elk/client/ElkConnector.java       |
| ElkConnectorImpl.java          |              7 |             0 |           7 |      0 |           0 |           0 |            0 | ONAP-PAP-REST/src/main/java/org/onap/policy/pap/xacml/rest/elk/client/ElkConnectorImpl.java   |
| SavePolicyHandler.java         |              4 |             0 |           4 |      0 |           0 |           0 |            0 | ONAP-PAP-REST/src/main/java/org/onap/policy/pap/xacml/rest/handler/SavePolicyHandler.java     |
| DecisionRequestParameters.java |              4 |             0 |           0 |      0 |           2 |           0 |            2 | PolicyEngineAPI/src/main/java/org/onap/policy/api/DecisionRequestParameters.java              |
| ConfigRequestParameters.java   |              4 |             0 |           0 |      0 |           2 |           0 |            2 | PolicyEngineAPI/src/main/java/org/onap/policy/api/ConfigRequestParameters.java                |
| PolicyParameters.java          |              4 |             0 |           0 |      0 |           2 |           0 |            2 | PolicyEngineAPI/src/main/java/org/onap/policy/api/PolicyParameters.java                       |
| PolicyApiUtils.java            |              4 |             0 |           3 |      0 |           1 |           0 |            0 | ONAP-PDP-REST/src/main/java/org/onap/policy/pdp/rest/api/utils/PolicyApiUtils.java            |
| ConfigPolicyAPIRequest.java    |              4 |             0 |           0 |      0 |           2 |           0 |            2 | ONAP-PDP-REST/src/main/java/org/onap/policy/pdp/rest/api/models/ConfigPolicyAPIRequest.java   |

## Project 6: _onap/policy-models_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_policy-models.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/policy-models) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_policy-models) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_policy-models.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                            | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                                                                             |
|:--------------------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:---------------------------------------------------------------------------------------------------------------------------------------|
| PdpStatisticsProvider.java            | 1              | 0             | 0           | 0      | 1           | 0           | 0            | models-pdp/src/main/java/org/onap/policy/models/pdp/persistence/provider/PdpStatisticsProvider.java                                    |
| PfDao.java                            | 1              | 0             | 0           | 0      | 1           | 0           | 0            | models-dao/src/main/java/org/onap/policy/models/dao/PfDao.java                                                                         |
| BasicBidirectionalTopicOperation.java | 1              | 0             | 1           | 0      | 0           | 0           | 0            | models-interactions/model-actors/actor.test/src/main/java/org/onap/policy/controlloop/actor/test/BasicBidirectionalTopicOperation.java |
| -                                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                                                                      |
| -                                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                                                                      |
| -                                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                                                                      |
| -                                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                                                                      |
| -                                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                                                                      |
| -                                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                                                                      |
| -                                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                                                                      |

