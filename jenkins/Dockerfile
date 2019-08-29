FROM jenkins/jenkins:lts
USER root
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y python3 python3-venv virtualenv python3-virtualenv

COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt

COPY jenkins.yaml /usr/share/jenkins/ref/jenkins.yaml
ENV CASC_JENKINS_CONFIG=/usr/share/jenkins/ref/jenkins.yaml

USER jenkins
