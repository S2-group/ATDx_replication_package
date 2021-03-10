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
|<p align="center">Project 1</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/JMeter.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/jmeter) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=JMeter) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/JMeter.json)</p>|<p align="center">Project 2</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/commons-compress.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/commons-compress) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=commons-compress) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/commons-compress.json)</p>
# ATDx project report summaries
## Project 1: _apache/jmeter_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/JMeter.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/jmeter) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=JMeter) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/JMeter.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                     |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                        |
|:-------------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:--------------------------------------------------------------------------------------------------|
| LoggingManager.java            |             32 |             0 |           0 |      0 |          16 |           0 |           16 | src/jorphan/src/main/java/org/apache/jorphan/logging/LoggingManager.java                          |
| SampleResult.java              |             20 |             1 |           0 |      1 |           9 |           0 |            9 | src/core/src/main/java/org/apache/jmeter/samplers/SampleResult.java                               |
| Logger.java                    |             20 |             0 |           0 |      0 |          10 |           0 |           10 | src/jorphan/src/main/java/org/apache/log/Logger.java                                              |
| JMeterUtils.java               |             11 |             0 |           5 |      0 |           3 |           0 |            3 | src/core/src/main/java/org/apache/jmeter/util/JMeterUtils.java                                    |
| PreciseThroughputTimer.java    |             10 |             1 |           0 |      1 |           4 |           0 |            4 | src/components/src/main/java/org/apache/jmeter/timers/poissonarrivals/PreciseThroughputTimer.java |
| JMeterContext.java             |              8 |             0 |           0 |      0 |           4 |           0 |            4 | src/core/src/main/java/org/apache/jmeter/threads/JMeterContext.java                               |
| HTTPSamplerBase.java           |              8 |             0 |           0 |      0 |           4 |           0 |            4 | src/protocol/http/src/main/java/org/apache/jmeter/protocol/http/sampler/HTTPSamplerBase.java      |
| HTTPAbstractImpl.java          |              8 |             0 |           0 |      0 |           4 |           0 |            4 | src/protocol/http/src/main/java/org/apache/jmeter/protocol/http/sampler/HTTPAbstractImpl.java     |
| XMLDefaultMutableTreeNode.java |              6 |             0 |           4 |      0 |           1 |           0 |            1 | src/components/src/main/java/org/apache/jmeter/visualizers/XMLDefaultMutableTreeNode.java         |
| JTextScrollPane.java           |              6 |             0 |           0 |      0 |           3 |           0 |            3 | src/core/src/main/java/org/apache/jmeter/gui/util/JTextScrollPane.java                            |

## Project 2: _apache/commons-compress_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/commons-compress.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/commons-compress) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=commons-compress) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/commons-compress.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                       |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                   |
|:---------------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:---------------------------------------------------------------------------------------------|
| SevenZFile.java                  |             20 |             0 |           3 |      0 |           3 |           0 |           14 | src/main/java/org/apache/commons/compress/archivers/sevenz/SevenZFile.java                   |
| Charsets.java                    |             13 |             0 |           0 |      0 |           7 |           0 |            6 | src/main/java/org/apache/commons/compress/utils/Charsets.java                                |
| TarArchiveOutputStream.java      |              9 |             0 |           1 |      0 |           4 |           0 |            4 | src/main/java/org/apache/commons/compress/archivers/tar/TarArchiveOutputStream.java          |
| SevenZArchiveEntry.java          |              8 |             0 |           0 |      0 |           4 |           0 |            4 | src/main/java/org/apache/commons/compress/archivers/sevenz/SevenZArchiveEntry.java           |
| TarArchiveEntry.java             |              7 |             0 |           0 |      0 |           2 |           0 |            5 | src/main/java/org/apache/commons/compress/archivers/tar/TarArchiveEntry.java                 |
| Expander.java                    |              6 |             0 |           0 |      0 |           3 |           0 |            3 | src/main/java/org/apache/commons/compress/archivers/examples/Expander.java                   |
| JarArchiveEntry.java             |              4 |             0 |           0 |      0 |           2 |           0 |            2 | src/main/java/org/apache/commons/compress/archivers/jar/JarArchiveEntry.java                 |
| Archiver.java                    |              4 |             0 |           0 |      0 |           2 |           0 |            2 | src/main/java/org/apache/commons/compress/archivers/examples/Archiver.java                   |
| ZipArchiveEntry.java             |              3 |             1 |           1 |      1 |           0 |           0 |            0 | src/main/java/org/apache/commons/compress/archivers/zip/ZipArchiveEntry.java                 |
| BZip2CompressorOutputStream.java |              3 |             1 |           0 |      0 |           0 |           0 |            2 | src/main/java/org/apache/commons/compress/compressors/bzip2/BZip2CompressorOutputStream.java |

