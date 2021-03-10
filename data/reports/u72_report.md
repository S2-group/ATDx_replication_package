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
|<p align="center">Project 1</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_aai-schema-service.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/aai-schema-service) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_aai-schema-service) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_aai-schema-service.json)</p>|<p align="center">Project 2</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_holmes-common.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/holmes-common) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_holmes-common) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_holmes-common.json)</p>|<p align="center">Project 3</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_holmes-rule-management.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/holmes-rule-management) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_holmes-rule-management) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_holmes-rule-management.json)</p>
 | |
|<p align="center">Project 4</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_sdnc-northbound.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/sdnc-northbound) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_sdnc-northbound) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_sdnc-northbound.json)</p>
# ATDx project report summaries
## Project 1: _onap/aai-schema-service_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_aai-schema-service.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/aai-schema-service) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_aai-schema-service) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_aai-schema-service.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                    |
|:--------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:----------------------------------------------------------------------------------------------|
| XSDElement.java           |             24 |             0 |          24 |      0 |           0 |           0 |            0 | aai-schema-gen/src/main/java/org/onap/aai/schemagen/genxsd/XSDElement.java                    |
| NodesYAMLfromOXM.java     |             11 |             8 |           2 |      0 |           1 |           0 |            0 | aai-schema-gen/src/main/java/org/onap/aai/schemagen/genxsd/NodesYAMLfromOXM.java              |
| YAMLfromOXM.java          |             11 |             8 |           2 |      0 |           1 |           0 |            0 | aai-schema-gen/src/main/java/org/onap/aai/schemagen/genxsd/YAMLfromOXM.java                   |
| HTMLfromOXM.java          |              4 |             3 |           1 |      0 |           0 |           0 |            0 | aai-schema-gen/src/main/java/org/onap/aai/schemagen/genxsd/HTMLfromOXM.java                   |
| GenerateSwagger.java      |              2 |             0 |           1 |      0 |           1 |           0 |            0 | aai-schema-gen/src/main/java/org/onap/aai/schemagen/swagger/GenerateSwagger.java              |
| SchemaServiceApp.java     |              2 |             0 |           2 |      0 |           0 |           0 |            0 | aai-schema-service/src/main/java/org/onap/aai/schemaservice/SchemaServiceApp.java             |
| AuthorizationService.java |              2 |             0 |           2 |      0 |           0 |           0 |            0 | aai-schema-service/src/main/java/org/onap/aai/schemaservice/service/AuthorizationService.java |
| GenerateXsd.java          |              2 |             0 |           1 |      0 |           1 |           0 |            0 | aai-schema-gen/src/main/java/org/onap/aai/schemagen/GenerateXsd.java                          |
| OxmFileProcessor.java     |              2 |             0 |           2 |      0 |           0 |           0 |            0 | aai-schema-gen/src/main/java/org/onap/aai/schemagen/genxsd/OxmFileProcessor.java              |
| SpringContextAware.java   |              1 |             0 |           1 |      0 |           0 |           0 |            0 | aai-schema-gen/src/main/java/org/onap/aai/schemagen/SpringContextAware.java                   |

## Project 2: _onap/holmes-common_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_holmes-common.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/holmes-common) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_holmes-common) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_holmes-common.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                         |
|:--------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:---------------------------------------------------------------------------------------------------|
| VesAlarm.java             |              3 |             2 |           0 |      1 |           0 |           0 |            0 | holmes-actions/src/main/java/org/onap/holmes/common/api/stat/VesAlarm.java                         |
| AaiConfig.java            |              3 |             0 |           0 |      0 |           3 |           0 |            0 | holmes-actions/src/main/java/org/onap/holmes/common/aai/config/AaiConfig.java                      |
| CorrelationRule.java      |              2 |             1 |           0 |      1 |           0 |           0 |            0 | holmes-actions/src/main/java/org/onap/holmes/common/api/entity/CorrelationRule.java                |
| Alarm.java                |              2 |             1 |           0 |      1 |           0 |           0 |            0 | holmes-actions/src/main/java/org/onap/holmes/common/api/stat/Alarm.java                            |
| MicroServiceConfig.java   |              1 |             0 |           0 |      0 |           1 |           0 |            0 | holmes-actions/src/main/java/org/onap/holmes/common/config/MicroServiceConfig.java                 |
| AaiQuery4Ccvpn.java       |              1 |             0 |           1 |      0 |           0 |           0 |            0 | holmes-actions/src/main/java/org/onap/holmes/common/aai/AaiQuery4Ccvpn.java                        |
| ServiceLocatorHolder.java |              1 |             0 |           0 |      0 |           1 |           0 |            0 | holmes-actions/src/main/java/org/onap/holmes/common/dropwizard/ioc/utils/ServiceLocatorHolder.java |
| DroolsLog.java            |              1 |             0 |           0 |      0 |           1 |           0 |            0 | holmes-actions/src/main/java/org/onap/holmes/common/utils/DroolsLog.java                           |
| GsonUtil.java             |              1 |             0 |           1 |      0 |           0 |           0 |            0 | holmes-actions/src/main/java/org/onap/holmes/common/utils/GsonUtil.java                            |
| HttpsUtils.java           |              1 |             0 |           0 |      0 |           1 |           0 |            0 | holmes-actions/src/main/java/org/onap/holmes/common/utils/HttpsUtils.java                          |

## Project 3: _onap/holmes-rule-management_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_holmes-rule-management.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/holmes-rule-management) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_holmes-rule-management) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_holmes-rule-management.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name              | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                       |
|:------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:---------------------------------------------------------------------------------|
| EngineService.java      | 3              | 0             | 3           | 0      | 0           | 0           | 0            | rulemgt/src/main/java/org/onap/holmes/rulemgt/bolt/enginebolt/EngineService.java |
| MsbQuery.java           | 2              | 0             | 2           | 0      | 0           | 0           | 0            | rulemgt/src/main/java/org/onap/holmes/rulemgt/msb/MsbQuery.java                  |
| RuleMgtWrapper.java     | 2              | 0             | 2           | 0      | 0           | 0           | 0            | rulemgt/src/main/java/org/onap/holmes/rulemgt/wrapper/RuleMgtWrapper.java        |
| RuleQueryWrapper.java   | 2              | 0             | 2           | 0      | 0           | 0           | 0            | rulemgt/src/main/java/org/onap/holmes/rulemgt/wrapper/RuleQueryWrapper.java      |
| EngineInsQueryTool.java | 1              | 0             | 1           | 0      | 0           | 0           | 0            | rulemgt/src/main/java/org/onap/holmes/rulemgt/msb/EngineInsQueryTool.java        |
| RuleAllocator.java      | 1              | 0             | 1           | 0      | 0           | 0           | 0            | rulemgt/src/main/java/org/onap/holmes/rulemgt/send/RuleAllocator.java            |
| -                       | -              | -             | -           | -      | -           | -           | -            | -                                                                                |
| -                       | -              | -             | -           | -      | -           | -           | -            | -                                                                                |
| -                       | -              | -             | -           | -      | -           | -           | -            | -                                                                                |
| -                       | -              | -             | -           | -      | -           | -           | -            | -                                                                                |

## Project 4: _onap/sdnc-northbound_
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

