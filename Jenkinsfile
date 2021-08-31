      pipeline {
        agent {
            docker { image 'python:3.9' }
        }
        stages {
            stage('Build') {
                steps {
                    sh 'docker-compose up --build'
                }
            }

            stage('Test') {
                steps {
                    sh 'pytest'
                }
            }

            stage('Deploy') {
                steps {
                    sh 'echo not yet...'
                }
            }
        }
    }