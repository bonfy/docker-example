FROM python:3.8-alpine

# Add bash
RUN apk update && apk add bash

# Make Dir /log
RUN mkdir /log
VOLUME [ "/log" ]

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
# RUN pip3 install --trusted-host pypi.python.org -r req.txt

CMD ["python3", "app.py"]