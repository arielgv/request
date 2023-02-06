From python:3.10.9-bullseye

WORKDIR /practices
COPY requirements.txt /practices
RUN pip install --upgrade --no-cache-dir -r requirements.txt
COPY . /practices/

CMD bash -c "while true; do sleep 1; done"
