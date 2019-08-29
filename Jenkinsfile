pipeline {
    agent any

    options { timestamps() }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh './setup.sh'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                sh 'pwd;ls; ls -al  venv/'
                sh '#!/bin/bash source venv/bin/activate'
                sh 'which python'
                sh 'python -m unittest discover'
            }
        }
    }
}