FROM python:3.10-slim-bullseye

WORKDIR /flask-docker

RUN python3 -m pip install --upgrade pip 
COPY requirements.txt requirements.txt 
RUN pip3 install -r requirements.txt 

COPY . .

#can also use CMD flask run
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
