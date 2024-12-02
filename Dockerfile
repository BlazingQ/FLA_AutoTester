# 使用 Ubuntu 22.04 基础镜像
FROM ubuntu:22.04

# 更换为阿里云镜像
RUN sed -i 's|archive.ubuntu.com|mirrors.aliyun.com|g' /etc/apt/sources.list && \
    sed -i 's|security.ubuntu.com|mirrors.aliyun.com|g' /etc/apt/sources.list

# 更新系统并安装必要工具
RUN apt-get update && apt-get install -y \
    python3 python3-pip cmake make g++ \
    --fix-missing \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 安装 Flask
RUN pip3 install flask -i https://pypi.tuna.tsinghua.edu.cn/simple

# 设置工作目录
WORKDIR /app

# 复制 Flask 应用代码和其他文件
COPY . .

# 暴露 Flask 服务的端口
EXPOSE 5000

# 启动 Flask 应用
CMD ["python3", "server.py"]
