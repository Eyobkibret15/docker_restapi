pipeline {
    agent any
    environment {
        DEBUG = "1"
}
    stages {
        stage('build') {
            steps {
                echo 'Hello World'
                sh   'python key.py'
            }
        }
        stage('test') {
            steps {
                echo 'Hello World'
            }
        }
    }
}
