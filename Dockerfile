FROM python:3.12-slim

WORKDIR /app

# 安装基础依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制服务源码
COPY server.py .

# 启动 MCP 服务 (stdio 模式)
CMD ["python", "server.py"]
