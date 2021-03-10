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
|<p align="center">Project 1</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/commons-compress.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/commons-compress) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=commons-compress) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/commons-compress.json)</p>|<p align="center">Project 2</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/cxf.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/cxf) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=cxf) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/cxf.json)</p>
# ATDx project report summaries
## Project 1: _apache/commons-compress_
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

## Project 2: _apache/cxf_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/cxf.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/cxf) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=cxf) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/cxf.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                    |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                                                  |
|:------------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:----------------------------------------------------------------------------------------------------------------------------|
| IDLLexer.java                 |            196 |             0 |          38 |      0 |           0 |           0 |          158 | tools/corba/src/main/generated/org/apache/cxf/tools/corba/processors/idl/IDLLexer.java                                      |
| ASMHelper.java                |             55 |             0 |           5 |      0 |          50 |           0 |            0 | core/src/main/java/org/apache/cxf/common/util/ASMHelper.java                                                                |
| UriBuilderImpl.java           |             47 |             2 |          42 |      1 |           2 |           0 |            0 | rt/frontend/jaxrs/src/main/java/org/apache/cxf/jaxrs/impl/UriBuilderImpl.java                                               |
| AbstractDelegatingLogger.java |             44 |            36 |           0 |      0 |           4 |           0 |            4 | core/src/main/java/org/apache/cxf/common/logging/AbstractDelegatingLogger.java                                              |
| CorbaObjectReader.java        |             37 |             0 |          25 |      0 |           0 |           0 |           12 | rt/bindings/corba/src/main/java/org/apache/cxf/binding/corba/runtime/CorbaObjectReader.java                                 |
| CryptoUtils.java              |             34 |             0 |          32 |      0 |           2 |           0 |            0 | rt/security/src/main/java/org/apache/cxf/rt/security/crypto/CryptoUtils.java                                                |
| StaxUtils.java                |             28 |             0 |          23 |      0 |           1 |           0 |            4 | core/src/main/java/org/apache/cxf/staxutils/StaxUtils.java                                                                  |
| ModelEncryptionSupport.java   |             28 |             0 |          28 |      0 |           0 |           0 |            0 | rt/rs/security/oauth-parent/oauth2/src/main/java/org/apache/cxf/rs/security/oauth2/utils/crypto/ModelEncryptionSupport.java |
| JMSConstants.java             |             26 |             0 |           0 |      0 |          13 |           0 |           13 | rt/transports/jms/src/main/java/org/apache/cxf/transport/jms/JMSConstants.java                                              |
| JAXBDataBinding.java          |             25 |            15 |          10 |      0 |           0 |           0 |            0 | tools/wsdlto/databinding/jaxb/src/main/java/org/apache/cxf/tools/wsdlto/databinding/jaxb/JAXBDataBinding.java               |

