FROM python:3.5

# Copy the application to image.
ADD . /code
WORKDIR /code

# Install application requirements.
RUN pip install -r requirements.txt

# Run the application.
CMD python app.py
