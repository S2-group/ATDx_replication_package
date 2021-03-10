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
|<p align="center">Project 1</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_sdc-dcae-d-ci.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/sdc-dcae-d-ci) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_sdc-dcae-d-ci) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_sdc-dcae-d-ci.json)</p>|<p align="center">Project 2</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_sdc-dcae-d-dt-be-main.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/sdc-dcae-d-dt-be-main) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_sdc-dcae-d-dt-be-main) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_sdc-dcae-d-dt-be-main.json)</p>|<p align="center">Project 3</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_sdc-dcae-d-dt-be-property.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/sdc-dcae-d-dt-be-property) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_sdc-dcae-d-dt-be-property) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_sdc-dcae-d-dt-be-property.json)</p>
 | |
|<p align="center">Project 4</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_sdc-sdc-be-common.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/sdc-sdc-be-common) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_sdc-sdc-be-common) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_sdc-sdc-be-common.json)</p>|<p align="center">Project 5</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_sdc-sdc-distribution-client.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/sdc-sdc-distribution-client) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_sdc-sdc-distribution-client) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_sdc-sdc-distribution-client.json)</p>|<p align="center">Project 6</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_sdc-sdc-tosca.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/sdc-sdc-tosca) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_sdc-sdc-tosca) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_sdc-sdc-tosca.json)</p>
 | |
|<p align="center">Project 7</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_sdc-sdc-workflow-designer.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/sdc-sdc-workflow-designer) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_sdc-sdc-workflow-designer) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_sdc-sdc-workflow-designer.json)</p>|<p align="center">Project 8</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_sdc.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/sdc) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_sdc) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_sdc.json)</p>
# ATDx project report summaries
## Project 1: _onap/sdc-dcae-d-ci_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_sdc-dcae-d-ci.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/sdc-dcae-d-ci) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_sdc-dcae-d-ci) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_sdc-dcae-d-ci.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                         |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                 |
|:-----------------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:-------------------------------------------------------------------------------------------|
| RuleEditorControllerTest.java      |              8 |             0 |           8 |      0 |           0 |           0 |            0 | src/main/java/org/onap/dcae/ci/api/tests/ruleEditor/RuleEditorControllerTest.java          |
| PostAttachment.java                |              7 |             0 |           7 |      0 |           0 |           0 |            0 | src/main/java/org/onap/dcae/ci/api/tests/services/attachment/PostAttachment.java           |
| PutCheckout.java                   |              7 |             0 |           7 |      0 |           0 |           0 |            0 | src/main/java/org/onap/dcae/ci/api/tests/lifeCycle/PutCheckout.java                        |
| PutCheckin.java                    |              7 |             0 |           7 |      0 |           0 |           0 |            0 | src/main/java/org/onap/dcae/ci/api/tests/lifeCycle/PutCheckin.java                         |
| DcaeEntityClient.java              |              6 |             0 |           6 |      0 |           0 |           0 |            0 | src/main/java/org/onap/dcae/ci/utilities/DcaeEntityClient.java                             |
| DcaeUtil.java                      |              5 |             0 |           2 |      0 |           3 |           0 |            0 | src/main/java/org/onap/dcae/ci/utilities/DcaeUtil.java                                     |
| CreateMonitoringComponent.java     |              4 |             0 |           4 |      0 |           0 |           0 |            0 | src/main/java/org/onap/dcae/ci/api/tests/vfcmt/CreateMonitoringComponent.java              |
| GetServiceInstancePositive.java    |              3 |             0 |           3 |      0 |           0 |           0 |            0 | src/main/java/org/onap/dcae/ci/api/tests/services/instance/GetServiceInstancePositive.java |
| GetDefinitionTest.java             |              3 |             0 |           3 |      0 |           0 |           0 |            0 | src/main/java/org/onap/dcae/ci/api/tests/ruleEditor/GetDefinitionTest.java                 |
| CompositionControllerApiTests.java |              2 |             0 |           2 |      0 |           0 |           0 |            0 | src/main/java/org/onap/dcae/ci/api/tests/composition/CompositionControllerApiTests.java    |

## Project 2: _onap/sdc-dcae-d-dt-be-main_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_sdc-dcae-d-dt-be-main.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/sdc-dcae-d-dt-be-main) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_sdc-dcae-d-dt-be-main) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_sdc-dcae-d-dt-be-main.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                 |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                |
|:---------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:------------------------------------------------------------------------------------------|
| ServiceBusinessLogic.java  |              2 |             0 |           2 |      0 |           0 |           0 |            0 | dcaedt_be/src/main/java/org/onap/sdc/dcae/composition/impl/ServiceBusinessLogic.java      |
| CompositionEngine.java     |              2 |             0 |           2 |      0 |           0 |           0 |            0 | dcaedt_be/src/main/java/org/onap/sdc/dcae/composition/CompositionEngine.java              |
| BlueprintController.java   |              2 |             0 |           0 |      0 |           1 |           0 |            1 | dcaedt_be/src/main/java/org/onap/sdc/dcae/composition/controller/BlueprintController.java |
| ServicesController.java    |              2 |             0 |           0 |      0 |           1 |           0 |            1 | dcaedt_be/src/main/java/org/onap/sdc/dcae/composition/controller/ServicesController.java  |
| PolicyException.java       |              1 |             0 |           1 |      0 |           0 |           0 |            0 | dcaedt_catalog/asdc/src/main/java/org/onap/sdc/dcae/errormng/PolicyException.java         |
| ServiceException.java      |              1 |             0 |           1 |      0 |           0 |           0 |            0 | dcaedt_catalog/asdc/src/main/java/org/onap/sdc/dcae/errormng/ServiceException.java        |
| Normalizers.java           |              1 |             0 |           0 |      0 |           1 |           0 |            0 | dcaedt_catalog/asdc/src/main/java/org/onap/sdc/dcae/utils/Normalizers.java                |
| ActionTranslator.java      |              1 |             0 |           0 |      0 |           1 |           0 |            0 | dcaedt_be/src/main/java/org/onap/sdc/dcae/rule/editor/translators/ActionTranslator.java   |
| AbstractSdncException.java |              1 |             0 |           1 |      0 |           0 |           0 |            0 | dcaedt_catalog/asdc/src/main/java/org/onap/sdc/dcae/errormng/AbstractSdncException.java   |
| VfcmtBusinessLogic.java    |              1 |             0 |           1 |      0 |           0 |           0 |            0 | dcaedt_be/src/main/java/org/onap/sdc/dcae/composition/impl/VfcmtBusinessLogic.java        |

## Project 3: _onap/sdc-dcae-d-dt-be-property_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_sdc-dcae-d-dt-be-property.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/sdc-dcae-d-dt-be-property) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_sdc-dcae-d-dt-be-property) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_sdc-dcae-d-dt-be-property.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                   | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                                  |
|:-----------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:--------------------------------------------------------------------------------------------|
| OnapLogConfiguration.java    | 28             | 0             | 0           | 0      | 28          | 0           | 0            | src/main/java/org/onap/sdc/common/onaplog/OnapLogConfiguration.java                         |
| DcaeBeConstants.java         | 3              | 0             | 0           | 0      | 3           | 0           | 0            | src/main/java/org/onap/sdc/dcae/composition/util/DcaeBeConstants.java                       |
| RequirementDeserializer.java | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/onap/sdc/dcae/composition/model/deserializer/RequirementDeserializer.java |
| ValueDeserializer.java       | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/onap/sdc/dcae/composition/model/deserializer/ValueDeserializer.java       |
| ApplyFilterRequest.java      | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/onap/sdc/dcae/composition/restmodels/ruleeditor/ApplyFilterRequest.java   |
| DcaeFeConstants.java         | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/onap/sdc/dcae/composition/util/DcaeFeConstants.java                       |
| -                            | -              | -             | -           | -      | -           | -           | -            | -                                                                                           |
| -                            | -              | -             | -           | -      | -           | -           | -            | -                                                                                           |
| -                            | -              | -             | -           | -      | -           | -           | -            | -                                                                                           |
| -                            | -              | -             | -           | -      | -           | -           | -            | -                                                                                           |

## Project 4: _onap/sdc-sdc-be-common_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_sdc-sdc-be-common.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/sdc-sdc-be-common) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_sdc-sdc-be-common) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_sdc-sdc-be-common.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                     |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                           |
|:-------------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:-----------------------------------------------------------------------------------------------------|
| Logger.java                    |             42 |             0 |           0 |      0 |          21 |           0 |           21 | security-util-lib/src/main/java/org/onap/sdc/security/logging/wrappers/Logger.java                   |
| LoggerError.java               |              2 |             2 |           0 |      0 |           0 |           0 |            0 | security-util-lib/src/main/java/org/onap/sdc/security/logging/elements/LoggerError.java              |
| FilterServletOutputStream.java |              2 |             2 |           0 |      0 |           0 |           0 |            0 | security-util-lib/src/main/java/org/onap/sdc/security/filters/FilterServletOutputStream.java         |
| SecurityLogsUtils.java         |              2 |             0 |           0 |      0 |           2 |           0 |            0 | security-util-lib/src/main/java/org/onap/sdc/security/utils/SecurityLogsUtils.java                   |
| RepresentationUtils.java       |              1 |             0 |           0 |      0 |           1 |           0 |            0 | security-util-lib/src/main/java/org/onap/sdc/security/RepresentationUtils.java                       |
| AuthenticationCookieUtils.java |              1 |             0 |           0 |      0 |           1 |           0 |            0 | security-util-lib/src/main/java/org/onap/sdc/security/AuthenticationCookieUtils.java                 |
| CipherUtil.java                |              1 |             0 |           0 |      0 |           1 |           0 |            0 | security-util-lib/src/main/java/org/onap/sdc/security/CipherUtil.java                                |
| RestrictionAccessFilter.java   |              1 |             1 |           0 |      0 |           0 |           0 |            0 | security-util-lib/src/main/java/org/onap/sdc/security/filters/RestrictionAccessFilter.java           |
| RestUtils.java                 |              1 |             0 |           0 |      0 |           1 |           0 |            0 | security-util-lib/src/main/java/org/onap/sdc/security/utils/RestUtils.java                           |
| SynchronizationState.java      |              1 |             1 |           0 |      0 |           0 |           0 |            0 | versioning-lib/src/main/java/org/onap/sdc/common/versioning/services/types/SynchronizationState.java |

## Project 5: _onap/sdc-sdc-distribution-client_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_sdc-sdc-distribution-client.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/sdc-sdc-distribution-client) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_sdc-sdc-distribution-client) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_sdc-sdc-distribution-client.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                             | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                                            |
|:---------------------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:------------------------------------------------------------------------------------------------------|
| IDistributionClientDownloadResult.java | 2              | 0             | 0           | 0      | 1           | 0           | 1            | sdc-distribution-client/src/main/java/org/onap/sdc/api/results/IDistributionClientDownloadResult.java |
| IDistributionClient.java               | 2              | 0             | 0           | 0      | 1           | 0           | 1            | sdc-distribution-client/src/main/java/org/onap/sdc/api/IDistributionClient.java                       |
| -                                      | -              | -             | -           | -      | -           | -           | -            | -                                                                                                     |
| -                                      | -              | -             | -           | -      | -           | -           | -            | -                                                                                                     |
| -                                      | -              | -             | -           | -      | -           | -           | -            | -                                                                                                     |
| -                                      | -              | -             | -           | -      | -           | -           | -            | -                                                                                                     |
| -                                      | -              | -             | -           | -      | -           | -           | -            | -                                                                                                     |
| -                                      | -              | -             | -           | -      | -           | -           | -            | -                                                                                                     |
| -                                      | -              | -             | -           | -      | -           | -           | -            | -                                                                                                     |
| -                                      | -              | -             | -           | -      | -           | -           | -            | -                                                                                                     |

## Project 6: _onap/sdc-sdc-tosca_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_sdc-sdc-tosca.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/sdc-sdc-tosca) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_sdc-sdc-tosca) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_sdc-sdc-tosca.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                        |
|:--------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:----------------------------------------------------------------------------------|
| ISdcCsarHelper.java       |             90 |             0 |           0 |      0 |          45 |           0 |           45 | sdc-tosca/src/main/java/org/onap/sdc/tosca/parser/api/ISdcCsarHelper.java         |
| CapabilityTypeDef.java    |              4 |             4 |           0 |      0 |           0 |           0 |            0 | jtosca/src/main/java/org/onap/sdc/toscaparser/api/elements/CapabilityTypeDef.java |
| TOSCAException.java       |              3 |             0 |           3 |      0 |           0 |           0 |            0 | jtosca/src/main/java/org/onap/sdc/toscaparser/api/common/TOSCAException.java      |
| NodeType.java             |              2 |             1 |           0 |      0 |           1 |           0 |            0 | jtosca/src/main/java/org/onap/sdc/toscaparser/api/elements/NodeType.java          |
| ArtifactTypeDef.java      |              2 |             2 |           0 |      0 |           0 |           0 |            0 | jtosca/src/main/java/org/onap/sdc/toscaparser/api/elements/ArtifactTypeDef.java   |
| SubstitutionMappings.java |              2 |             0 |           0 |      0 |           1 |           0 |            1 | jtosca/src/main/java/org/onap/sdc/toscaparser/api/SubstitutionMappings.java       |
| GroupType.java            |              2 |             2 |           0 |      0 |           0 |           0 |            0 | jtosca/src/main/java/org/onap/sdc/toscaparser/api/elements/GroupType.java         |
| PolicyType.java           |              2 |             2 |           0 |      0 |           0 |           0 |            0 | jtosca/src/main/java/org/onap/sdc/toscaparser/api/elements/PolicyType.java        |
| SdcToscaUtility.java      |              1 |             0 |           0 |      0 |           1 |           0 |            0 | sdc-tosca/src/main/java/org/onap/sdc/tosca/parser/utils/SdcToscaUtility.java      |
| GeneralUtility.java       |              1 |             0 |           0 |      0 |           1 |           0 |            0 | sdc-tosca/src/main/java/org/onap/sdc/tosca/parser/utils/GeneralUtility.java       |

## Project 7: _onap/sdc-sdc-workflow-designer_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_sdc-sdc-workflow-designer.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/sdc-sdc-workflow-designer) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_sdc-sdc-workflow-designer) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_sdc-sdc-workflow-designer.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                       | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                                                   |
|:---------------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:-------------------------------------------------------------------------------------------------------------|
| JsonUtil.java                    | 2              | 0             | 2           | 0      | 0           | 0           | 0            | sdc-workflow-designer-be/src/main/java/org/onap/sdc/workflow/services/utilities/JsonUtil.java                |
| ArtifactAssociationService.java  | 1              | 0             | 0           | 0      | 1           | 0           | 0            | sdc-workflow-designer-be/src/main/java/org/onap/sdc/workflow/api/ArtifactAssociationService.java             |
| WorkflowValidationConstants.java | 1              | 0             | 0           | 0      | 1           | 0           | 0            | sdc-workflow-designer-be/src/main/java/org/onap/sdc/workflow/services/types/WorkflowValidationConstants.java |
| -                                | -              | -             | -           | -      | -           | -           | -            | -                                                                                                            |
| -                                | -              | -             | -           | -      | -           | -           | -            | -                                                                                                            |
| -                                | -              | -             | -           | -      | -           | -           | -            | -                                                                                                            |
| -                                | -              | -             | -           | -      | -           | -           | -            | -                                                                                                            |
| -                                | -              | -             | -           | -      | -           | -           | -            | -                                                                                                            |
| -                                | -              | -             | -           | -      | -           | -           | -            | -                                                                                                            |
| -                                | -              | -             | -           | -      | -           | -           | -            | -                                                                                                            |

## Project 8: _onap/sdc_
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

