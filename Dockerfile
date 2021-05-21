FROM ubuntu:18.04
MAINTAINER sstuddard@oculus360.us

# Uncomment the following to make it work
#ARG DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && \
 apt-get -y install default-jre && \
 apt-get -y install awscli && \
 apt-get -y install jq && \
 apt-get -y install time
