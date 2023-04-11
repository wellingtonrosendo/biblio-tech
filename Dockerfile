FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-venv
WORKDIR /usr/src/app
ADD ./requirements.txt /usr/src/app/requirements.txt
RUN pip3 install "Flask==1.1.4"
ADD . /usr/src/app
RUN pip3 install --upgrade pip
RUN pip3 install wheel
RUN pip3 install -r requirements.txt

CMD python3 manage.py runserver -h 0.0.0.0