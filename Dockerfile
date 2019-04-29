FROM python:3.6.8-alpine3.9
COPY dist /app/dist
COPY server /app/server
WORKDIR /app/server
RUN pip install --upgrade pip --no-cache-dir -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
