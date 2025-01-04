FROM ubuntu:latest

ENTRYPOINT ["top", "-b"]
# Use an official Python runtime as a parent image
#FROM python:3.8-slim

# Metadata indicating an image maintainer
LABEL maintainer=""

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run behave tests when the container launches
# CMD instruction should be used to run the software
# contained by your image, along with any arguments.
CMD ["behave"]