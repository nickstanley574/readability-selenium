FROM jenkins/jenkins:lts
USER root
RUN apt-get -y update && apt-get -y upgrade

COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
COPY jenkins.yaml /usr/share/jenkins/ref/jenkins.yaml
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt
ENV CASC_JENKINS_CONFIG=/usr/share/jenkins/ref/jenkins.yaml

USER jenkins
