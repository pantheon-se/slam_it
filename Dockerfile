FROM python:3.8

# Set the working directory
WORKDIR /locust

# Copy your Locust script and requirements file
COPY locustfile.py .
COPY load_test.py .

# Install any dependencies
RUN pip install locust

# Expose the Locust master web UI port
EXPOSE 8089

# Start the Locust master
CMD ["locust", "--host=https://dev-dunder-mifflin-drupal.pantheonsite.io"]
