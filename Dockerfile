FROM python:3.7-alpine
LABEL maintainer="Sadeeptha Bandara"
# Base image: alpine is lightweight

# Running python in unbuffered mode is recommended for running python in docker containers. Outputs are not buffered.
# This is an environment variable we're setting.
ENV PYTHONUNBUFFERED 1

# Dependencies
# Copy from the file in the directory to a file in the docker image
COPY ./requirements.txt /requirements.txt

# Adding postgres support. psycopg2, the recommended package to communicate between django and postgres has been added to requirements.txt. Before installing it, the following command is required to install necessary dependencies.
# - apk --> The package manager that comes with alpine
# - add --> add package
# - update --> update the registry prior to adding
# - no-cache --> Don't store the registry index on our docker file. This is done to minimize the number of extra files and packages installed in the docker container. 
RUN apk add --update --no-cache postgresql-client

# The following packages are required installing running requirements.txt. They can removed after requirements.txt has been run
# virtual --> Sets up an alias: temp-build-deps for the dependencies so that they can be removed easily later.
# The dependencies referenced by the alias are listed below.
RUN apk add --update --no-cache --virtual .temp-build-deps \
        gcc libc-dev linux-headers postgresql-dev

# Installs the requirements file
RUN pip install -r /requirements.txt    

# remove temporary dependencies.
RUN apk del .temp-build-deps

# Directory within docker image to store app source code
# create empty dir, switch that dir as default, copies the app folder from the local machine to the app folder in the docker image
RUN mkdir /app  
WORKDIR /app
COPY ./app app

# User that will run the app: Create user and switch to the user
# This is done for security because if it is not done, the app will run under the root account of the image. So, we create a user just for the application.
# -D : Create a user for running applications only
RUN adduser -D user
USER user

# To run: docker build . (Will run dockerfile in current dir)



