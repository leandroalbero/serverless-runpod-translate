FROM python:3.9

WORKDIR /

RUN pip install -r requirements/development/requirements.txt

add src/handler.py .

CMD ["python", "-u", "/src/handler.py"]