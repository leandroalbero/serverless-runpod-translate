FROM nvidia/cuda:11.4.0-base-ubuntu20.04

RUN mkdir /app
WORKDIR /app

COPY requirements/ requirements/

RUN apt update
RUN apt-get install -y python3 python3-pip
RUN pip install --upgrade pip
RUN pip install -v pybind11
RUN pip install -r requirements/development/requirements.txt

# Copy the src directory to the working directory
COPY ./ ./

CMD ["python3", "-u", "src/handler.py"]