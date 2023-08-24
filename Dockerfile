FROM python:3.9

RUN mkdir /app
WORKDIR /app

COPY requirements/ requirements/

RUN pip install --upgrade pip --no-cache-dir && \
    pip install -v pybind11 && \
    pip install -r requirements/development/requirements.txt && \
    rm -r /root/.cache/pip

# Copy the src directory to the working directory
COPY ./ ./

RUN python /cache_models.py && rm /cache_models.py

CMD ["python", "-u", "src/handler.py"]