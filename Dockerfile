FROM tiangolo/uwsgi-nginx:python3.6
#

COPY uwsgi.ini /app/uwsgi.ini
COPY nginx.conf /etc/nginx/conf.d/nginx.conf
COPY nginx_base.conf /app/nginx.conf
# SSH: remove the existing ssh file, so that the system can generate a new file
RUN rm -f /etc/ssh/sshd_config

COPY sshd_config /etc/ssh/
#
RUN pip3 install --upgrade pip

WORKDIR /code/

# Install requirements
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt

# Do final prep
COPY . /code/
# Convert entrypoint.sh to Unix line endings and make it executable
# RUN apt-get update && apt-get install -y dos2unix && \
#     dos2unix /code/docker/prod/entrypoint.sh && \
#     chmod 755 /code/docker/prod/entrypoint.sh

# ENTRYPOINT for supervisord
ENTRYPOINT ["/code/docker/prod/entrypoint.sh"]
# This has to be re-specified even though it's in the base image because we
# overrode entrypoint.
CMD ["/usr/bin/supervisord"]
