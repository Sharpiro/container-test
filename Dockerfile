FROM python:3

WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# # Install any needed packages specified in requirements.txt
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

# # Make port 80 available to the world outside this container
# EXPOSE 80

# Define environment variable
ENV TEST_ENV "here is my variable"

# Run app.py when the container launches
# CMD ["python", "main.py"]
# CMD ["python", "-m", "http.server", "5678"]
CMD ["python", "main.py"]
