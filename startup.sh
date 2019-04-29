#!/usr/bin/env bash
echo "正在构建前端项目..."
cd client && yarn build && cd -;
echo "正在生成后端依赖..."
cd server && pipenv lock -r > requirements.txt && cd -;
echo "正在构建docker镜像..."
docker build -t quick-start:latest .;
echo "正在启动应用..."
docker stop quick-start && docker rm quick-start;
docker run --name quick-start -p 8000:5000 -d quick-start;
exit 0;