FROM phopper/obs-base:latest

MAINTAINER DSM

# Which uWSGI .ini file should be used, to make it customizable
ENV UWSGI_INI /app/obs-pdf/public/uwsgi.ini

# URL under which static (not modified by Python) files will be requested
# They will be served by Nginx directly, without being handled by uWSGI
ENV STATIC_URL /output
# Absolute path in where the static files wil be
ENV STATIC_PATH /app/obs-pdf/output
# Timeout in seconds for processing Flask requests
ENV NGINX_TIMEOUT 300

# install the obs-pdf app
RUN cd /app && git clone --single-branch -b master https://github.com/unfoldingWord-dev/obs-pdf.git \
    && cd /app/obs-pdf \
    && git pull \
    && pip install --upgrade pip \
    && pip install --upgrade -r prerequisites.txt \
    && pip install -r requirements.txt

COPY start.sh /start.sh
COPY entrypoint.sh /entrypoint.sh
