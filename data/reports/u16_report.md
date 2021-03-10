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
|<p align="center">Project 1</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-api.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-api) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-api) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-api.json)</p>|<p align="center">Project 2</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-jcr-contentloader.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-jcr-contentloader) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-jcr-contentloader) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-jcr-contentloader.json)</p>|<p align="center">Project 3</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-jcr-jackrabbit-accessmanager.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-jcr-jackrabbit-accessmanager) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-jcr-jackrabbit-accessmanager) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-jcr-jackrabbit-accessmanager.json)</p>
 | |
|<p align="center">Project 4</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-jcr-jackrabbit-usermanager.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-jcr-jackrabbit-usermanager) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-jcr-jackrabbit-usermanager) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-jcr-jackrabbit-usermanager.json)</p>|<p align="center">Project 5</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-launchpad-integration-tests.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-launchpad-integration-tests) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-launchpad-integration-tests) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-launchpad-integration-tests.json)</p>|<p align="center">Project 6</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-scripting-core.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-scripting-core) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-scripting-core) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-scripting-core.json)</p>
 | |
|<p align="center">Project 7</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-scripting-javascript.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-scripting-javascript) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-scripting-javascript) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-scripting-javascript.json)</p>|<p align="center">Project 8</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-servlets-resolver.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-servlets-resolver) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-servlets-resolver) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-servlets-resolver.json)</p>|<p align="center">Project 9</p><img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-testing-clients.jpg"/> <p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-testing-clients) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-testing-clients) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-testing-clients.json)</p>

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

## Project 2: _apache/sling-org-apache-sling-jcr-contentloader_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-jcr-contentloader.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-jcr-contentloader) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-jcr-contentloader) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-jcr-contentloader.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name               | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                         |
|:-------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:-----------------------------------------------------------------------------------|
| XmlReader.java           | 14             | 0             | 3           | 0      | 10          | 1           | 0            | src/main/java/org/apache/sling/jcr/contentloader/internal/readers/XmlReader.java   |
| PathEntry.java           | 3              | 3             | 0           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/jcr/contentloader/internal/PathEntry.java           |
| ContentTypeUtil.java     | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/jcr/contentloader/ContentTypeUtil.java              |
| ImportOptions.java       | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/jcr/contentloader/ImportOptions.java                |
| BundleContentLoader.java | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/jcr/contentloader/internal/BundleContentLoader.java |
| -                        | -              | -             | -           | -      | -           | -           | -            | -                                                                                  |
| -                        | -              | -             | -           | -      | -           | -           | -            | -                                                                                  |
| -                        | -              | -             | -           | -      | -           | -           | -            | -                                                                                  |
| -                        | -              | -             | -           | -      | -           | -           | -            | -                                                                                  |
| -                        | -              | -             | -           | -      | -           | -           | -            | -                                                                                  |

## Project 3: _apache/sling-org-apache-sling-jcr-jackrabbit-accessmanager_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-jcr-jackrabbit-accessmanager.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-jcr-jackrabbit-accessmanager) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-jcr-jackrabbit-accessmanager) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-jcr-jackrabbit-accessmanager.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                     | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                                      |
|:-------------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:------------------------------------------------------------------------------------------------|
| AbstractAccessPostServlet.java | 8              | 0             | 0           | 0      | 5           | 0           | 3            | src/main/java/org/apache/sling/jcr/jackrabbit/accessmanager/post/AbstractAccessPostServlet.java |
| ModifyAceServlet.java          | 2              | 1             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/jcr/jackrabbit/accessmanager/post/ModifyAceServlet.java          |
| ModifyAce.java                 | 2              | 0             | 0           | 0      | 2           | 0           | 0            | src/main/java/org/apache/sling/jcr/jackrabbit/accessmanager/ModifyAce.java                      |
| DeleteAcesServlet.java         | 1              | 1             | 0           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/jcr/jackrabbit/accessmanager/post/DeleteAcesServlet.java         |
| -                              | -              | -             | -           | -      | -           | -           | -            | -                                                                                               |
| -                              | -              | -             | -           | -      | -           | -           | -            | -                                                                                               |
| -                              | -              | -             | -           | -      | -           | -           | -            | -                                                                                               |
| -                              | -              | -             | -           | -      | -           | -           | -            | -                                                                                               |
| -                              | -              | -             | -           | -      | -           | -           | -            | -                                                                                               |
| -                              | -              | -             | -           | -      | -           | -           | -            | -                                                                                               |

## Project 4: _apache/sling-org-apache-sling-jcr-jackrabbit-usermanager_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-jcr-jackrabbit-usermanager.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-jcr-jackrabbit-usermanager) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-jcr-jackrabbit-usermanager) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-jcr-jackrabbit-usermanager.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                          |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                            |
|:------------------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:------------------------------------------------------------------------------------------------------|
| AbstractPostServlet.java            |              8 |             0 |           0 |      0 |           5 |           0 |            3 | src/main/java/org/apache/sling/jackrabbit/usermanager/impl/post/AbstractPostServlet.java              |
| AuthorizablePrivilegesInfoImpl.java |              4 |             0 |           4 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/jackrabbit/usermanager/impl/AuthorizablePrivilegesInfoImpl.java        |
| AuthorizableValueMap.java           |              2 |             0 |           2 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/jackrabbit/usermanager/impl/resource/AuthorizableValueMap.java         |
| DeleteAuthorizableServlet.java      |              2 |             2 |           0 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/jackrabbit/usermanager/impl/post/DeleteAuthorizableServlet.java        |
| CreateGroupServlet.java             |              1 |             1 |           0 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/jackrabbit/usermanager/impl/post/CreateGroupServlet.java               |
| ChangeUserPasswordServlet.java      |              1 |             1 |           0 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/jackrabbit/usermanager/impl/post/ChangeUserPasswordServlet.java        |
| CreateUserServlet.java              |              1 |             1 |           0 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/jackrabbit/usermanager/impl/post/CreateUserServlet.java                |
| UpdateUserServlet.java              |              1 |             1 |           0 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/jackrabbit/usermanager/impl/post/UpdateUserServlet.java                |
| UpdateGroupServlet.java             |              1 |             1 |           0 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/jackrabbit/usermanager/impl/post/UpdateGroupServlet.java               |
| AuthorizableResourceProvider.java   |              1 |             1 |           0 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/jackrabbit/usermanager/impl/resource/AuthorizableResourceProvider.java |

## Project 5: _apache/sling-org-apache-sling-launchpad-integration-tests_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-launchpad-integration-tests.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-launchpad-integration-tests) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-launchpad-integration-tests) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-launchpad-integration-tests.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                          |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                                                        |
|:------------------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:------------------------------------------------------------------------------------------------------------------|
| ResourceResolverGeneralTest.java    |             35 |             0 |          33 |      0 |           0 |           0 |            2 | src/main/java/org/apache/sling/launchpad/webapp/integrationtest/resourceresolver/ResourceResolverGeneralTest.java |
| ModifyAceTest.java                  |             23 |             0 |          23 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/launchpad/webapp/integrationtest/accessManager/ModifyAceTest.java                  |
| PostServletImportTest.java          |             20 |             0 |          20 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/launchpad/webapp/integrationtest/servlets/post/PostServletImportTest.java          |
| AuthenticationResponseCodeTest.java |             10 |             0 |          10 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/launchpad/webapp/integrationtest/auth/AuthenticationResponseCodeTest.java          |
| CreateUserTest.java                 |             10 |             0 |           6 |      0 |           0 |           0 |            4 | src/main/java/org/apache/sling/launchpad/webapp/integrationtest/userManager/CreateUserTest.java                   |
| UpdateGroupTest.java                |             10 |             0 |          10 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/launchpad/webapp/integrationtest/userManager/UpdateGroupTest.java                  |
| UserPrivilegesInfoTest.java         |              7 |             0 |           7 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/launchpad/webapp/integrationtest/userManager/UserPrivilegesInfoTest.java           |
| GetAclTest.java                     |              7 |             0 |           7 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/launchpad/webapp/integrationtest/accessManager/GetAclTest.java                     |
| AccessPrivilegesInfoTest.java       |              7 |             0 |           7 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/launchpad/webapp/integrationtest/accessManager/AccessPrivilegesInfoTest.java       |
| JspScriptingTest.java               |              6 |             0 |           6 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/launchpad/webapp/integrationtest/JspScriptingTest.java                             |

## Project 6: _apache/sling-org-apache-sling-scripting-core_
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

## Project 7: _apache/sling-org-apache-sling-scripting-javascript_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-scripting-javascript.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-scripting-javascript) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-scripting-javascript) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-scripting-javascript.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                        | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                                     |
|:----------------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:-----------------------------------------------------------------------------------------------|
| EspReader.java                    | 9              | 9             | 0           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/scripting/javascript/io/EspReader.java                          |
| ScriptableResource.java           | 6              | 0             | 0           | 0      | 3           | 0           | 3            | src/main/java/org/apache/sling/scripting/javascript/wrapper/ScriptableResource.java            |
| SlingGlobal.java                  | 3              | 0             | 0           | 0      | 0           | 0           | 3            | src/main/java/org/apache/sling/scripting/javascript/helper/SlingGlobal.java                    |
| ScriptableNode.java               | 2              | 0             | 2           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/scripting/javascript/wrapper/ScriptableNode.java                |
| RhinoJavaScriptEngineFactory.java | 1              | 1             | 0           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/scripting/javascript/internal/RhinoJavaScriptEngineFactory.java |
| -                                 | -              | -             | -           | -      | -           | -           | -            | -                                                                                              |
| -                                 | -              | -             | -           | -      | -           | -           | -            | -                                                                                              |
| -                                 | -              | -             | -           | -      | -           | -           | -            | -                                                                                              |
| -                                 | -              | -             | -           | -      | -           | -           | -            | -                                                                                              |
| -                                 | -              | -             | -           | -      | -           | -           | -            | -                                                                                              |

## Project 8: _apache/sling-org-apache-sling-servlets-resolver_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-servlets-resolver.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-servlets-resolver) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-servlets-resolver) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-servlets-resolver.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name                           | Total issues   | Inheritance   | Exception   | JVMS   | Interface   | Threading   | Complexity   | Fully qualified class name                                                                                    |
|:-------------------------------------|:---------------|:--------------|:------------|:-------|:------------|:------------|:-------------|:--------------------------------------------------------------------------------------------------------------|
| SlingScriptResolverImpl.java         | 3              | 0             | 1           | 0      | 1           | 0           | 1            | src/main/java/org/apache/sling/servlets/resolver/internal/SlingScriptResolverImpl.java                        |
| ScriptResourceResolver.java          | 2              | 2             | 0           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/servlets/resolver/internal/ScriptResourceResolver.java                         |
| LocationIterator.java                | 1              | 1             | 0           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/servlets/resolver/internal/helper/LocationIterator.java                        |
| ResolutionCache.java                 | 1              | 0             | 1           | 0      | 0           | 0           | 0            | src/main/java/org/apache/sling/servlets/resolver/internal/resolution/ResolutionCache.java                     |
| BundledRenderUnitCapabilityImpl.java | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/servlets/resolver/bundle/tracker/internal/BundledRenderUnitCapabilityImpl.java |
| ResourceCollector.java               | 1              | 0             | 0           | 0      | 1           | 0           | 0            | src/main/java/org/apache/sling/servlets/resolver/internal/helper/ResourceCollector.java                       |
| -                                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                                             |
| -                                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                                             |
| -                                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                                             |
| -                                    | -              | -             | -           | -      | -           | -           | -            | -                                                                                                             |

## Project 9: _apache/sling-org-apache-sling-testing-clients_
|<img src="https://github.com/S2-group/ATDx_reports/blob/master/plots/apache_sling-org-apache-sling-testing-clients.jpg"/>|<p style="text-align:left">[Project on Github](https://github.com/apache/sling-org-apache-sling-testing-clients) <br> [Project on SonarCloud ](https://sonarcloud.io/dashboard?id=apache_sling-org-apache-sling-testing-clients) <br> [Complete issue report (JSON)](https://github.com/S2-group/ATDx_reports/blob/master/jsons/apache_sling-org-apache-sling-testing-clients.json)</p>
|-|-|
### Top classes with architectural debt violations
| Class name               |   Total issues |   Inheritance |   Exception |   JVMS |   Interface |   Threading |   Complexity | Fully qualified class name                                                     |
|:-------------------------|---------------:|--------------:|------------:|-------:|------------:|------------:|-------------:|:-------------------------------------------------------------------------------|
| AbstractSlingClient.java |             12 |             0 |           8 |      0 |           2 |           0 |            2 | src/main/java/org/apache/sling/testing/clients/AbstractSlingClient.java        |
| OsgiConsoleClient.java   |             10 |             0 |           0 |      0 |           5 |           0 |            5 | src/main/java/org/apache/sling/testing/clients/osgi/OsgiConsoleClient.java     |
| SlingClient.java         |              6 |             0 |           0 |      0 |           3 |           0 |            3 | src/main/java/org/apache/sling/testing/clients/SlingClient.java                |
| SlingHttpResponse.java   |              4 |             0 |           4 |      0 |           0 |           0 |            0 | src/main/java/org/apache/sling/testing/clients/SlingHttpResponse.java          |
| BundlesInstaller.java    |              2 |             0 |           0 |      0 |           1 |           0 |            1 | src/main/java/org/apache/sling/testing/clients/osgi/BundlesInstaller.java      |
| TimeoutsProvider.java    |              2 |             0 |           0 |      0 |           1 |           0 |            1 | src/main/java/org/apache/sling/testing/clients/util/TimeoutsProvider.java      |
| PathPoller.java          |              2 |             0 |           0 |      0 |           1 |           0 |            1 | src/main/java/org/apache/sling/testing/clients/util/poller/PathPoller.java     |
| AbstractPoller.java      |              2 |             0 |           0 |      0 |           1 |           0 |            1 | src/main/java/org/apache/sling/testing/clients/util/poller/AbstractPoller.java |
| Poller.java              |              2 |             0 |           0 |      0 |           1 |           0 |            1 | src/main/java/org/apache/sling/testing/clients/util/poller/Poller.java         |
| OsgiInstanceConfig.java  |              2 |             0 |           0 |      0 |           1 |           0 |            1 | src/main/java/org/apache/sling/testing/clients/osgi/OsgiInstanceConfig.java    |

