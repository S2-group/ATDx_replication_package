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
|<p align="center">Project 1</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_cli.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/cli) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_cli) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_cli.json)</p>|<p align="center">Project 2</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_vfc-nfvo-driver-ems.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/vfc-nfvo-driver-ems) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_vfc-nfvo-driver-ems) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_vfc-nfvo-driver-ems.json)</p>|<p align="center">Project 3</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_vfc-nfvo-driver-sfc.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/vfc-nfvo-driver-sfc) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_vfc-nfvo-driver-sfc) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_vfc-nfvo-driver-sfc.json)</p>
 | |
|<p align="center">Project 4</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_vfc-nfvo-multivimproxy.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/vfc-nfvo-multivimproxy) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_vfc-nfvo-multivimproxy) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_vfc-nfvo-multivimproxy.json)</p>|<p align="center">Project 5</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_vfc-nfvo-resmanagement.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/vfc-nfvo-resmanagement) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_vfc-nfvo-resmanagement) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_vfc-nfvo-resmanagement.json)</p>
# ATDx project report summaries
## Project 1: _onap/cli_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_cli.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/cli) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_cli) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_cli.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                           |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                 |
|:-------------------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:-------------------------------------------------------------------------------------------|
| OpenRemoteCli.java                   |              4 |             0 |           4 |      0 |           0 |           0 |            0 | grpc/grpc-client/src/main/java/org/open/infc/grpc/client/OpenRemoteCli.java                |
| OnapCommand.java                     |              3 |             0 |           3 |      0 |           0 |           0 |            0 | framework/src/main/java/org/onap/cli/fw/cmd/OnapCommand.java                               |
| OnapCommandArtifactStore.java        |              2 |             0 |           2 |      0 |           0 |           0 |            0 | framework/src/main/java/org/onap/cli/fw/store/OnapCommandArtifactStore.java                |
| OnapCommandDiscoveryUtils.java       |              2 |             0 |           1 |      0 |           1 |           0 |            0 | framework/src/main/java/org/onap/cli/fw/utils/OnapCommandDiscoveryUtils.java               |
| OpenInterfaceGrpcClient.java         |              2 |             0 |           2 |      0 |           0 |           0 |            0 | grpc/grpc-client/src/main/java/org/open/infc/grpc/client/OpenInterfaceGrpcClient.java      |
| OnapCommandSchemaSnmpLoader.java     |              2 |             0 |           1 |      0 |           1 |           0 |            0 | profiles/snmp/src/main/java/org/onap/cli/fw/snmp/schema/OnapCommandSchemaSnmpLoader.java   |
| OnapCommandSchemaCmdLoader.java      |              1 |             0 |           1 |      0 |           0 |           0 |            0 | profiles/command/src/main/java/org/onap/cli/fw/cmd/schema/OnapCommandSchemaCmdLoader.java  |
| ProcessRunner.java                   |              1 |             0 |           1 |      0 |           0 |           0 |            0 | framework/src/main/java/org/onap/cli/fw/utils/ProcessRunner.java                           |
| OnapCommandExceutionShowCommand.java |              1 |             0 |           1 |      0 |           0 |           0 |            0 | framework/src/main/java/org/onap/cli/fw/cmd/execution/OnapCommandExceutionShowCommand.java |
| MockResponse.java                    |              1 |             0 |           1 |      0 |           0 |           0 |            0 | validate/sample-mock-generator/src/main/java/org/onap/cli/http/mock/MockResponse.java      |

## Project 2: _onap/vfc-nfvo-driver-ems_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_vfc-nfvo-driver-ems.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/vfc-nfvo-driver-ems) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_vfc-nfvo-driver-ems) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_vfc-nfvo-driver-ems.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name               |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                  |
|:-------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:--------------------------------------------------------------------------------------------|
| MsgType.java             |              3 |             0 |           0 |      0 |           3 |           0 |            0 | ems/boco/src/main/java/org/onap/vfc/nfvo/emsdriver/collector/alarm/MsgType.java             |
| HttpClientFactory.java   |              1 |             0 |           0 |      0 |           1 |           0 |            0 | ems/boco/src/main/java/org/onap/vfc/nfvo/emsdriver/northbound/client/HttpClientFactory.java |
| QuartzManager.java       |              1 |             0 |           0 |      0 |           1 |           0 |            0 | ems/boco/src/main/java/org/onap/vfc/nfvo/emsdriver/taskscheduler/QuartzManager.java         |
| TaskThread.java          |              1 |             0 |           0 |      0 |           1 |           0 |            0 | ems/boco/src/main/java/org/onap/vfc/nfvo/emsdriver/collector/TaskThread.java                |
| MsbConfiguration.java    |              1 |             0 |           0 |      0 |           1 |           0 |            0 | ems/boco/src/main/java/org/onap/vfc/nfvo/emsdriver/serviceregister/MsbConfiguration.java    |
| MsbRestServiceProxy.java |              1 |             0 |           0 |      0 |           1 |           0 |            0 | ems/boco/src/main/java/org/onap/vfc/nfvo/emsdriver/serviceregister/MsbRestServiceProxy.java |
| XmlUtil.java             |              1 |             0 |           0 |      0 |           1 |           0 |            0 | ems/boco/src/main/java/org/onap/vfc/nfvo/emsdriver/commons/utils/XmlUtil.java               |
| VarExprParser.java       |              1 |             0 |           0 |      0 |           1 |           0 |            0 | ems/boco/src/main/java/org/onap/vfc/nfvo/emsdriver/commons/utils/VarExprParser.java         |
| HttpClientUtil.java      |              1 |             0 |           0 |      0 |           1 |           0 |            0 | ems/boco/src/main/java/org/onap/vfc/nfvo/emsdriver/northbound/client/HttpClientUtil.java    |
| MessageChannel.java      |              1 |             0 |           1 |      0 |           0 |           0 |            0 | ems/boco/src/main/java/org/onap/vfc/nfvo/emsdriver/messagemgr/MessageChannel.java           |

## Project 3: _onap/vfc-nfvo-driver-sfc_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_vfc-nfvo-driver-sfc.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/vfc-nfvo-driver-sfc) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_vfc-nfvo-driver-sfc) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_vfc-nfvo-driver-sfc.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name              | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                            |
|:------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:----------------------------------------------------------------------|
| DriverResource.java     | 8              | 0             | 8           | 0      | 0           | 0           | 0            | sfc-driver/src/main/java/org/onap/sfc/resources/DriverResource.java   |
| SdnServiceConsumer.java | 3              | 0             | 2           | 0      | 1           | 0           | 0            | sfc-driver/src/main/java/org/onap/sfc/service/SdnServiceConsumer.java |
| N2sReqWrapper.java      | 1              | 0             | 0           | 0      | 1           | 0           | 0            | sfc-driver/src/main/java/org/onap/sfc/wrapper/N2sReqWrapper.java      |
| ConfigInfo.java         | 1              | 0             | 0           | 0      | 1           | 0           | 0            | sfc-driver/src/main/java/org/onap/sfc/service/ConfigInfo.java         |
| SfcDriverUtil.java      | 1              | 0             | 0           | 0      | 1           | 0           | 0            | sfc-driver/src/main/java/org/onap/sfc/utils/SfcDriverUtil.java        |
| -                       | -              | -             | -           | -      | -           | -           | -            | -                                                                     |
| -                       | -              | -             | -           | -      | -           | -           | -            | -                                                                     |
| -                       | -              | -             | -           | -      | -           | -           | -            | -                                                                     |
| -                       | -              | -             | -           | -      | -           | -           | -            | -                                                                     |
| -                       | -              | -             | -           | -      | -           | -           | -            | -                                                                     |

## Project 4: _onap/vfc-nfvo-multivimproxy_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_vfc-nfvo-multivimproxy.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/vfc-nfvo-multivimproxy) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_vfc-nfvo-multivimproxy) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_vfc-nfvo-multivimproxy.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name            | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                                         |
|:----------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:---------------------------------------------------------------------------------------------------|
| ServiceException.java | 4              | 0             | 4           | 0      | 0           | 0           | 0            | service/src/main/java/org/onap/vfc/nfvo/multivimproxy/common/util/restclient/ServiceException.java |
| -                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                                  |
| -                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                                  |
| -                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                                  |
| -                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                                  |
| -                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                                  |
| -                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                                  |
| -                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                                  |
| -                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                                  |
| -                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                                  |

## Project 5: _onap/vfc-nfvo-resmanagement_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_vfc-nfvo-resmanagement.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/vfc-nfvo-resmanagement) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_vfc-nfvo-resmanagement) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_vfc-nfvo-resmanagement.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                                                                 |
|:--------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:---------------------------------------------------------------------------------------------------------------------------|
| ServiceException.java     | 3              | 0             | 3           | 0      | 0           | 0           | 0            | ResmanagementService/service/src/main/java/org/onap/vfc/nfvo/resmanagement/common/util/restclient/ServiceException.java    |
| SitesRoa.java             | 2              | 0             | 2           | 0      | 0           | 0           | 0            | ResmanagementService/service/src/main/java/org/onap/vfc/nfvo/resmanagement/service/rest/SitesRoa.java                      |
| LocationBusinessImpl.java | 1              | 0             | 1           | 0      | 0           | 0           | 0            | ResmanagementService/service/src/main/java/org/onap/vfc/nfvo/resmanagement/service/business/impl/LocationBusinessImpl.java |
| NsRoa.java                | 1              | 0             | 1           | 0      | 0           | 0           | 0            | ResmanagementService/service/src/main/java/org/onap/vfc/nfvo/resmanagement/service/rest/NsRoa.java                         |
| VnfRoa.java               | 1              | 0             | 1           | 0      | 0           | 0           | 0            | ResmanagementService/service/src/main/java/org/onap/vfc/nfvo/resmanagement/service/rest/VnfRoa.java                        |
| VmServiceImpl.java        | 1              | 0             | 1           | 0      | 0           | 0           | 0            | ResmanagementService/service/src/main/java/org/onap/vfc/nfvo/resmanagement/service/group/impl/VmServiceImpl.java           |
| -                         | -              | -             | -           | -      | -           | -           | -            | -                                                                                                                          |
| -                         | -              | -             | -           | -      | -           | -           | -            | -                                                                                                                          |
| -                         | -              | -             | -           | -      | -           | -           | -            | -                                                                                                                          |
| -                         | -              | -             | -           | -      | -           | -           | -            | -                                                                                                                          |

