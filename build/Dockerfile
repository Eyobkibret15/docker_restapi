FROM jenkins/jenkins:lts-alpine

USER root
RUN apk add docker
RUN apk add docker-compose
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers
