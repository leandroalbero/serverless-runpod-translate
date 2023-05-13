FROM python:3.9

RUN mkdir /app
WORKDIR /app

COPY requirements/ requirements/

RUN pip install --upgrade pip
RUN pip install -r requirements/development/requirements.txt

# Copy the src directory to the working directory
COPY ./ ./

CMD ["python", "-u", "src/handler.py"]