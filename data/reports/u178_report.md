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
|<p align="center">Project 1</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_incubator-ratis.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/incubator-ratis) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_incubator-ratis) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_incubator-ratis.json)</p>|<p align="center">Project 2</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/hadoop-ozone.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/hadoop-ozone) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=hadoop-ozone) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/hadoop-ozone.json)</p>
# ATDx project report summaries
## Project 1: _apache/incubator-ratis_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_incubator-ratis.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/incubator-ratis) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_incubator-ratis) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_incubator-ratis.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name            |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                              |
|:----------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:----------------------------------------------------------------------------------------|
| NativeIO.java         |             40 |             3 |           1 |      0 |          36 |           0 |            0 | ratis-common/src/main/java/org/apache/ratis/io/nativeio/NativeIO.java                   |
| MetaStateMachine.java |              6 |             5 |           0 |      1 |           0 |           0 |            0 | ratis-logservice/src/main/java/org/apache/ratis/logservice/server/MetaStateMachine.java |
| VerificationTool.java |              6 |             0 |           6 |      0 |           0 |           0 |            0 | ratis-logservice/src/main/java/org/apache/ratis/logservice/tool/VerificationTool.java   |
| RaftProperties.java   |              6 |             0 |           6 |      0 |           0 |           0 |            0 | ratis-common/src/main/java/org/apache/ratis/conf/RaftProperties.java                    |
| NativeCrc32.java      |              5 |             0 |           2 |      0 |           3 |           0 |            0 | ratis-common/src/main/java/org/apache/ratis/util/NativeCrc32.java                       |
| ServerProtoUtils.java |              3 |             0 |           0 |      0 |           3 |           0 |            0 | ratis-server/src/main/java/org/apache/ratis/server/impl/ServerProtoUtils.java           |
| LogServiceClient.java |              3 |             0 |           3 |      0 |           0 |           0 |            0 | ratis-logservice/src/main/java/org/apache/ratis/logservice/api/LogServiceClient.java    |
| LogStateMachine.java  |              3 |             0 |           3 |      0 |           0 |           0 |            0 | ratis-logservice/src/main/java/org/apache/ratis/logservice/server/LogStateMachine.java  |
| LogAppender.java      |              3 |             0 |           3 |      0 |           0 |           0 |            0 | ratis-server/src/main/java/org/apache/ratis/server/impl/LogAppender.java                |
| LogSegment.java       |              3 |             1 |           0 |      1 |           1 |           0 |            0 | ratis-server/src/main/java/org/apache/ratis/server/raftlog/segmented/LogSegment.java    |

## Project 2: _apache/hadoop-ozone_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/hadoop-ozone.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/hadoop-ozone) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=hadoop-ozone) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/hadoop-ozone.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name               |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                   |
|:-------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:---------------------------------------------------------------------------------------------|
| OzoneManager.java        |             22 |             0 |          18 |      0 |           4 |           0 |            0 | hadoop-ozone/ozone-manager/src/main/java/org/apache/hadoop/ozone/om/OzoneManager.java        |
| HddsDatanodeService.java |             14 |             0 |          14 |      0 |           0 |           0 |            0 | hadoop-hdds/container-service/src/main/java/org/apache/hadoop/ozone/HddsDatanodeService.java |
| BaseFreonGenerator.java  |              8 |             0 |           8 |      0 |           0 |           0 |            0 | hadoop-ozone/tools/src/main/java/org/apache/hadoop/ozone/freon/BaseFreonGenerator.java       |
| LockManager.java         |              7 |             0 |           3 |      0 |           2 |           0 |            2 | hadoop-hdds/common/src/main/java/org/apache/hadoop/ozone/lock/LockManager.java               |
| OzoneManagerLock.java    |              6 |             0 |           2 |      0 |           2 |           0 |            2 | hadoop-ozone/common/src/main/java/org/apache/hadoop/ozone/om/lock/OzoneManagerLock.java      |
| ConfigurationSource.java |              6 |             0 |           4 |      0 |           1 |           0 |            1 | hadoop-hdds/config/src/main/java/org/apache/hadoop/hdds/conf/ConfigurationSource.java        |
| OzoneManagerStarter.java |              6 |             0 |           6 |      0 |           0 |           0 |            0 | hadoop-ozone/ozone-manager/src/main/java/org/apache/hadoop/ozone/om/OzoneManagerStarter.java |
| OS3Exception.java        |              6 |             0 |           6 |      0 |           0 |           0 |            0 | hadoop-ozone/s3gateway/src/main/java/org/apache/hadoop/ozone/s3/exception/OS3Exception.java  |
| OzoneBucket.java         |              5 |             0 |           1 |      0 |           4 |           0 |            0 | hadoop-ozone/client/src/main/java/org/apache/hadoop/ozone/client/OzoneBucket.java            |
| GenericTestUtils.java    |              5 |             0 |           0 |      0 |           3 |           0 |            2 | hadoop-hdds/test-utils/src/main/java/org/apache/hadoop/test/GenericTestUtils.java            |

