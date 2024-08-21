FROM python:3.10

# Install Git and other dependencies
RUN apt-get update && \
    apt-get install -y git python3-venv && \
    apt-get clean

WORKDIR /app

# Clone the GitHub repository
RUN git clone https://github.com/at-sso/AWS-Tests.git .

# Set up a virtual environment and install dependencies
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir -r ./env/requirements.txt

# Set environment variables for Flask
ENV FLASK_APP=./zperk.t4/manage.py
ENV FLASK_ENV=development

# Initialize the database within the Flask app context
# RUN . venv/bin/activate && \
#     flask db init && \
#     flask db migrate -m "Init" && \
#     flask db upgrade
# ^ I do not feel like fixing this

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the application
CMD ["sh", "-c", ". venv/bin/activate && flask run --host=0.0.0.0"]
