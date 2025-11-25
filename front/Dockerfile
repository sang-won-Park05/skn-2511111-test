FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 8080

CMD [ "streamlit", "run", "app.py", "--server.address0.0.0.0", "--server.port 8080" ]

