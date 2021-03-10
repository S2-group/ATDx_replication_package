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
|<p align="center">Project 1</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_dmaap-messagerouter-dmaapclient.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/dmaap-messagerouter-dmaapclient) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_dmaap-messagerouter-dmaapclient) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_dmaap-messagerouter-dmaapclient.json)</p>|<p align="center">Project 2</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_dmaap-messagerouter-messageservice.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/dmaap-messagerouter-messageservice) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_dmaap-messagerouter-messageservice) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_dmaap-messagerouter-messageservice.json)</p>|<p align="center">Project 3</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_dmaap-messagerouter-mirroragent.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/dmaap-messagerouter-mirroragent) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_dmaap-messagerouter-mirroragent) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_dmaap-messagerouter-mirroragent.json)</p>
 | |
|<p align="center">Project 4</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_dmaap-messagerouter-msgrtr.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/dmaap-messagerouter-msgrtr) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_dmaap-messagerouter-msgrtr) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_dmaap-messagerouter-msgrtr.json)</p>
# ATDx project report summaries
## Project 1: _onap/dmaap-messagerouter-dmaapclient_
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

## Project 2: _onap/dmaap-messagerouter-messageservice_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_dmaap-messagerouter-messageservice.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/dmaap-messagerouter-messageservice) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_dmaap-messagerouter-messageservice) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_dmaap-messagerouter-messageservice.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                    | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                      |
|:------------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:----------------------------------------------------------------|
| MirrorMaker.java              | 5              | 0             | 0           | 0      | 5           | 0           | 0            | src/main/java/org/onap/dmaap/mmagent/MirrorMaker.java           |
| MMRestService.java            | 4              | 0             | 4           | 0      | 0           | 0           | 0            | src/main/java/org/onap/dmaap/service/MMRestService.java         |
| TopicRestService.java         | 2              | 0             | 2           | 0      | 0           | 0           | 0            | src/main/java/org/onap/dmaap/service/TopicRestService.java      |
| ApiKeysRestService.java       | 2              | 0             | 2           | 0      | 0           | 0           | 0            | src/main/java/org/onap/dmaap/service/ApiKeysRestService.java    |
| ServiceUtil.java              | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/onap/dmaap/service/ServiceUtil.java           |
| ServicePropertiesMapBean.java | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/onap/dmaap/util/ServicePropertiesMapBean.java |
| CreateMirrorMaker.java        | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/onap/dmaap/mmagent/CreateMirrorMaker.java     |
| -                             | -              | -             | -           | -      | -           | -           | -            | -                                                               |
| -                             | -              | -             | -           | -      | -           | -           | -            | -                                                               |
| -                             | -              | -             | -           | -      | -           | -           | -            | -                                                               |

## Project 3: _onap/dmaap-messagerouter-mirroragent_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_dmaap-messagerouter-mirroragent.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/dmaap-messagerouter-mirroragent) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_dmaap-messagerouter-mirroragent) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_dmaap-messagerouter-mirroragent.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                     | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                        |
|:-------------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:----------------------------------------------------------------------------------|
| MirrorMaker.java               | 7              | 0             | 0           | 0      | 7           | 0           | 0            | src/main/java/org/onap/dmaap/mr/dmaapMMAgent/dao/MirrorMaker.java                 |
| MirrorMakerProcessHandler.java | 3              | 1             | 1           | 0      | 1           | 0           | 0            | src/main/java/org/onap/dmaap/mr/dmaapMMAgent/utils/MirrorMakerProcessHandler.java |
| MirrorMakerAgent.java          | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/onap/dmaap/mr/dmaapMMAgent/MirrorMakerAgent.java                |
| -                              | -              | -             | -           | -      | -           | -           | -            | -                                                                                 |
| -                              | -              | -             | -           | -      | -           | -           | -            | -                                                                                 |
| -                              | -              | -             | -           | -      | -           | -           | -            | -                                                                                 |
| -                              | -              | -             | -           | -      | -           | -           | -            | -                                                                                 |
| -                              | -              | -             | -           | -      | -           | -           | -            | -                                                                                 |
| -                              | -              | -             | -           | -      | -           | -           | -            | -                                                                                 |
| -                              | -              | -             | -           | -      | -           | -           | -            | -                                                                                 |

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

