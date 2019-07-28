FROM python:3

WORKDIR /app

# Copy the current directory contents into the container at /app
# COPY main.py simple-main.py requirements.txt /app/
COPY simple-main.py /app/

# # Install any needed packages specified in requirements.txt
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

# # Make port 80 available to the world outside this container
# EXPOSE 80

# Define environment variable
ENV PORT 80

EXPOSE 80

# Run app.py when the container launches
# CMD ["python", "main.py"]
# CMD ["python", "-m", "http.server", "5678"]
CMD ["python", "simple-main.py"]
