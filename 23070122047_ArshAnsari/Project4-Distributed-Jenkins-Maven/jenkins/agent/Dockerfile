FROM jenkins/ssh-agent:jdk17

USER root
RUN apt-get update \
    && apt-get install -y --no-install-recommends maven git \
    && rm -rf /var/lib/apt/lists/*
