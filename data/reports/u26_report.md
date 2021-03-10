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
|<p align="center">Project 1</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-api.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-api) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-api) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-api.json)</p>|<p align="center">Project 2</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-caconfig-impl.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-caconfig-impl) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-caconfig-impl) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-caconfig-impl.json)</p>|<p align="center">Project 3</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-servlet-helpers.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-servlet-helpers) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-servlet-helpers) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-servlet-helpers.json)</p>
 | |
|<p align="center">Project 4</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-testing-jcr-mock.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-testing-jcr-mock) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-testing-jcr-mock) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-testing-jcr-mock.json)</p>|<p align="center">Project 5</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-testing-osgi-mock.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-testing-osgi-mock) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-testing-osgi-mock) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-testing-osgi-mock.json)</p>|<p align="center">Project 6</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-testing-resourceresolver-mock.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-testing-resourceresolver-mock) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-testing-resourceresolver-mock) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-testing-resourceresolver-mock.json)</p>
 | |
|<p align="center">Project 7</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-testing-sling-mock.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-testing-sling-mock) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-testing-sling-mock) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-testing-sling-mock.json)</p>
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

## Project 2: _apache/sling-org-apache-sling-caconfig-impl_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-caconfig-impl.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-caconfig-impl) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-caconfig-impl) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-caconfig-impl.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                            | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                                           |
|:--------------------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:-----------------------------------------------------------------------------------------------------|
| ConfigurationResourceWrapper.java     | 8              | 8             | 0           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/caconfig/impl/ConfigurationResourceWrapper.java                       |
| ConfigurationManager.java             | 2              | 0             | 0           | 0      | 1           | 0           | 1            | src/main/java/org/apache/sling/caconfig/management/ConfigurationManager.java                         |
| ContextPathStrategyMultiplexer.java   | 2              | 0             | 0           | 0      | 1           | 0           | 1            | src/main/java/org/apache/sling/caconfig/management/ContextPathStrategyMultiplexer.java               |
| ConfigurationDataImpl.java            | 2              | 0             | 0           | 0      | 2           | 0           | 0            | src/main/java/org/apache/sling/caconfig/management/impl/ConfigurationDataImpl.java                   |
| ConfigurationBuilderImpl.java         | 2              | 0             | 0           | 0      | 2           | 0           | 0            | src/main/java/org/apache/sling/caconfig/impl/ConfigurationBuilderImpl.java                           |
| ConfigurationOverrideMultiplexer.java | 2              | 0             | 0           | 0      | 1           | 0           | 1            | src/main/java/org/apache/sling/caconfig/management/multiplexer/ConfigurationOverrideMultiplexer.java |
| OverrideStringParser.java             | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/caconfig/impl/override/OverrideStringParser.java                      |
| CAConfigInventoryPrinter.java         | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/caconfig/management/impl/console/CAConfigInventoryPrinter.java        |
| ValueInfoImpl.java                    | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/caconfig/management/impl/ValueInfoImpl.java                           |
| -                                     | -              | -             | -           | -      | -           | -           | -            | -                                                                                                    |

## Project 3: _apache/sling-org-apache-sling-servlet-helpers_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-servlet-helpers.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-servlet-helpers) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-servlet-helpers) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-servlet-helpers.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                        | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                      |
|:----------------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:--------------------------------------------------------------------------------|
| MockSlingHttpServletRequest.java  | 2              | 0             | 2           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/servlethelpers/MockSlingHttpServletRequest.java  |
| ResponseBodySupport.java          | 2              | 0             | 2           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/servlethelpers/ResponseBodySupport.java          |
| MockSlingHttpServletResponse.java | 2              | 0             | 0           | 0      | 1           | 0           | 1            | src/main/java/org/apache/sling/servlethelpers/MockSlingHttpServletResponse.java |
| AdaptableUtil.java                | 2              | 0             | 1           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/servlethelpers/AdaptableUtil.java                |
| MockRequestPathInfo.java          | 2              | 0             | 0           | 0      | 1           | 0           | 1            | src/main/java/org/apache/sling/servlethelpers/MockRequestPathInfo.java          |
| -                                 | -              | -             | -           | -      | -           | -           | -            | -                                                                               |
| -                                 | -              | -             | -           | -      | -           | -           | -            | -                                                                               |
| -                                 | -              | -             | -           | -      | -           | -           | -            | -                                                                               |
| -                                 | -              | -             | -           | -      | -           | -           | -            | -                                                                               |
| -                                 | -              | -             | -           | -      | -           | -           | -            | -                                                                               |

## Project 4: _apache/sling-org-apache-sling-testing-jcr-mock_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-testing-jcr-mock.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-testing-jcr-mock) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-testing-jcr-mock) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-testing-jcr-mock.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name        | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                        |
|:------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:------------------------------------------------------------------|
| MockQuery.java    | 3              | 0             | 3           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/testing/mock/jcr/MockQuery.java    |
| MockJcr.java      | 2              | 0             | 2           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/testing/mock/jcr/MockJcr.java      |
| MockRow.java      | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/testing/mock/jcr/MockRow.java      |
| MockProperty.java | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/testing/mock/jcr/MockProperty.java |
| MockNode.java     | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/testing/mock/jcr/MockNode.java     |
| ResourceUtil.java | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/testing/mock/jcr/ResourceUtil.java |
| -                 | -              | -             | -           | -      | -           | -           | -            | -                                                                 |
| -                 | -              | -             | -           | -      | -           | -           | -            | -                                                                 |
| -                 | -              | -             | -           | -      | -           | -           | -            | -                                                                 |
| -                 | -              | -             | -           | -      | -           | -           | -            | -                                                                 |

## Project 5: _apache/sling-org-apache-sling-testing-osgi-mock_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-testing-osgi-mock.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-testing-osgi-mock) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-testing-osgi-mock) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-testing-osgi-mock.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name             |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                         |
|:-----------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:-----------------------------------------------------------------------------------|
| OsgiServiceUtil.java   |             12 |             0 |          12 |      0 |           0 |           0 |            0 | core/src/main/java/org/apache/sling/testing/mock/osgi/OsgiServiceUtil.java         |
| OsgiMetadataUtil.java  |              9 |             0 |           9 |      0 |           0 |           0 |            0 | core/src/main/java/org/apache/sling/testing/mock/osgi/OsgiMetadataUtil.java        |
| MockBundleContext.java |              8 |             0 |           8 |      0 |           0 |           0 |            0 | core/src/main/java/org/apache/sling/testing/mock/osgi/MockBundleContext.java       |
| ContextPlugins.java    |              4 |             0 |           4 |      0 |           0 |           0 |            0 | core/src/main/java/org/apache/sling/testing/mock/osgi/context/ContextPlugins.java  |
| ContextPlugin.java     |              4 |             0 |           4 |      0 |           0 |           0 |            0 | core/src/main/java/org/apache/sling/testing/mock/osgi/context/ContextPlugin.java   |
| MockBundle.java        |              2 |             0 |           2 |      0 |           0 |           0 |            0 | core/src/main/java/org/apache/sling/testing/mock/osgi/MockBundle.java              |
| MockOsgi.java          |              2 |             0 |           2 |      0 |           0 |           0 |            0 | core/src/main/java/org/apache/sling/testing/mock/osgi/MockOsgi.java                |
| ContextCallback.java   |              1 |             0 |           1 |      0 |           0 |           0 |            0 | core/src/main/java/org/apache/sling/testing/mock/osgi/context/ContextCallback.java |
| OsgiContextImpl.java   |              1 |             0 |           1 |      0 |           0 |           0 |            0 | core/src/main/java/org/apache/sling/testing/mock/osgi/context/OsgiContextImpl.java |
| MapMergeUtil.java      |              1 |             0 |           1 |      0 |           0 |           0 |            0 | core/src/main/java/org/apache/sling/testing/mock/osgi/MapMergeUtil.java            |

## Project 6: _apache/sling-org-apache-sling-testing-resourceresolver-mock_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-testing-resourceresolver-mock.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-testing-resourceresolver-mock) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-testing-resourceresolver-mock) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-testing-resourceresolver-mock.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                       | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                               |
|:---------------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:-----------------------------------------------------------------------------------------|
| MockHelper.java                  | 2              | 0             | 0           | 0      | 2           | 0           | 0            | src/main/java/org/apache/sling/testing/resourceresolver/MockHelper.java                  |
| MockResourceResolver.java        | 2              | 0             | 0           | 0      | 1           | 0           | 1            | src/main/java/org/apache/sling/testing/resourceresolver/MockResourceResolver.java        |
| ResourceTypeUtil.java            | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/testing/resourceresolver/ResourceTypeUtil.java            |
| MockValueMap.java                | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/testing/resourceresolver/MockValueMap.java                |
| MockResourceResolverFactory.java | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/testing/resourceresolver/MockResourceResolverFactory.java |
| -                                | -              | -             | -           | -      | -           | -           | -            | -                                                                                        |
| -                                | -              | -             | -           | -      | -           | -           | -            | -                                                                                        |
| -                                | -              | -             | -           | -      | -           | -           | -            | -                                                                                        |
| -                                | -              | -             | -           | -      | -           | -           | -            | -                                                                                        |
| -                                | -              | -             | -           | -      | -           | -           | -            | -                                                                                        |

## Project 7: _apache/sling-org-apache-sling-testing-sling-mock_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-testing-sling-mock.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-testing-sling-mock) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-testing-sling-mock) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-testing-sling-mock.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                          |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                         |
|:------------------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:---------------------------------------------------------------------------------------------------|
| ImmutableValueMap.java              |             10 |             0 |           0 |      0 |           6 |           0 |            4 | core/src/main/java/org/apache/sling/testing/mock/sling/builder/ImmutableValueMap.java              |
| MockJcrSlingRepository.java         |              8 |             0 |           8 |      0 |           0 |           0 |            0 | core/src/main/java/org/apache/sling/testing/mock/sling/MockJcrSlingRepository.java                 |
| SlingContextImpl.java               |              5 |             2 |           1 |      0 |           1 |           0 |            1 | core/src/main/java/org/apache/sling/testing/mock/sling/context/SlingContextImpl.java               |
| ContentLoader.java                  |              4 |             0 |           4 |      0 |           0 |           0 |            0 | core/src/main/java/org/apache/sling/testing/mock/sling/loader/ContentLoader.java                   |
| MockSling.java                      |              4 |             0 |           4 |      0 |           0 |           0 |            0 | core/src/main/java/org/apache/sling/testing/mock/sling/MockSling.java                              |
| MockMimeTypeService.java            |              3 |             0 |           3 |      0 |           0 |           0 |            0 | core/src/main/java/org/apache/sling/testing/mock/sling/services/MockMimeTypeService.java           |
| ContextResourceResolverFactory.java |              3 |             0 |           3 |      0 |           0 |           0 |            0 | core/src/main/java/org/apache/sling/testing/mock/sling/context/ContextResourceResolverFactory.java |
| MockRequestPathInfo.java            |              2 |             0 |           0 |      0 |           1 |           0 |            1 | core/src/main/java/org/apache/sling/testing/mock/sling/servlet/MockRequestPathInfo.java            |
| MockSlingHttpServletRequest.java    |              2 |             2 |           0 |      0 |           0 |           0 |            0 | core/src/main/java/org/apache/sling/testing/mock/sling/servlet/MockSlingHttpServletRequest.java    |
| LoaderContentHandler.java           |              2 |             0 |           2 |      0 |           0 |           0 |            0 | core/src/main/java/org/apache/sling/testing/mock/sling/loader/LoaderContentHandler.java            |

