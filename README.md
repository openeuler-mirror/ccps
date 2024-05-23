# CCPS

#### 介绍
容器云管理平台解决方案（CCPS）是以 Kubernetes、OKD、CRI-O为基础，以应用为中心的企业级容器云 PaaS 平台，通过全栈自动化操作的 DevOps 工作流，对接各种基础架构的方法，提供自动伸缩、配置管理、资源管理、自动运维等功能，实现对容器化应用的
全生命周期管理。  

#### 产品功能
对于管理员视角，容器云管理平台解决方案具有可视化管理、身份验证和授权、事件和日志收集、监控和报警等功能；对于开发者视角，容器云管理平台解决方案具有自动化的容器和应用构建、部署、扩展、运行状况管理等功能。

#### 软件架构
+ DevOps 管理工具： 提供用于管理用户应用程序和自身服务的可视化 Web UI 和高效的 CLI 管理工具，并使用 REST API 构建，可被 IDE 和 CI 平台等外部工具使用。
+ PaaS 功能组件&容器镜像：PaaS 功能组件以容器方式于容器云管理平台上运行，应用程序运行时及中间件镜像则为运行在统信容器云管理平台中的云原生应用提供运行环境和中间件支持。
+ Kubernetes & Etcd：Kubernetes 作为容器的编排和调度核心，Etcd 是兼具一致性和高可用性的分布式键值存储数据库，用来存储有关 Kubernetes 集群元数据和其他资源的配置和状态信息。
+ CRD：提供 Operator 架构，其使用了 Kubernetes 中的 CRD，扩展了 Kubernetes API 和声明性管理功能。
+ 基础操作系统环境：节点机器的基础操作系统环境。


#### 安装教程（本地部署）

本地集群用于开发和测试目的，不要将其用于生产。欢迎您使用、[提交 PR](https://gitee.com/openeuler/ccps#%E5%8F%82%E4%B8%8E%E8%B4%A1%E7%8C%AE) 或 [反馈问题](mailto:jizongyao@uniontech.com)~！

##### 本地部署与生产环境安装的差异

本地部署的 CCPS 预设提供了常规 CCPS 安装，但具有以下显著差异：
- CCPS 集群是临时集群，不适用于生产用途。
- 不支持升级到较新的 CCPS 版本。
- 它使用单个节点，该节点既充当控制平面又充当工作节点。
- 默认情况下，它会禁用 Cluster Monitoring Operator。该禁用的 Operator 会导致 Web 控制台的相应部分无法运行。
- CCPS 集群在称为实例的虚拟机中运行。这可能会导致其他差异，特别是在外部网络方面。

本地部署提供的 CCPS 集群还包括以下不可自定义的集群设置。不应修改这些设置：
- *.crc.testing域。
- 用于内部集群通信的地址范围。
- 集群使用172地址范围。例如，当代理在同一地址空间中运行时，这可能会导致问题。

##### 开始部署

###### 最小系统资源

- 4 个物理 CPU 核心
- 9 GB 可用内存
- 35 GB 存储空间

###### 安装

1.  下载和配置可移植可执行文件。
```bash
$ wget ​registry.uniontech.com/crc/latest/crc-linux-amd64.tar.xz
$ tar xvf crc-linux-amd64.tar.xz
$ mkdir -p ~/bin
$ cp crc-linux-amd64/crc ~/bin
$ export PATH=$PATH:$HOME/bin
$ echo 'export PATH=$PATH:$HOME/bin' >> ~/.bashrc
```
2.  配置环境。
```bash
$ crc setup
```

#### 使用说明

1.  启动实例，集群至少需要四分钟来启动必要的容器和 Operator。
```bash
$ crc start
```
2. 访问 web 控制台
要使用默认 Web 浏览器访问 CCPS Web 控制台，请运行以下命令：
```bash
$ crc console
```
查看 kubeadmin 和用户 developer 的密码，请运行以下命令：
```bash
$ crc console --credentials
```
3.  停止实例
```bash
$ crc stop
```
4.  删除实例
```bash
$ crc delete
```

#### 参与贡献

1.  Fork [ccps](https://gitee.com/ccps) 组织下的仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request

