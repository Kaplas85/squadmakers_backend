FROM python:3.10.6
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code/
RUN pip install -U pip && pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]