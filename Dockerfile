FROM python:3.9

WORKDIR /

RUN pip install -r requirements/develpment/requirements.txt

add src/handler.py .

CMD ["python", "-u", "/src/handler.py"]