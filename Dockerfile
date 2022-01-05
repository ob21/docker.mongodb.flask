FROM python:3
ADD . /todo
WORKDIR /todo
RUN pip install --no-cache-dir -r requirements.txt
RUN python --version
