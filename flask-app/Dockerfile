# This Dockerfile is the Dockerfile for the test version
# Install python 
FROM python:3.8.15

# Add app in directory : /usr/src/app
ADD . /usr/src/app

# Go into the folder that is just being created
WORKDIR /usr/src/app

# Install depedencies of python
RUN pip install --no-cache-dir -r requirements.txt
# Delete folder that can mess up apt-get update
RUN rm -rf /var/lib/apt/lists/*
# Updates
RUN apt-get update -y && apt-get upgrade -y

# Note : You can run all of the "RUN" command in one line.
# I separated them for some clarification

# No need to install npm to install nodemon since we won't use nodemon in the test version
# Install npm
# RUN apt-get install npm -y
# Install nodemon
# RUN npm install -g nodemon

# Port 5000
EXPOSE 5000

# Run the app
CMD [ "python", "./app.py" ]