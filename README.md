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
```bash
alembic upgrade head
```

### Step 4: Run the Application
Launch the FastAPI server:
```bash
fastapi dev app/main.py
```
The interactive API documentation (Swagger UI) will be automatically generated and accessible at: `http://127.0.0.1:8000/docs`.
```

---

### 2. 如何应付过时的课程设计答辩

大学老旧的课程设计通常还在要求使用 JSP、Servlet 或者传统的 Spring MVC，配合本地 session 和本地图片上传。你拿这套包含 FastAPI、MinIO 和全异步 SQLAlchemy 的代码上去，老师可能第一眼看不懂。

**答辩核心话术：主打“业界标准”与“痛点解决”。**

* **当老师问：“为什么不用传统的 Session 而用 JWT？”**
    回答重点：传统 Session 会在服务器内存中堆积，不仅增加服务器负担，而且在分布式部署时存在跨域和共享问题。采用 JWT 实现无状态认证，是目前业界微服务和前后端分离架构的绝对主流。
* **当老师问：“为什么要多此一举用 MinIO，直接传到项目的 static 文件夹不行吗？”**
    回答重点：将文件存在本地会导致项目体积臃肿，且扩展服务器时文件无法同步。引入 MinIO 搭建本地对象存储，是为了模拟云原生环境（如 AWS S3 或阿里云 OSS），实现了计算与存储的物理隔离。
* **当老师问：“这个 FastAPI 和传统的框架有什么区别？”**
    回答重点：FastAPI 基于 ASGI（异步服务器网关接口）。传统的同步框架（如老版本的 Flask 或 Spring）是一个请求占用一个线程，高并发时会因线程切换耗尽资源；而本项目使用单线程事件循环配合 `aiomysql`，能以极低的内存占用处理海量并发请求。

### 3. 如何撰写差异化的课程设计报告（拿高分策略）

不要把报告写成简单的“功能说明书”，要写成**“架构演进与安全性分析报告”**，特别是在信息安全专业的背景下，你可以把重点放在安全和性能防御上：

**第一章：架构设计与选型分析**
* 对比老旧的 MVC 架构，画一张前后端分离的架构图。
* 强调 Python 3.14 JIT 特性结合 FastAPI 带来的性能飞跃，体现你对底层运行效率的追求。

**第二章：信息安全与防御机制（报告的核心亮点）**
* **认证安全**：详细描述代码中使用的 `bcrypt.gensalt()` 机制。解释为什么单纯的 MD5 已经不安全，以及 bcrypt 如何通过加盐和动态计算代价来防御彩虹表攻击和暴力破解。
* **接口防泄漏**：展示 `Pydantic` schema 的隔离设计（如代码中的 `UserOut` 不含密码），说明如何从框架层杜绝敏感字段的意外序列化。
* **注入防御**：说明 `SQLAlchemy` ORM 是如何通过参数化查询彻底杜绝 SQL 注入的。

**第三章：云原生存储的最佳实践**
* 在这一章贴出你的 `docker-compose.yml`，解释容器化部署的优势。
* 描述引入 MinIO 解决单点故障和文件持久化的问题，展示你的项目不仅能在一台笔记本上跑，更能随时上云部署。

这样写报告，评委老师看到的就不是一个普通的“大作业”，而是一个完全具备企业级思维、注重底层性能，且深谙信息安全规范的现代化系统。
