# Use an official Python runtime as a parent image
FROM python:3.8-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y glpk-utils \
    && pip install -r requirements.txt
# Make port 80 available to the world outside this container
EXPOSE 800

# Define the command to run your application
CMD ["python", "your_app.py"]
# CMD ["tail", "-f", "/dev/null"]
