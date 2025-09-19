FROM docker.io/nginx
VOLUME /certs
VOLUME /mirror
VOLUME /log

RUN openssl req -x509 -newkey rsa:4096 -keyout /certs/key.pem -out /certs/cert.pem -sha256 -days 3650 -nodes -subj "/C=eu/ST=state/L=city/O=mirror/OU=mirror/CN=mirror"

COPY default.conf /etc/nginx/conf.d/default.conf  

EXPOSE 80
EXPOSE 443
