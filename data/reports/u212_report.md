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
|<p align="center">Project 1</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/pdfbox-reactor.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/pdfbox) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=pdfbox-reactor) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/pdfbox-reactor.json)</p>|<p align="center">Project 2</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/poi-parent.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/poi) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=poi-parent) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/poi-parent.json)</p>
# ATDx project report summaries
## Project 1: _apache/pdfbox_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/pdfbox-reactor.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/pdfbox) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=pdfbox-reactor) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/pdfbox-reactor.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                   |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                             |
|:-----------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:---------------------------------------------------------------------------------------|
| PDPageContentStream.java     |             68 |             0 |           0 |      0 |          34 |           0 |           34 | pdfbox/src/main/java/org/apache/pdfbox/pdmodel/PDPageContentStream.java                |
| CMapParser.java              |             17 |             0 |           0 |      0 |           0 |           0 |           17 | fontbox/src/main/java/org/apache/fontbox/cmap/CMapParser.java                          |
| PDFDebugger.java             |             13 |             0 |          12 |      0 |           1 |           0 |            0 | debugger/src/main/java/org/apache/pdfbox/debugger/PDFDebugger.java                     |
| CCITTFactory.java            |             12 |             0 |           0 |      0 |           0 |           0 |           12 | pdfbox/src/main/java/org/apache/pdfbox/pdmodel/graphics/image/CCITTFactory.java        |
| PDFStreamParser.java         |             10 |             0 |           0 |      0 |           0 |           0 |           10 | pdfbox/src/main/java/org/apache/pdfbox/pdfparser/PDFStreamParser.java                  |
| BaseParser.java              |              8 |             0 |           0 |      0 |           0 |           0 |            8 | pdfbox/src/main/java/org/apache/pdfbox/pdfparser/BaseParser.java                       |
| OSXAdapter.java              |              6 |             0 |           6 |      0 |           0 |           0 |            0 | debugger/src/main/java/org/apache/pdfbox/debugger/ui/OSXAdapter.java                   |
| StandardSecurityHandler.java |              6 |             0 |           0 |      0 |           6 |           0 |            0 | pdfbox/src/main/java/org/apache/pdfbox/pdmodel/encryption/StandardSecurityHandler.java |
| Type2CharString.java         |              4 |             0 |           0 |      0 |           0 |           0 |            4 | fontbox/src/main/java/org/apache/fontbox/cff/Type2CharString.java                      |
| GlyphSubstitutionTable.java  |              4 |             0 |           0 |      0 |           0 |           0 |            4 | fontbox/src/main/java/org/apache/fontbox/ttf/GlyphSubstitutionTable.java               |

## Project 2: _apache/poi_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/poi-parent.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/poi) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=poi-parent) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/poi-parent.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                   |
|:--------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:-----------------------------------------------------------------------------|
| FileInformationBlock.java |             68 |             0 |           0 |      0 |          34 |           0 |           34 | scratchpad/src/main/java/org/apache/poi/hwpf/model/FileInformationBlock.java |
| ClassID.java              |             55 |             0 |           1 |      0 |          27 |           0 |           27 | main/src/main/java/org/apache/poi/hpsf/ClassID.java                          |
| XSSFChart.java            |             30 |             0 |           0 |      0 |          15 |           0 |           15 | ooxml/src/main/java/org/apache/poi/xssf/usermodel/XSSFChart.java             |
| Range.java                |             26 |             0 |           0 |      0 |          13 |           0 |           13 | scratchpad/src/main/java/org/apache/poi/hwpf/usermodel/Range.java            |
| HeaderStories.java        |             26 |             0 |           0 |      0 |          13 |           0 |           13 | scratchpad/src/main/java/org/apache/poi/hwpf/usermodel/HeaderStories.java    |
| SXSSFCell.java            |             21 |             0 |           2 |      0 |           1 |           0 |           18 | ooxml/src/main/java/org/apache/poi/xssf/streaming/SXSSFCell.java             |
| SignatureConfig.java      |             20 |             0 |           0 |      0 |          10 |           0 |           10 | ooxml/src/main/java/org/apache/poi/poifs/crypt/dsig/SignatureConfig.java     |
| FontFormatting.java       |             19 |             1 |           0 |      0 |           9 |           0 |            9 | main/src/main/java/org/apache/poi/hssf/record/cf/FontFormatting.java         |
| HSLFShape.java            |             18 |             0 |           0 |      0 |           4 |           0 |           14 | scratchpad/src/main/java/org/apache/poi/hslf/usermodel/HSLFShape.java        |
| SXSSFWorkbook.java        |             17 |             0 |           5 |      0 |           6 |           0 |            6 | ooxml/src/main/java/org/apache/poi/xssf/streaming/SXSSFWorkbook.java         |

