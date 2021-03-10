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
|||
|-|-|
|<p align="center">Project 1</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_plc4x.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/plc4x) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_plc4x) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_plc4x.json)</p>|<p align="center">Project 2</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-distribution-journal.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-distribution-journal) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-distribution-journal) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-distribution-journal.json)</p>
# ATDx project report summaries
## Project 1: _apache/plc4x_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_plc4x.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/plc4x) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_plc4x) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_plc4x.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                      |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                                                                   |
|:--------------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:---------------------------------------------------------------------------------------------------------------------------------------------|
| LittleEndianDecoder.java        |             39 |             0 |           0 |      0 |           0 |           0 |           39 | sandbox/test-java-amsads-driver/src/main/java/org/apache/plc4x/java/amsads/protocol/util/LittleEndianDecoder.java                            |
| JavaLanguageTemplateHelper.java |             38 |             0 |          10 |      0 |           0 |           0 |           28 | build-utils/language-java/src/main/java/org/apache/plc4x/language/java/JavaLanguageTemplateHelper.java                                       |
| TriggerConfiguration.java       |             12 |             0 |          12 |      0 |           0 |           0 |            0 | plc4j/tools/scraper/src/main/java/org/apache/plc4x/java/scraper/triggeredscraper/triggerhandler/TriggerConfiguration.java                    |
| DriverTestsuiteRunner.java      |              8 |             0 |           1 |      0 |           0 |           0 |            7 | plc4j/utils/test-utils/src/main/java/org/apache/plc4x/test/driver/DriverTestsuiteRunner.java                                                 |
| S7Step7ServerAdapter.java       |              7 |             0 |           0 |      0 |           0 |           0 |            7 | sandbox/plc-simulator/src/main/java/org/apache/plc4x/simulator/server/s7/protocol/S7Step7ServerAdapter.java                                  |
| Df1Protocol.java                |              6 |             0 |           0 |      0 |           1 |           0 |            5 | sandbox/test-java-df1-driver/src/main/java/org/apache/plc4x/java/df1/protocol/Df1Protocol.java                                               |
| SerialChannel.java              |              6 |             0 |           6 |      0 |           0 |           0 |            0 | plc4j/transports/serial/src/main/java/org/apache/plc4x/java/transport/serial/SerialChannel.java                                              |
| Plc4xEmbeddedChannel.java       |              6 |             0 |           2 |      0 |           2 |           0 |            2 | plc4j/transports/test/src/main/java/io/netty/channel/embedded/Plc4xEmbeddedChannel.java                                                      |
| ExpressionStringListener.java   |              5 |             0 |           5 |      0 |           0 |           0 |            0 | build-utils/protocol-base-mspec/src/main/java/org/apache/plc4x/plugins/codegenerator/language/mspec/expression/ExpressionStringListener.java |
| WaterTankService.java           |              5 |             0 |           5 |      0 |           0 |           0 |            0 | plc4j/examples/hello-webapp/webapp/src/main/java/org/apache/plc4x/examples/watertank/service/WaterTankService.java                           |

## Project 2: _apache/sling-org-apache-sling-distribution-journal_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-distribution-journal.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-distribution-journal) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-distribution-journal) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-distribution-journal.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                 |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                    |
|:---------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:----------------------------------------------------------------------------------------------|
| LocalStore.java            |              3 |             0 |           3 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/distribution/journal/impl/subscriber/LocalStore.java           |
| DistributionPublisher.java |              2 |             0 |           2 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/distribution/journal/impl/publisher/DistributionPublisher.java |
| PubQueueCache.java         |              2 |             0 |           2 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/distribution/journal/impl/queue/impl/PubQueueCache.java        |
| JMXRegistration.java       |              2 |             0 |           2 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/distribution/journal/impl/shared/JMXRegistration.java          |
| PackageRepo.java           |              1 |             0 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/distribution/journal/impl/publisher/PackageRepo.java           |
| BookKeeper.java            |              1 |             0 |           0 |      0 |           1 |           0 |            0 | src/main/java/org/apache/sling/distribution/journal/impl/subscriber/BookKeeper.java           |
| LimitPoller.java           |              1 |             0 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/distribution/journal/impl/shared/LimitPoller.java              |
| PackageMessageFactory.java |              1 |             0 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/distribution/journal/impl/publisher/PackageMessageFactory.java |
| Announcer.java             |              1 |             0 |           0 |      0 |           1 |           0 |            0 | src/main/java/org/apache/sling/distribution/journal/impl/subscriber/Announcer.java            |
| PubQueueCacheService.java  |              1 |             0 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/distribution/journal/impl/queue/impl/PubQueueCacheService.java |

