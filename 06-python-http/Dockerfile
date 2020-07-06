FROM python:3.8-alpine

# Add bash
# RUN apk update && apk add bash

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install -r req.txt

EXPOSE 8888

CMD ["python3", "app.py"]