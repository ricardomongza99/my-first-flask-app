FROM python:3.10-alpine

WORKDIR /app

COPY . .

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_ENV=production

CMD ["flask", "run", "--host", "0.0.0.0"]