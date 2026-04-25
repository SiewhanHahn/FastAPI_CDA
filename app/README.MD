```plaintext
portfolio-backend/
├── app/
│   ├── api/          # 路由逻辑 (v1)
│   ├── core/         # 配置与安全 (JWT, Config)
│   ├── models/       # SQLAlchemy 异步模型
│   ├── schemas/      # Pydantic 类型定义
│   └── main.py       # 程序入口
├── tests/            # 自动化测试
├── .env              # 环境变量 (信安规范：不进入 Git)
└── docker-compose.yml
```
