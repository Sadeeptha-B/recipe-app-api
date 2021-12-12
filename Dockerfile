FROM python:3.7-alpine
LABEL maintainer="Sadeeptha Bandara"
# Base image: alpine is lightweight

# Running python in unbuffered mode is recommended for running python in docker containers. Outputs are not buffered.
# This is an environment variable we're setting.
ENV PYTHONUNBUFFERED 1

# Dependencies
# Copy from the file in the directory to a file in the docker image
COPY ./requirements.txt /requirements.txt

# Installs the requirements file
RUN pip install -r /requirements.txt    

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



