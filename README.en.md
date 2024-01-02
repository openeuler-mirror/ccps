# ccps

#### introduce

The Container Cloud Platform Solution (CCPS) is an application-centric, enterprise-level container cloud PaaS platform based on Kubernetes, OKD, and CRI-O, which provides functions such as automatic scaling, configuration management, resource management, and automatic operation and maintenance through full-stack automated DevOps workflows, and provides functions such as automatic scaling, configuration management, resource management, and automatic operation and maintenance, so as to realize the full lifecycle management of containerized applications.

#### Product features

From the administrator's perspective, the container cloud management platform solution has functions such as visual management, authentication and authorization, event and log collection, monitoring, and alerting. From a developer's perspective, the container cloud management platform solution has features such as automated container and application build, deployment, scaling, and health management.

#### Software Architecture
- DevOps management tools: Provides a visual web UI and efficient CLI management tools for managing user applications and their own services, and is built using REST APIs that can be used by external tools such as IDEs and CI platforms.
- PaaS Functional Components & Container Images: PaaS functional components run in containers on the container cloud management platform, while application runtime and middleware images provide runtime and middleware support for cloud-native applications running in UnionTech Container Cloud Management Platform.
- Kubernetes & Etcd: As the orchestration and scheduling core of containers, Etcd is a distributed key-value storage database with consistency and high availability, which is used to store configuration and status information about Kubernetes cluster metadata and other resources.
- CRD: Provides an Operator architecture that uses CRDs in Kubernetes to extend the Kubernetes API and declarative management capabilities.
- Basic Operating System Environment: The basic operating system environment of the node machine.

#### Installation tutorial

1.  xxxx
2.  xxxx
3.  xxxx

#### Directions for use

1.  xxxx
2.  xxxx
3.  xxxx

#### Get involved

1.  Fork the repository under the ccps organizationCreate Feat [ccps](https://gitee.com/openeuler/ccps) branch
3.  Create a new Feat_xxx branch
4.  Create Pull Request
4.  Pull Request Create a new pull request


#### Gitee Feature

1.  You can use Readme\_XXX.md to support different languages, such as Readme\_en.md, Readme\_zh.md
2.  Gitee blog [blog.gitee.com](https://blog.gitee.com)
3.  Explore open source project [https://gitee.com/explore](https://gitee.com/explore)
4.  The most valuable open source project [GVP](https://gitee.com/gvp)
5.  The manual of Gitee [https://gitee.com/help](https://gitee.com/help)
6.  The most popular members  [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
