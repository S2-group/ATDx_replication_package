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
|<p align="center">Project 1</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_dmaap-datarouter.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/dmaap-datarouter) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_dmaap-datarouter) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_dmaap-datarouter.json)</p>|<p align="center">Project 2</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_externalapi-nbi.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/externalapi-nbi) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_externalapi-nbi) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_externalapi-nbi.json)</p>|<p align="center">Project 3</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_music.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/onap/music) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_music) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_music.json)</p>
 | |

# ATDx project report summaries
## Project 1: _onap/dmaap-datarouter_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_dmaap-datarouter.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/dmaap-datarouter) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_dmaap-datarouter) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_dmaap-datarouter.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name         | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                                    |
|:-------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:----------------------------------------------------------------------------------------------|
| StatusLog.java     | 4              | 0             | 0           | 0      | 4           | 0           | 0            | datarouter-node/src/main/java/org/onap/dmaap/datarouter/node/StatusLog.java                   |
| RLEBitSet.java     | 3              | 2             | 0           | 1      | 0           | 0           | 0            | datarouter-prov/src/main/java/org/onap/dmaap/datarouter/provisioning/utils/RLEBitSet.java     |
| LOGJSONObject.java | 3              | 2             | 0           | 1      | 0           | 0           | 0            | datarouter-prov/src/main/java/org/onap/dmaap/datarouter/provisioning/utils/LOGJSONObject.java |
| NodeConfig.java    | 1              | 0             | 0           | 0      | 1           | 0           | 0            | datarouter-node/src/main/java/org/onap/dmaap/datarouter/node/NodeConfig.java                  |
| -                  | -              | -             | -           | -      | -           | -           | -            | -                                                                                             |
| -                  | -              | -             | -           | -      | -           | -           | -            | -                                                                                             |
| -                  | -              | -             | -           | -      | -           | -           | -            | -                                                                                             |
| -                  | -              | -             | -           | -      | -           | -           | -            | -                                                                                             |
| -                  | -              | -             | -           | -      | -           | -           | -            | -                                                                                             |
| -                  | -              | -             | -           | -      | -           | -           | -            | -                                                                                             |

## Project 2: _onap/externalapi-nbi_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_externalapi-nbi.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/externalapi-nbi) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_externalapi-nbi) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_externalapi-nbi.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                           | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                                 |
|:-------------------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:-------------------------------------------------------------------------------------------|
| MongoConfig.java                     | 2              | 0             | 2           | 0      | 0           | 0           | 0            | src/main/java/org/onap/nbi/configuration/MongoConfig.java                                  |
| ExecutionTaskProcessorScheduler.java | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/onap/nbi/apis/serviceorder/workflow/ExecutionTaskProcessorScheduler.java |
| EventFactory.java                    | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/onap/nbi/apis/hub/service/EventFactory.java                              |
| E2EServiceUtils.java                 | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/onap/nbi/apis/serviceorder/utils/E2EServiceUtils.java                    |
| MacroServiceUtils.java               | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/onap/nbi/apis/serviceorder/utils/MacroServiceUtils.java                  |
| -                                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                          |
| -                                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                          |
| -                                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                          |
| -                                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                          |
| -                                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                          |

## Project 3: _onap/music_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/onap_music.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/onap/music) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=onap_music) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/onap_music.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                  |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                     |
|:----------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:-------------------------------------------------------------------------------|
| RestMusicDataAPI.java       |             18 |             0 |           6 |      0 |          12 |           0 |            0 | music-rest/src/main/java/org/onap/music/rest/RestMusicDataAPI.java             |
| RestMusicLocksAPI.java      |             13 |             0 |           8 |      0 |           3 |           0 |            2 | music-rest/src/main/java/org/onap/music/rest/RestMusicLocksAPI.java            |
| MusicUtil.java              |              9 |             0 |           5 |      0 |           2 |           0 |            2 | music-core/src/main/java/org/onap/music/main/MusicUtil.java                    |
| CipherUtil.java             |              8 |             0 |           0 |      0 |           4 |           0 |            4 | music-core/src/main/java/org/onap/music/main/CipherUtil.java                   |
| RestMusicQAPI.java          |              7 |             0 |           0 |      0 |           7 |           0 |            0 | music-rest/src/main/java/org/onap/music/rest/RestMusicQAPI.java                |
| MusicCassaCore.java         |              6 |             0 |           0 |      0 |           3 |           0 |            3 | music-core/src/main/java/org/onap/music/service/impl/MusicCassaCore.java       |
| MusicDeadlockException.java |              4 |             0 |           4 |      0 |           0 |           0 |            0 | music-core/src/main/java/org/onap/music/exceptions/MusicDeadlockException.java |
| JsonInsert.java             |              2 |             0 |           0 |      0 |           2 |           0 |            0 | music-core/src/main/java/org/onap/music/datastore/jsonobjects/JsonInsert.java  |
| JsonSelect.java             |              2 |             0 |           0 |      0 |           2 |           0 |            0 | music-core/src/main/java/org/onap/music/datastore/jsonobjects/JsonSelect.java  |
| MusicServiceException.java  |              2 |             0 |           2 |      0 |           0 |           0 |            0 | music-core/src/main/java/org/onap/music/exceptions/MusicServiceException.java  |

