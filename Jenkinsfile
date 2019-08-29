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
                sh '#!/bin/bash source venv/bin/activate'
                sh 'which python'
                sh 'python -m unittest discover'
            }
        }
    }
    post {
        always {
            // Recursively delete the current directory from the workspace
            deleteDir()
        }
    }
}