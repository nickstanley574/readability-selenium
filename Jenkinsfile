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
                echo 'Testing..'

            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
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