pipeline {
    agent any

    options { timestamps() }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh ./setup.sh

                }
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
}