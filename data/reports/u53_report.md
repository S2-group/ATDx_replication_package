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
|<p align="center">Project 1</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_ccsdk-sli-adaptors.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/ccsdk-sli-adaptors) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_ccsdk-sli-adaptors) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_ccsdk-sli-adaptors.json)</p>|<p align="center">Project 2</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_ccsdk-sli-core.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/ccsdk-sli-core) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_ccsdk-sli-core) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_ccsdk-sli-core.json)</p>|<p align="center">Project 3</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_ccsdk-sli-plugins.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/ccsdk-sli-plugins) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_ccsdk-sli-plugins) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_ccsdk-sli-plugins.json)</p>
 | |
|<p align="center">Project 4</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_logging-analytics.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/logging-analytics) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_logging-analytics) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_logging-analytics.json)</p>|<p align="center">Project 5</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_sdnc-northbound.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/sdnc-northbound) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_sdnc-northbound) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_sdnc-northbound.json)</p>
# ATDx project report summaries
## Project 1: _onap/ccsdk-sli-adaptors_
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

## Project 2: _onap/ccsdk-sli-core_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_ccsdk-sli-core.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/ccsdk-sli-core) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_ccsdk-sli-core) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_ccsdk-sli-core.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name               |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                       |
|:-------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:-------------------------------------------------------------------------------------------------|
| MdsalHelper.java         |             11 |             0 |           0 |      0 |           6 |           0 |            5 | sli/provider/src/main/java/org/onap/ccsdk/sli/core/sli/provider/MdsalHelper.java                 |
| MetricLogger.java        |              6 |             0 |           0 |      0 |           3 |           0 |            3 | sli/common/src/main/java/org/onap/ccsdk/sli/core/sli/MetricLogger.java                           |
| MessageWriter.java       |              4 |             0 |           0 |      0 |           2 |           1 |            1 | sli/common/src/main/java/org/onap/ccsdk/sli/core/sli/MessageWriter.java                          |
| SvcLogicContext.java     |              4 |             0 |           0 |      0 |           2 |           0 |            2 | sli/common/src/main/java/org/onap/ccsdk/sli/core/sli/SvcLogicContext.java                        |
| SliPluginUtils.java      |              3 |             0 |           1 |      0 |           1 |           0 |            1 | sliPluginUtils/provider/src/main/java/org/onap/ccsdk/sli/core/slipluginutils/SliPluginUtils.java |
| DBConfigFactory.java     |              3 |             0 |           2 |      0 |           1 |           0 |            0 | dblib/provider/src/main/java/org/onap/ccsdk/sli/core/dblib/factory/DBConfigFactory.java          |
| SliStringUtils.java      |              3 |             0 |           3 |      0 |           0 |           0 |            0 | sliPluginUtils/provider/src/main/java/org/onap/ccsdk/sli/core/slipluginutils/SliStringUtils.java |
| SvcLogicServiceImpl.java |              3 |             0 |           1 |      0 |           1 |           0 |            1 | sli/provider/src/main/java/org/onap/ccsdk/sli/core/sli/provider/SvcLogicServiceImpl.java         |
| BaseDBConfiguration.java |              3 |             0 |           3 |      0 |           0 |           0 |            0 | dblib/provider/src/main/java/org/onap/ccsdk/sli/core/dblib/config/BaseDBConfiguration.java       |
| PrintYangToProp.java     |              2 |             0 |           0 |      0 |           2 |           0 |            0 | sli/provider/src/main/java/org/onap/ccsdk/sli/core/sli/provider/PrintYangToProp.java             |

## Project 3: _onap/ccsdk-sli-plugins_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_ccsdk-sli-plugins.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/ccsdk-sli-plugins) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_ccsdk-sli-plugins) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_ccsdk-sli-plugins.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name              |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                                         |
|:------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:-------------------------------------------------------------------------------------------------------------------|
| Parameters.java         |             31 |             0 |           0 |      0 |          31 |           0 |            0 | restapi-call-node/provider/src/main/java/org/onap/ccsdk/sli/plugins/restapicall/Parameters.java                    |
| RestapiCallNode.java    |             17 |             0 |           0 |      0 |          17 |           0 |            0 | restapi-call-node/provider/src/main/java/org/onap/ccsdk/sli/plugins/restapicall/RestapiCallNode.java               |
| Parameters.java         |             15 |             0 |           0 |      0 |          15 |           0 |            0 | sshapi-call-node/provider/src/main/java/org/onap/ccsdk/sli/plugins/sshapicall/model/Parameters.java                |
| GrToolkitProvider.java  |              6 |             0 |           0 |      0 |           3 |           0 |            3 | grToolkit/provider/src/main/java/org/onap/ccsdk/sli/plugins/grtoolkit/GrToolkitProvider.java                       |
| HttpResponse.java       |              5 |             0 |           0 |      0 |           5 |           0 |            0 | restapi-call-node/provider/src/main/java/org/onap/ccsdk/sli/plugins/restapicall/HttpResponse.java                  |
| Parameters.java         |              4 |             0 |           0 |      0 |           4 |           0 |            0 | properties-node/provider/src/main/java/org/onap/ccsdk/sli/plugins/prop/Parameters.java                             |
| ConnectionResponse.java |              2 |             0 |           0 |      0 |           2 |           0 |            0 | grToolkit/provider/src/main/java/org/onap/ccsdk/sli/plugins/grtoolkit/connection/ConnectionResponse.java           |
| ParseParam.java         |              2 |             0 |           2 |      0 |           0 |           0 |            0 | sshapi-call-node/provider/src/main/java/org/onap/ccsdk/sli/plugins/sshapicall/model/ParseParam.java                |
| RetryPolicy.java        |              1 |             0 |           1 |      0 |           0 |           0 |            0 | restapi-call-node/provider/src/main/java/org/onap/ccsdk/sli/plugins/restapicall/RetryPolicy.java                   |
| YangParameters.java     |              1 |             0 |           0 |      0 |           1 |           0 |            0 | restconf-client/provider/src/main/java/org/onap/ccsdk/sli/plugins/yangserializers/dfserializer/YangParameters.java |

## Project 4: _onap/logging-analytics_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_logging-analytics.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/logging-analytics) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_logging-analytics) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_logging-analytics.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                         | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                                                                 |
|:-----------------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:---------------------------------------------------------------------------------------------------------------------------|
| Constants.java                     | 4              | 0             | 0           | 0      | 4           | 0           | 0            | reference/logging-filter/logging-filter-base/src/main/java/org/onap/logging/filter/base/Constants.java                     |
| FilteredMetricLogClientFilter.java | 4              | 4             | 0           | 0      | 0           | 0           | 0            | reference/logging-filter/logging-filter-base/src/main/java/org/onap/logging/filter/base/FilteredMetricLogClientFilter.java |
| AbstractMDCSetupAspect.java        | 1              | 0             | 1           | 0      | 0           | 0           | 0            | reference/logging-filter/logging-filter-base/src/main/java/org/onap/logging/filter/base/AbstractMDCSetupAspect.java        |
| ScheduledTaskException.java        | 1              | 0             | 1           | 0      | 0           | 0           | 0            | reference/logging-filter/logging-filter-base/src/main/java/org/onap/logging/filter/base/ScheduledTaskException.java        |
| SLF4JRefApplication.java           | 1              | 0             | 1           | 0      | 0           | 0           | 0            | reference/logging-slf4j-demo/src/main/java/org/onap/logging/ref/slf4j/demo/SLF4JRefApplication.java                        |
| SpringClientPayloadFilter.java     | 1              | 0             | 1           | 0      | 0           | 0           | 0            | reference/logging-filter/logging-filter-spring/src/main/java/org/onap/logging/filter/spring/SpringClientPayloadFilter.java |
| PayloadLoggingClientFilter.java    | 1              | 0             | 1           | 0      | 0           | 0           | 0            | reference/logging-filter/logging-filter-base/src/main/java/org/onap/logging/filter/base/PayloadLoggingClientFilter.java    |
| -                                  | -              | -             | -           | -      | -           | -           | -            | -                                                                                                                          |
| -                                  | -              | -             | -           | -      | -           | -           | -            | -                                                                                                                          |
| -                                  | -              | -             | -           | -      | -           | -           | -            | -                                                                                                                          |

## Project 5: _onap/sdnc-northbound_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_sdnc-northbound.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/sdnc-northbound) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_sdnc-northbound) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_sdnc-northbound.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                      | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                                           |
|:--------------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:-----------------------------------------------------------------------------------------------------|
| GenericResourceApiProvider.java | 2              | 0             | 1           | 0      | 0           | 1           | 0            | generic-resource-api/provider/src/main/java/org/onap/sdnc/northbound/GenericResourceApiProvider.java |
| VnfApiProvider.java             | 1              | 0             | 0           | 0      | 0           | 1           | 0            | vnfapi/provider/src/main/java/org/onap/sdnc/vnfapi/VnfApiProvider.java                               |
| -                               | -              | -             | -           | -      | -           | -           | -            | -                                                                                                    |
| -                               | -              | -             | -           | -      | -           | -           | -            | -                                                                                                    |
| -                               | -              | -             | -           | -      | -           | -           | -            | -                                                                                                    |
| -                               | -              | -             | -           | -      | -           | -           | -            | -                                                                                                    |
| -                               | -              | -             | -           | -      | -           | -           | -            | -                                                                                                    |
| -                               | -              | -             | -           | -      | -           | -           | -            | -                                                                                                    |
| -                               | -              | -             | -           | -      | -           | -           | -            | -                                                                                                    |
| -                               | -              | -             | -           | -      | -           | -           | -            | -                                                                                                    |

