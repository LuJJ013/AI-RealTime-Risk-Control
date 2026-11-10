# AI 实时风控平台

一个以 Python 和 AI Agent 为基础的大数据实时风控学习项目。项目目标架构包含 Kafka、Spark / Flink、风控规则与 AI 模型、Redis / MySQL / ClickHouse、FastAPI、Vue 3 和 AI Agent。

目前代码处于后端基础阶段，提供 FastAPI 示例接口、API 健康检查和 MySQL 连通性检查。完整目标与分阶段计划见 [`docs/项目需求.md`](docs/项目需求.md)。

## 环境要求

- Python 3.12 或兼容版本
- MySQL（仅调用 `/health/db` 时需要）

## 本地运行

在项目根目录执行：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```

打开 `http://127.0.0.1:8000/docs` 查看并调用 API。

## 数据库配置

数据库连接通过 `DATABASE_URL` 环境变量配置。PowerShell 示例：

```powershell
$env:DATABASE_URL = "mysql+pymysql://用户名:密码@localhost:3306/ai_bigdata"
uvicorn main:app --reload
```

请使用自己的本地数据库账号信息，不要把真实密码写入代码或提交到 GitHub。

## 当前接口

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| GET | `/` | 项目状态 |
| GET | `/hello` | FastAPI 示例接口 |
| GET | `/health` | 检查 API 进程是否运行 |
| GET | `/health/db` | 检查数据库连通性；未连接时返回 HTTP 503 |

## 项目目录

```text
AI_bigdata/
├── database/          # 数据库连接
├── docs/              # 项目需求与说明文档
├── models/            # 数据模型
├── main.py            # FastAPI 应用入口
├── requirements.txt   # Python 依赖
└── Agents.md          # 项目协作与学习要求
```

## 学习方式

项目按小步骤实现。每次代码改动应有聚焦的 Git commit；代码、架构、接口或运行方式变化时，同步更新相关文档。
