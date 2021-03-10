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
|<p align="center">Project 1</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-jspc-maven-plugin.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-jspc-maven-plugin) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-jspc-maven-plugin) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-jspc-maven-plugin.json)</p>|<p align="center">Project 2</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-feature-analyser.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-feature-analyser) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-feature-analyser) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-feature-analyser.json)</p>|<p align="center">Project 3</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-feature-extension-apiregions.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-feature-extension-apiregions) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-feature-extension-apiregions) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-feature-extension-apiregions.json)</p>
 | |
|<p align="center">Project 4</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-feature-launcher.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-feature-launcher) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-feature-launcher) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-feature-launcher.json)</p>|<p align="center">Project 5</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-feature.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-feature) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-feature) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-feature.json)</p>|<p align="center">Project 6</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-scripting-bundle-tracker.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-scripting-bundle-tracker) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-scripting-bundle-tracker) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-scripting-bundle-tracker.json)</p>
 | |
|<p align="center">Project 7</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-scripting-core.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-scripting-core) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-scripting-core) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-scripting-core.json)</p>|<p align="center">Project 8</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-scripting-jsp.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-scripting-jsp) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-scripting-jsp) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-scripting-jsp.json)</p>|<p align="center">Project 9</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-scripting-sightly.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-scripting-sightly) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-scripting-sightly) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-scripting-sightly.json)</p>

# ATDx project report summaries
## Project 1: _apache/sling-jspc-maven-plugin_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-jspc-maven-plugin.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-jspc-maven-plugin) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-jspc-maven-plugin) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-jspc-maven-plugin.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                 | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                           |
|:---------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:---------------------------------------------------------------------|
| JspCServletContext.java    | 8              | 0             | 0           | 0      | 4           | 0           | 4            | src/main/java/org/apache/sling/maven/jspc/JspCServletContext.java    |
| JspcMojo.java              | 4              | 0             | 2           | 0      | 1           | 0           | 1            | src/main/java/org/apache/sling/maven/jspc/JspcMojo.java              |
| JspCTldLocationsCache.java | 2              | 0             | 2           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/maven/jspc/JspCTldLocationsCache.java |
| JspCIOProvider.java        | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/maven/jspc/JspCIOProvider.java        |
| JspCClassLoaderWriter.java | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/maven/jspc/JspCClassLoaderWriter.java |
| -                          | -              | -             | -           | -      | -           | -           | -            | -                                                                    |
| -                          | -              | -             | -           | -      | -           | -           | -            | -                                                                    |
| -                          | -              | -             | -           | -      | -           | -           | -            | -                                                                    |
| -                          | -              | -             | -           | -      | -           | -           | -            | -                                                                    |
| -                          | -              | -             | -           | -      | -           | -           | -            | -                                                                    |

## Project 2: _apache/sling-org-apache-sling-feature-analyser_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-feature-analyser.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-feature-analyser) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-feature-analyser) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-feature-analyser.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                            | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                                      |
|:--------------------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:------------------------------------------------------------------------------------------------|
| CheckBundleExportsImports.java        | 6              | 0             | 0           | 0      | 6           | 0           | 0            | src/main/java/org/apache/sling/feature/analyser/task/impl/CheckBundleExportsImports.java        |
| Analyser.java                         | 2              | 0             | 2           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/feature/analyser/Analyser.java                                   |
| Scanner.java                          | 2              | 0             | 0           | 0      | 1           | 0           | 1            | src/main/java/org/apache/sling/feature/scanner/Scanner.java                                     |
| BundleDescriptor.java                 | 2              | 0             | 0           | 0      | 1           | 0           | 1            | src/main/java/org/apache/sling/feature/scanner/BundleDescriptor.java                            |
| AnalyserTask.java                     | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/feature/analyser/task/AnalyserTask.java                          |
| CheckContentPackagesDependencies.java | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/feature/analyser/task/impl/CheckContentPackagesDependencies.java |
| -                                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                               |
| -                                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                               |
| -                                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                               |
| -                                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                               |

## Project 3: _apache/sling-org-apache-sling-feature-extension-apiregions_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-feature-extension-apiregions.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-feature-extension-apiregions) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-feature-extension-apiregions) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-feature-extension-apiregions.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                               | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                                                    |
|:-----------------------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:--------------------------------------------------------------------------------------------------------------|
| CheckApiRegionsBundleExportsImports.java | 7              | 0             | 0           | 0      | 7           | 0           | 0            | src/main/java/org/apache/sling/feature/extension/apiregions/analyser/CheckApiRegionsBundleExportsImports.java |
| APIRegionMergeHandler.java               | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/feature/extension/apiregions/APIRegionMergeHandler.java                        |
| LauncherProperties.java                  | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/feature/extension/apiregions/launcher/LauncherProperties.java                  |
| RegionLauncher.java                      | 1              | 1             | 0           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/feature/extension/apiregions/launcher/RegionLauncher.java                      |
| AbstractApiRegionsAnalyserTask.java      | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/feature/extension/apiregions/analyser/AbstractApiRegionsAnalyserTask.java      |
| -                                        | -              | -             | -           | -      | -           | -           | -            | -                                                                                                             |
| -                                        | -              | -             | -           | -      | -           | -           | -            | -                                                                                                             |
| -                                        | -              | -             | -           | -      | -           | -           | -            | -                                                                                                             |
| -                                        | -              | -             | -           | -      | -           | -           | -            | -                                                                                                             |
| -                                        | -              | -             | -           | -      | -           | -           | -            | -                                                                                                             |

## Project 4: _apache/sling-org-apache-sling-feature-launcher_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-feature-launcher.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-feature-launcher) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-feature-launcher) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-feature-launcher.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name            | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                                    |
|:----------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:----------------------------------------------------------------------------------------------|
| AbstractRunner.java   | 4              | 0             | 4           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/feature/launcher/impl/launchers/AbstractRunner.java            |
| FeatureProcessor.java | 2              | 0             | 1           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/feature/launcher/impl/FeatureProcessor.java                    |
| Launcher.java         | 2              | 0             | 2           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/feature/launcher/spi/Launcher.java                             |
| FrameworkRunner.java  | 2              | 0             | 2           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/feature/launcher/impl/launchers/FrameworkRunner.java           |
| Bootstrap.java        | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/feature/launcher/impl/Bootstrap.java                           |
| ExtensionHandler.java | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/feature/launcher/spi/extensions/ExtensionHandler.java          |
| RepoInitHandler.java  | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/feature/launcher/impl/extensions/handlers/RepoInitHandler.java |
| -                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                             |
| -                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                             |
| -                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                             |

## Project 5: _apache/sling-org-apache-sling-feature_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-feature.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-feature) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-feature) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-feature.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                 |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                     |
|:---------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:-------------------------------------------------------------------------------|
| Extension.java             |              6 |             0 |           0 |      0 |           3 |           0 |            3 | src/main/java/org/apache/sling/feature/Extension.java                          |
| ConfiguratorUtil.java      |              4 |             0 |           2 |      0 |           1 |           0 |            1 | src/main/java/org/apache/sling/feature/io/ConfiguratorUtil.java                |
| CloseShieldWriter.java     |              2 |             0 |           0 |      0 |           1 |           0 |            1 | src/main/java/org/apache/sling/feature/io/CloseShieldWriter.java               |
| Configuration.java         |              2 |             1 |           0 |      1 |           0 |           0 |            0 | src/main/java/org/apache/sling/feature/Configuration.java                      |
| BuilderContext.java        |              2 |             0 |           0 |      0 |           1 |           0 |            1 | src/main/java/org/apache/sling/feature/builder/BuilderContext.java             |
| FeatureBuilder.java        |              1 |             0 |           0 |      0 |           1 |           0 |            0 | src/main/java/org/apache/sling/feature/builder/FeatureBuilder.java             |
| JSONConstants.java         |              1 |             0 |           0 |      0 |           1 |           0 |            0 | src/main/java/org/apache/sling/feature/io/json/JSONConstants.java              |
| IOUtils.java               |              1 |             0 |           0 |      0 |           1 |           0 |            0 | src/main/java/org/apache/sling/feature/io/IOUtils.java                         |
| ArtifactManagerConfig.java |              1 |             0 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/feature/io/artifacts/ArtifactManagerConfig.java |
| BuilderUtil.java           |              1 |             0 |           0 |      0 |           1 |           0 |            0 | src/main/java/org/apache/sling/feature/builder/BuilderUtil.java                |

## Project 6: _apache/sling-org-apache-sling-scripting-bundle-tracker_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-scripting-bundle-tracker.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-scripting-bundle-tracker) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-scripting-bundle-tracker) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-scripting-bundle-tracker.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                           | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                                            |
|:-------------------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:------------------------------------------------------------------------------------------------------|
| BundledRenderUnitCapabilityImpl.java | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/scripting/bundle/tracker/internal/BundledRenderUnitCapabilityImpl.java |
| -                                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                                     |
| -                                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                                     |
| -                                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                                     |
| -                                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                                     |
| -                                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                                     |
| -                                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                                     |
| -                                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                                     |
| -                                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                                     |
| -                                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                                     |

## Project 7: _apache/sling-org-apache-sling-scripting-core_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-scripting-core.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-scripting-core) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-scripting-core) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-scripting-core.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                        |
|:--------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:----------------------------------------------------------------------------------|
| ScriptHelper.java         | 3              | 0             | 1           | 0      | 1           | 0           | 1            | src/main/java/org/apache/sling/scripting/core/ScriptHelper.java                   |
| ServiceCache.java         | 2              | 0             | 0           | 0      | 2           | 0           | 0            | src/main/java/org/apache/sling/scripting/core/impl/ServiceCache.java              |
| Script.java               | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/scripting/core/impl/bundled/Script.java            |
| PrecompiledScript.java    | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/scripting/core/impl/bundled/PrecompiledScript.java |
| InternalScriptHelper.java | 1              | 1             | 0           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/scripting/core/impl/InternalScriptHelper.java      |
| -                         | -              | -             | -           | -      | -           | -           | -            | -                                                                                 |
| -                         | -              | -             | -           | -      | -           | -           | -            | -                                                                                 |
| -                         | -              | -             | -           | -      | -           | -           | -            | -                                                                                 |
| -                         | -              | -             | -           | -      | -           | -           | -            | -                                                                                 |
| -                         | -              | -             | -           | -      | -           | -           | -            | -                                                                                 |

## Project 8: _apache/sling-org-apache-sling-scripting-jsp_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-scripting-jsp.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-scripting-jsp) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-scripting-jsp) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-scripting-jsp.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name               |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                             |
|:-------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:---------------------------------------------------------------------------------------|
| PageDataImpl.java        |             34 |            33 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/scripting/jsp/jasper/compiler/PageDataImpl.java         |
| Dumper.java              |             22 |            21 |           0 |      0 |           1 |           0 |            0 | src/main/java/org/apache/sling/scripting/jsp/jasper/compiler/Dumper.java               |
| Collector.java           |             14 |            13 |           0 |      0 |           1 |           0 |            0 | src/main/java/org/apache/sling/scripting/jsp/jasper/compiler/Collector.java            |
| ELResolverImpl.java      |             13 |             0 |          13 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/scripting/jsp/jasper/el/ELResolverImpl.java             |
| JspValueExpression.java  |             13 |             0 |          13 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/scripting/jsp/jasper/el/JspValueExpression.java         |
| XMLEncodingDetector.java |             11 |             7 |           0 |      0 |           0 |           0 |            4 | src/main/java/org/apache/sling/scripting/jsp/jasper/xmlparser/XMLEncodingDetector.java |
| JspDocumentParser.java   |             11 |             8 |           1 |      0 |           2 |           0 |            0 | src/main/java/org/apache/sling/scripting/jsp/jasper/compiler/JspDocumentParser.java    |
| Generator.java           |             11 |             0 |          11 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/scripting/jsp/jasper/compiler/Generator.java            |
| ELFunctionMapper.java    |             11 |            11 |           0 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/scripting/jsp/jasper/compiler/ELFunctionMapper.java     |
| Compiler.java            |             10 |             0 |          10 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/scripting/jsp/jasper/compiler/Compiler.java             |

## Project 9: _apache/sling-org-apache-sling-scripting-sightly_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-scripting-sightly.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-scripting-sightly) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-scripting-sightly) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-scripting-sightly.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name              | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                                 |
|:------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:-------------------------------------------------------------------------------------------|
| ExtensionUtils.java     | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/scripting/sightly/impl/engine/extension/ExtensionUtils.java |
| BindingsUtils.java      | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/scripting/sightly/impl/utils/BindingsUtils.java             |
| ScriptUtils.java        | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/scripting/sightly/impl/utils/ScriptUtils.java               |
| ResourceResolution.java | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/scripting/sightly/engine/ResourceResolution.java            |
| -                       | -              | -             | -           | -      | -           | -           | -            | -                                                                                          |
| -                       | -              | -             | -           | -      | -           | -           | -            | -                                                                                          |
| -                       | -              | -             | -           | -      | -           | -           | -            | -                                                                                          |
| -                       | -              | -             | -           | -      | -           | -           | -            | -                                                                                          |
| -                       | -              | -             | -           | -      | -           | -           | -            | -                                                                                          |
| -                       | -              | -             | -           | -      | -           | -           | -            | -                                                                                          |

