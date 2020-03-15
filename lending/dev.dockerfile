FROM node:10.16.0

WORKDIR /app
COPY package.json package-lock.json /app/
RUN npm install

RUN npm list --depth=0

COPY ./ /app
RUN cp -r node_modules/ static/

FROM python:3.7

RUN pip3 install --upgrade pip
RUN pip3 install pipenv

WORKDIR /app
COPY ./Pipfile /app/

RUN pipenv install --system --skip-lock

COPY ./ app/
COPY ./static /static/

# ENV FLASK_APP=main.py
# ENV FLASK_DEBUG=1
# ENV FLASK_ENV='development'

EXPOSE 8888
# CMD flask run --host=0.0.0.0 --port=8888
ENTRYPOINT ["python3", "main.py"]
