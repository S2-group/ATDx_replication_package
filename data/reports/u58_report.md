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
|<p align="center">Project 1</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_dcaegen2-collectors-ves.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/dcaegen2-collectors-ves) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_dcaegen2-collectors-ves) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_dcaegen2-collectors-ves.json)</p>|<p align="center">Project 2</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_dcaegen2-services-prh.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/dcaegen2-services-prh) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_dcaegen2-services-prh) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_dcaegen2-services-prh.json)</p>|<p align="center">Project 3</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_dcaegen2-services-sdk.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/dcaegen2-services-sdk) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_dcaegen2-services-sdk) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_dcaegen2-services-sdk.json)</p>
 | |
|<p align="center">Project 4</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_so.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/so) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_so) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_so.json)</p>
# ATDx project report summaries
## Project 1: _onap/dcaegen2-collectors-ves_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_dcaegen2-collectors-ves.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/dcaegen2-collectors-ves) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_dcaegen2-collectors-ves) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_dcaegen2-collectors-ves.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                    | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                  |
|:------------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:----------------------------------------------------------------------------|
| DMaaPPublishersBuilder.java   | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/onap/dcae/common/publishing/DMaaPPublishersBuilder.java   |
| DMaaPConfigurationParser.java | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/onap/dcae/common/publishing/DMaaPConfigurationParser.java |
| ConfigSource.java             | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/onap/dcae/controller/ConfigSource.java                    |
| VESLogger.java                | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/onap/dcae/common/VESLogger.java                           |
| CLIUtils.java                 | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/onap/dcae/CLIUtils.java                                   |
| EnvPropertiesReader.java      | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/onap/dcae/controller/EnvPropertiesReader.java             |
| -                             | -              | -             | -           | -      | -           | -           | -            | -                                                                           |
| -                             | -              | -             | -           | -      | -           | -           | -            | -                                                                           |
| -                             | -              | -             | -           | -      | -           | -           | -            | -                                                                           |
| -                             | -              | -             | -           | -      | -           | -           | -            | -                                                                           |

## Project 2: _onap/dcaegen2-services-prh_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_dcaegen2-services-prh.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/dcaegen2-services-prh) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_dcaegen2-services-prh) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_dcaegen2-services-prh.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                    | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                                            |
|:------------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:------------------------------------------------------------------------------------------------------|
| AaiClientConfiguration.java   | 4              | 0             | 0           | 0      | 2           | 0           | 2            | prh-commons/src/main/java/org/onap/dcaegen2/services/prh/adapter/aai/main/AaiClientConfiguration.java |
| PrhModelAwareGsonBuilder.java | 1              | 0             | 0           | 0      | 1           | 0           | 0            | prh-commons/src/main/java/org/onap/dcaegen2/services/prh/model/utils/PrhModelAwareGsonBuilder.java    |
| -                             | -              | -             | -           | -      | -           | -           | -            | -                                                                                                     |
| -                             | -              | -             | -           | -      | -           | -           | -            | -                                                                                                     |
| -                             | -              | -             | -           | -      | -           | -           | -            | -                                                                                                     |
| -                             | -              | -             | -           | -      | -           | -           | -            | -                                                                                                     |
| -                             | -              | -             | -           | -      | -           | -           | -            | -                                                                                                     |
| -                             | -              | -             | -           | -      | -           | -           | -            | -                                                                                                     |
| -                             | -              | -             | -           | -      | -           | -           | -            | -                                                                                                     |
| -                             | -              | -             | -           | -      | -           | -           | -            | -                                                                                                     |

## Project 3: _onap/dcaegen2-services-sdk_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_dcaegen2-services-sdk.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/dcaegen2-services-sdk) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_dcaegen2-services-sdk) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_dcaegen2-services-sdk.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                  |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                                                                           |
|:----------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------|
| CbsClientConfiguration.java |             10 |             0 |           0 |      0 |           5 |           0 |            5 | rest-services/cbs-client/src/main/java/org/onap/dcaegen2/services/sdk/rest/services/cbs/client/model/CbsClientConfiguration.java                     |
| MdcVariables.java           |              6 |             0 |           0 |      0 |           3 |           0 |            3 | rest-services/http-client/src/main/java/org/onap/dcaegen2/services/sdk/rest/services/adapters/http/logging/MdcVariables.java                         |
| SslFactory.java             |              2 |             0 |           0 |      0 |           1 |           0 |            1 | security/ssl/src/main/java/org/onap/dcaegen2/services/sdk/security/ssl/SslFactory.java                                                               |
| DummyHttpServer.java        |              1 |             0 |           1 |      0 |           0 |           0 |            0 | rest-services/http-client/src/main/java/org/onap/dcaegen2/services/sdk/rest/services/adapters/http/test/DummyHttpServer.java                         |
| DataStreamUtils.java        |              1 |             0 |           0 |      0 |           1 |           0 |            0 | rest-services/cbs-client/src/main/java/org/onap/dcaegen2/services/sdk/rest/services/cbs/client/impl/streams/gson/DataStreamUtils.java                |
| StreamPredicates.java       |              1 |             0 |           0 |      0 |           1 |           0 |            0 | rest-services/cbs-client/src/main/java/org/onap/dcaegen2/services/sdk/rest/services/cbs/client/api/streams/StreamPredicates.java                     |
| CbsRequests.java            |              1 |             0 |           0 |      0 |           1 |           0 |            0 | rest-services/cbs-client/src/main/java/org/onap/dcaegen2/services/sdk/rest/services/cbs/client/api/CbsRequests.java                                  |
| CbsClientFactory.java       |              1 |             0 |           0 |      0 |           1 |           0 |            0 | rest-services/cbs-client/src/main/java/org/onap/dcaegen2/services/sdk/rest/services/cbs/client/api/CbsClientFactory.java                             |
| StreamsConstants.java       |              1 |             0 |           0 |      0 |           1 |           0 |            0 | rest-services/cbs-client/src/main/java/org/onap/dcaegen2/services/sdk/rest/services/cbs/client/impl/streams/gson/StreamsConstants.java               |
| WireFrameEncoder.java       |              1 |             0 |           1 |      0 |           0 |           0 |            0 | services/hv-ves-client/producer/impl/src/main/java/org/onap/dcaegen2/services/sdk/services/hvves/client/producer/impl/encoders/WireFrameEncoder.java |

## Project 4: _onap/so_
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

