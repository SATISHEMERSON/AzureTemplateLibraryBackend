# Use the tiangolo/uwsgi-nginx:python3.6 base image
FROM tiangolo/uwsgi-nginx:python3.6

# Copy the necessary configuration files
COPY uwsgi.ini /app/uwsgi.ini
COPY nginx.conf /etc/nginx/conf.d/nginx.conf
COPY nginx_base.conf /app/nginx.conf

# Remove the existing SSH file so the system can generate a new one
RUN rm -f /etc/ssh/sshd_config

# Copy the SSH config file
COPY sshd_config /etc/ssh/

# Upgrade pip
RUN pip3 install --upgrade pip

# Set the working directory for the app
WORKDIR /code/

# Copy the requirements file and install dependencies
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt

# Collect static files during the build process
RUN python /code/manage.py collectstatic --noinput

# Do final prep
COPY . /code/
# Convert entrypoint.sh to Unix line endings and make it executable
# RUN apt-get update && apt-get install -y dos2unix && \
#     dos2unix /code/docker/prod/entrypoint.sh && \
#     chmod 755 /code/docker/prod/entrypoint.sh

# Copy the entrypoint.sh script and ensure it has the right line endings and permissions
COPY entrypoint.sh /code/entrypoint.sh

# Convert entrypoint.sh to Unix line endings and make it executable
# RUN apt-get update && apt-get install -y dos2unix && \
#     dos2unix /code/entrypoint.sh && \
#     chmod 755 /code/entrypoint.sh

# Set the ENTRYPOINT for the application to use supervisord
RUN chmod +x /code/entrypoint.sh
# This has to be re-specified even though it's in the base image because we
# overrode entrypoint.
CMD ["/usr/bin/supervisord"]
