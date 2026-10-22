FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
 && apt-get install -y --no-install-recommends apache2 \
 && rm -rf /var/lib/apt/lists/*
COPY web/index.html /var/www/html/index.html
EXPOSE 80
CMD ["apachectl", "-D", "FOREGROUND"]
