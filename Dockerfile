FROM arm32v6/python:3.9-alpine as base

RUN apk update
RUN apk add python3-dev
RUN apk add raspberrypi-utils-vcgencmd

WORKDIR /app

ENV FLASK_APP=flaskr

COPY requirements/base.txt ./requirements/base.txt
COPY flaskr ./flaskr

FROM base as testing

COPY requirements/tests.txt ./requirements/tests.txt
RUN pip3 install -r requirements/tests.txt

COPY pytest.ini ./pytest.ini
COPY .coveragerc ./.coveragerc
COPY tests ./tests

RUN ["flake8", "flaskr/"]
RUN ["flake8", "tests/"]

RUN ["coverage", "run", "-m", "pytest", "-m", "unit"]
RUN ["coverage", "run", "-m", "pytest", "-m", "api"]
RUN ["coverage", "report", "--fail-under", "80"]

FROM base as production

RUN pip3 install -r requirements/base.txt

EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
