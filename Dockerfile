FROM python:3.11-slim
WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt
EXPOSE 8000
COPY ./app /src/app
CMD ["uvicorn", "app/main:app", "--host", "0.0.0.0"]