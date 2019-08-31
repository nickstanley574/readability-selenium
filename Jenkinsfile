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
                sh 'sleep 30' //builds are going to fast to test jenkins cocurrent build check this will be removed
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