# Source Image
FROM python:3.7
# Author
MAINTAINER Leon "leontian1024@gmail.com"
# Set working director
WORKDIR /var/app/userOpers
# Add source code from os into container
Add . /var/app/userOpers
# Import packages
RUN pip install Flask
RUN pip install Flask-wtf
RUN pip install psycopg2-binary
RUN pip install flask-sqlalchemy
RUN pip install flask-migrate
# Expose port
EXPOSE 80
# Run command
ENTRYPOINT ["python","./userOpers.py"]

