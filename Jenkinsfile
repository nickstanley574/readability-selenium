pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    stages {
        stage('Build') {
            steps {
                sh './setup.sh'
            }
        }
        stage('UnitTests') {
            steps {
                sh '''#!/bin/bash
                    source venv/bin/activate
                    which python
                    python -m unittest discover
                '''
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