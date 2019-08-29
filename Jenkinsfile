pipeline {
    agent any

    options { timestamps() }

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
}