FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y curl python3 python3-pip python3-dev build-essential
# get install script and pass it to execute:
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash
# and install node
RUN apt-get install nodejs
# confirm that it was successful
RUN node -v
# npm installs automatically
RUN npm -v
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"]

