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
|<p align="center">Project 1</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-api.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-api) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-api) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-api.json)</p>|<p align="center">Project 2</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-app-cms.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-app-cms) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-app-cms) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-app-cms.json)</p>|<p align="center">Project 3</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-engine.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-engine) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-engine) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-engine.json)</p>
 | |
|<p align="center">Project 4</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-feature-analyser.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-feature-analyser) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-feature-analyser) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-feature-analyser.json)</p>|<p align="center">Project 5</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-feature-cpconverter.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-feature-cpconverter) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-feature-cpconverter) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-feature-cpconverter.json)</p>|<p align="center">Project 6</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-feature-extension-apiregions.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-feature-extension-apiregions) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-feature-extension-apiregions) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-feature-extension-apiregions.json)</p>
 | |
|<p align="center">Project 7</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-feature-launcher.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-feature-launcher) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-feature-launcher) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-feature-launcher.json)</p>|<p align="center">Project 8</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-feature-modelconverter.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-feature-modelconverter) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-feature-modelconverter) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-feature-modelconverter.json)</p>|<p align="center">Project 9</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-feature.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-feature) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-feature) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-feature.json)</p>

# ATDx project report summaries
## Project 1: _apache/sling-org-apache-sling-api_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-api.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-api) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-api) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-api.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                   |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                       |
|:-----------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:---------------------------------------------------------------------------------|
| ResourceUtil.java            |             13 |             0 |           0 |      0 |           7 |           0 |            6 | src/main/java/org/apache/sling/api/resource/ResourceUtil.java                    |
| ResourceProviderDTO.java     |             10 |             0 |           0 |      0 |          10 |           0 |            0 | src/main/java/org/apache/sling/api/resource/runtime/dto/ResourceProviderDTO.java |
| ResourceChange.java          |              8 |             0 |           0 |      0 |           4 |           0 |            4 | src/main/java/org/apache/sling/api/resource/observation/ResourceChange.java      |
| SlingConstants.java          |              7 |             0 |           0 |      0 |           4 |           0 |            3 | src/main/java/org/apache/sling/api/SlingConstants.java                           |
| ResourceMetadata.java        |              4 |             1 |           0 |      1 |           1 |           0 |            1 | src/main/java/org/apache/sling/api/resource/ResourceMetadata.java                |
| CompositeValueMap.java       |              4 |             2 |           0 |      0 |           1 |           0 |            1 | src/main/java/org/apache/sling/api/wrappers/CompositeValueMap.java               |
| ResourceProvider.java        |              4 |             0 |           0 |      0 |           2 |           0 |            2 | src/main/java/org/apache/sling/api/resource/ResourceProvider.java                |
| ResourceProviderFactory.java |              4 |             0 |           0 |      0 |           2 |           0 |            2 | src/main/java/org/apache/sling/api/resource/ResourceProviderFactory.java         |
| ResourceResolver.java        |              4 |             0 |           0 |      0 |           2 |           0 |            2 | src/main/java/org/apache/sling/api/resource/ResourceResolver.java                |
| NonExistingResource.java     |              3 |             3 |           0 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/api/resource/NonExistingResource.java             |

## Project 2: _apache/sling-org-apache-sling-app-cms_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-app-cms.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-app-cms) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-app-cms) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-app-cms.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name               | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                             |
|:-------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:---------------------------------------------------------------------------------------|
| FormRequestImpl.java     | 3              | 0             | 3           | 0      | 0           | 0           | 0            | reference/src/main/java/org/apache/sling/cms/reference/forms/impl/FormRequestImpl.java |
| BaseInsightProvider.java | 1              | 0             | 1           | 0      | 0           | 0           | 0            | core/src/main/java/org/apache/sling/cms/core/insights/impl/BaseInsightProvider.java    |
| -                        | -              | -             | -           | -      | -           | -           | -            | -                                                                                      |
| -                        | -              | -             | -           | -      | -           | -           | -            | -                                                                                      |
| -                        | -              | -             | -           | -      | -           | -           | -            | -                                                                                      |
| -                        | -              | -             | -           | -      | -           | -           | -            | -                                                                                      |
| -                        | -              | -             | -           | -      | -           | -           | -            | -                                                                                      |
| -                        | -              | -             | -           | -      | -           | -           | -            | -                                                                                      |
| -                        | -              | -             | -           | -      | -           | -           | -            | -                                                                                      |
| -                        | -              | -             | -           | -      | -           | -           | -            | -                                                                                      |

## Project 3: _apache/sling-org-apache-sling-engine_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-engine.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-engine) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-engine) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-engine.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                          |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                          |
|:------------------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:------------------------------------------------------------------------------------|
| EngineConstants.java                |             15 |             0 |           0 |      0 |           8 |           0 |            7 | src/main/java/org/apache/sling/engine/EngineConstants.java                          |
| SlingServletContext.java            |              8 |             0 |           0 |      0 |           4 |           0 |            4 | src/main/java/org/apache/sling/engine/impl/helper/SlingServletContext.java          |
| SlingServletResponseAdapter.java    |              6 |             0 |           0 |      0 |           3 |           0 |            3 | src/main/java/org/apache/sling/engine/impl/adapter/SlingServletResponseAdapter.java |
| SlingServletRequestAdapter.java     |              4 |             0 |           0 |      0 |           2 |           0 |            2 | src/main/java/org/apache/sling/engine/impl/adapter/SlingServletRequestAdapter.java  |
| SlingHttpServletResponseImpl.java   |              4 |             0 |           0 |      0 |           2 |           0 |            2 | src/main/java/org/apache/sling/engine/impl/SlingHttpServletResponseImpl.java        |
| Util.java                           |              3 |             0 |           2 |      0 |           1 |           0 |            0 | src/main/java/org/apache/sling/engine/impl/parameters/Util.java                     |
| ResponseUtil.java                   |              3 |             0 |           0 |      0 |           2 |           0 |            1 | src/main/java/org/apache/sling/engine/ResponseUtil.java                             |
| RequestUtil.java                    |              3 |             0 |           0 |      0 |           2 |           0 |            1 | src/main/java/org/apache/sling/engine/RequestUtil.java                              |
| AbstractServiceReferenceConfig.java |              2 |             0 |           0 |      0 |           1 |           0 |            1 | src/main/java/org/apache/sling/engine/servlets/AbstractServiceReferenceConfig.java  |
| RequestLog.java                     |              2 |             0 |           0 |      0 |           1 |           0 |            1 | src/main/java/org/apache/sling/engine/RequestLog.java                               |

## Project 4: _apache/sling-org-apache-sling-feature-analyser_
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

## Project 5: _apache/sling-org-apache-sling-feature-cpconverter_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-feature-cpconverter.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-feature-cpconverter) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-feature-cpconverter) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-feature-cpconverter.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                                |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                         |
|:------------------------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:---------------------------------------------------------------------------------------------------|
| BaseVaultPackageScanner.java              |              3 |             0 |           3 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/feature/cpconverter/vltpkg/BaseVaultPackageScanner.java             |
| AbstractConfigurationEntryHandler.java    |              1 |             0 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/feature/cpconverter/handlers/AbstractConfigurationEntryHandler.java |
| DefaultFeaturesManager.java               |              1 |             0 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/feature/cpconverter/features/DefaultFeaturesManager.java            |
| EntryHandler.java                         |              1 |             0 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/feature/cpconverter/handlers/EntryHandler.java                      |
| DefaultAclManager.java                    |              1 |             0 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/feature/cpconverter/acl/DefaultAclManager.java                      |
| FeaturesManager.java                      |              1 |             0 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/feature/cpconverter/features/FeaturesManager.java                   |
| AbstractJcrNodeParser.java                |              1 |             0 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/feature/cpconverter/shared/AbstractJcrNodeParser.java               |
| ContentPackage2FeatureModelConverter.java |              1 |             0 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/feature/cpconverter/ContentPackage2FeatureModelConverter.java       |
| AbstractContentPackageHandler.java        |              1 |             0 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/feature/cpconverter/handlers/AbstractContentPackageHandler.java     |
| VaultPackageAssembler.java                |              1 |             0 |           1 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/feature/cpconverter/vltpkg/VaultPackageAssembler.java               |

## Project 6: _apache/sling-org-apache-sling-feature-extension-apiregions_
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

## Project 7: _apache/sling-org-apache-sling-feature-launcher_
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

## Project 8: _apache/sling-org-apache-sling-feature-modelconverter_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-feature-modelconverter.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-feature-modelconverter) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-feature-modelconverter) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-feature-modelconverter.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                 | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                       |
|:---------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:---------------------------------------------------------------------------------|
| FeatureToProvisioning.java | 4              | 0             | 3           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/feature/modelconverter/FeatureToProvisioning.java |
| ProvisioningToFeature.java | 2              | 0             | 0           | 0      | 2           | 0           | 0            | src/main/java/org/apache/sling/feature/modelconverter/ProvisioningToFeature.java |
| -                          | -              | -             | -           | -      | -           | -           | -            | -                                                                                |
| -                          | -              | -             | -           | -      | -           | -           | -            | -                                                                                |
| -                          | -              | -             | -           | -      | -           | -           | -            | -                                                                                |
| -                          | -              | -             | -           | -      | -           | -           | -            | -                                                                                |
| -                          | -              | -             | -           | -      | -           | -           | -            | -                                                                                |
| -                          | -              | -             | -           | -      | -           | -           | -            | -                                                                                |
| -                          | -              | -             | -           | -      | -           | -           | -            | -                                                                                |
| -                          | -              | -             | -           | -      | -           | -           | -            | -                                                                                |

## Project 9: _apache/sling-org-apache-sling-feature_
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

