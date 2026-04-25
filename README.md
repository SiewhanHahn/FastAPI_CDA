# Modern Personal Blog API - Course Design Project

## Overview

This project is a high-performance, RESTful API backend for a personal blog system, developed independently as a course design project. Breaking away from traditional monolithic MVC architectures, this system adopts a modern frontend-backend separation paradigm. It is engineered with asynchronous I/O, robust security protocols, and cloud-native storage solutions, strictly adhering to current industry standards.

## Core Features

* **Authentication & Security**: Stateless user authentication using JWT (JSON Web Tokens) with robust password hashing via `bcrypt`.
* **Asynchronous Database Operations**: Fully async database interactions using `SQLAlchemy 2.0` and `aiomysql` to maximize concurrency.
* **Cloud-Native Storage**: Integration with `MinIO` for distributed object storage, replacing traditional local file system uploads.
* **Data Validation**: Strict request/response schema validation and serialization using `Pydantic`.
* **Version Control for DB**: Database schema migrations managed automatically by `Alembic`.

## Technology Stack

* **Language**: Python 3.14+ (Leveraging JIT compiler for enhanced performance)
* **Framework**: FastAPI
* **Database**: MySQL 8.0 (Async)
* **Object Storage**: MinIO
* **Containerization**: Docker & Docker Compose

## Quick Start & Deployment

### Prerequisites

Ensure `Docker`, `docker-compose`, and Python 3.14 are installed on your environment.

### Step 1: Infrastructure Setup

Start the MySQL and MinIO instances using the provided Docker Compose configuration:

```bash
docker-compose up -d
```

*Note: MySQL will be exposed on port 3306, and MinIO API on port 9000.*

### Step 2: Environment Configuration

Create a virtual environment and install the required dependencies:

```bash
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Step 3: Database Migration

Initialize the database tables using Alembic:

```Bash
alembic upgrade head
```

### Step 4: Run the Application

Launch the FastAPI server:

```bash
fastapi dev app/main.py
```

The interactive API documentation (Swagger UI) will be automatically generated and accessible at: `http://127.0.0.1:8000/docs`.

---

## 2. How to Handle Outdated Course Design Defenses

Legacy university course designs often still require JSP, Servlets, or traditional Spring MVC, along with local sessions and local image uploads. When you present this code featuring FastAPI, MinIO, and fully asynchronous SQLAlchemy, the professors might not understand it at first glance.

**Core Defense Narrative: Focus on "Industry Standards" and "Solving Pain Points".**

- **When asked: "Why use JWT instead of traditional Sessions?"**

  *Key Response:* Traditional Sessions pile up in server memory, increasing the server's load and causing cross-domain and sharing issues during distributed deployment. Adopting JWT for stateless authentication is the absolute mainstream in current industry microservices and frontend-backend separated architectures.
- **When asked: "Why go through the trouble of using MinIO instead of just uploading to the project's static folder?"**

  *Key Response:* Storing files locally leads to a bloated project size, and files cannot be synchronized when scaling servers. Introducing MinIO to build local object storage simulates a cloud-native environment (like AWS S3 or Aliyun OSS), achieving physical isolation of computing and storage.
- **When asked: "What is the difference between FastAPI and traditional frameworks?"**

  *Key Response:* FastAPI is based on ASGI (Asynchronous Server Gateway Interface). Traditional synchronous frameworks (like older versions of Flask or Spring) tie up one thread per request, which can exhaust resources due to thread switching during high concurrency. In contrast, this project uses a single-threaded event loop combined with `aiomysql`, capable of handling massive concurrent requests with an extremely low memory footprint.

## 3. How to Write a Differentiated Course Design Report (High-Scoring Strategy)

Do not write the report as a simple "functional manual." Frame it as an **"Architecture Evolution and Security Analysis Report."** Especially given your Information Security background, you can focus heavily on security and performance defenses:

**Chapter 1: Architecture Design and Selection Analysis**

- Compare it with the legacy MVC architecture by drawing a frontend-backend separation architecture diagram.
- Emphasize the performance leap brought by the Python 3.14 JIT compiler combined with FastAPI, demonstrating your pursuit of low-level execution efficiency.

**Chapter 2: Information Security and Defense Mechanisms (The Core Highlight)**

- **Authentication Security**: Detail the `bcrypt.gensalt()` mechanism used in the code. Explain why plain MD5 is no longer secure, and how bcrypt defends against rainbow tables and brute-force attacks through salting and dynamically calculated costs.
- **Data Leakage Prevention**: Showcase the isolated design of `Pydantic` schemas (e.g., the `UserOut` schema that excludes passwords), explaining how it prevents accidental serialization of sensitive fields at the framework level.
- **Injection Defense**: Explain how the `SQLAlchemy` ORM completely eliminates SQL injection through parameterized queries.

**Chapter 3: Best Practices for Cloud-Native Storage**

- Paste your `docker-compose.yml` in this chapter to explain the advantages of containerized deployment.
- Describe how introducing MinIO solves single points of failure and file persistence issues, showing that your project can not only run locally but is also ready for cloud deployment at any time.

---

---

> # 现代个人博客 API - 课程设计项目
>
> ## 简介
>
> 本项目是一个高性能、RESTful 风格的个人博客系统后端 API，作为课程设计独立开发。打破传统的单体 MVC 架构，本系统采用现代的前后端分离范式。它结合了异步 I/O、强大的安全协议和云原生存储解决方案，严格遵循当前的业界标准。
>
> ## 核心特性
>
> - **认证与安全**：使用 JWT（JSON Web Tokens）进行无状态用户认证，并结合 `bcrypt` 进行强大的密码哈希处理。
> - **异步数据库操作**：使用 `SQLAlchemy 2.0` 和 `aiomysql` 实现全异步的数据库交互，最大化并发性能。
> - **云原生存储**：集成 `MinIO` 用于分布式对象存储，取代传统的本地文件系统上传。
> - **数据校验**：使用 `Pydantic` 进行严格的请求/响应 Schema 校验和序列化。
> - **数据库版本控制**：由 `Alembic` 自动管理数据库结构的迁移。
>
> ## 技术栈
>
> - **语言**：Python 3.14+（利用 JIT 编译器提升性能）
> - **框架**：FastAPI
> - **数据库**：MySQL 8.0 (异步)
> - **对象存储**：MinIO
> - **容器化**：Docker & Docker Compose
>
> ## 快速启动与部署
>
> ### 前置要求
>
> 确保你的环境中已安装 `Docker`、`docker-compose` 和 Python 3.14。
>
> 以下命令针对懒人（windows11）:
>
> 1. 安装 wsl2：安装完成 wsl2 后请重启电脑
>
>    ```powershell
>    winget install Microsoft.WSL
>    ```
> 2. 安装 Docker Desktop 和 Docker Compose：
>
>    - 安装完成后，启动 Docker Desktop。
>    - 在初始设置中，确保勾选了 "Use the WSL 2 based engine"。
>
>    ```powershell
>    winget install Docker.DockerDesktop
>    ```
> 3. 安装 Python 3.14
>
>    ```powershell
>    winget install --id Python.Python.3.14
>    ```
>
> ### 第一步：基础设施搭建
>
> 使用提供的 Docker Compose 配置启动 MySQL 和 MinIO 实例：
>
> ```Bash
> docker-compose up -d
> ```
> *注意：MySQL 将暴露在 3306 端口，MinIO API 在 9000 端口。*
>
> ### 第二步：环境配置
>
> 创建虚拟环境并安装所需的依赖项：
>
>> 如果使用的 PyCharm 版本 > 25年，激活虚拟环境可以跳过。
>>
>
> ```Bash
> # 激活虚拟环境
> py -3.14 -m venv .venv
> .\.venv\Scripts\Activate.ps1
>
> # 安装依赖包
> pip install -r requirements.txt
> ```
> ### 第三步：数据库迁移
>
> 使用 Alembic 初始化数据库表结构：
>
> ```Bash
> alembic upgrade head
> ```
> ### 第四步：运行应用程序
>
> 启动 FastAPI 服务器：
>
> ```Bash
> fastapi dev app/main.py
> ```
> 交互式 API 文档（Swagger UI）将自动生成，访问地址为：`http://127.0.0.1:8000/docs`。
>
> ---
>
> ### 2. 如何应付过时的课程设计答辩
>
> 大学老旧的课程设计通常还在要求使用 JSP、Servlet 或者传统的 Spring MVC，配合本地 session 和本地图片上传。你拿这套包含 FastAPI、MinIO 和全异步 SQLAlchemy 的代码上去，老师可能第一眼看不懂。
>
> **答辩核心话术：主打“业界标准”与“痛点解决”。**
>
> - **当老师问：“为什么不用传统的 Session 而用 JWT？”**
>
>   回答重点：传统 Session 会在服务器内存中堆积，不仅增加服务器负担，而且在分布式部署时存在跨域和共享问题。采用 JWT 实现无状态认证，是目前业界微服务和前后端分离架构的绝对主流。
> - **当老师问：“为什么要多此一举用 MinIO，直接传到项目的 static 文件夹不行吗？”**
>
>   回答重点：将文件存在本地会导致项目体积臃肿，且扩展服务器时文件无法同步。引入 MinIO 搭建本地对象存储，是为了模拟云原生环境（如 AWS S3 或阿里云 OSS），实现了计算与存储的物理隔离。
> - **当老师问：“这个 FastAPI 和传统的框架有什么区别？”**
>
>   回答重点：FastAPI 基于 ASGI（异步服务器网关接口）。传统的同步框架（如老版本的 Flask 或 Spring）是一个请求占用一个线程，高并发时会因线程切换耗尽资源；而本项目使用单线程事件循环配合 `aiomysql`，能以极低的内存占用处理海量并发请求。
>
> ### 3. 如何撰写差异化的课程设计报告（拿高分策略）
>
> 不要把报告写成简单的“功能说明书”，要写成**“架构演进与安全性分析报告”**，特别是在信息安全专业的背景下，你可以把重点放在安全和性能防御上：
>
> **第一章：架构设计与选型分析**
>
> - 对比老旧的 MVC 架构，画一张前后端分离的架构图。
> - 强调 Python 3.14 JIT 特性结合 FastAPI 带来的性能飞跃，体现你对底层运行效率的追求。
>
> **第二章：信息安全与防御机制（报告的核心亮点）**
>
> - **认证安全**：详细描述代码中使用的 `bcrypt.gensalt()` 机制。解释为什么单纯的 MD5 已经不安全，以及 bcrypt 如何通过加盐和动态计算代价来防御彩虹表攻击和暴力破解。
> - **接口防泄漏**：展示 `Pydantic` schema 的隔离设计（如代码中的 `UserOut` 不含密码），说明如何从框架层杜绝敏感字段的意外序列化。
> - **注入防御**：说明 `SQLAlchemy` ORM 是如何通过参数化查询彻底杜绝 SQL 注入的。
>
> **第三章：云原生存储的最佳实践**
>
> - 在这一章贴出你的 `docker-compose.yml`，解释容器化部署的优势。
> - 描述引入 MinIO 解决单点故障和文件持久化的问题，展示你的项目不仅能在一台笔记本上跑，更能随时上云部署。
>
> 这样写报告，评委老师看到的就不是一个普通的“大作业”，而是一个完全具备企业级思维、注重底层性能，且深谙信息安全规范的现代化系统。
