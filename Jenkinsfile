pipeline {
    agent any

    stages {
  stage('Checkout external proj') {
        steps {
            git branch: 'master',
                credentialsId: 'api',
                url: 'git@github.com:Eyobkibret15/docker_restapi.git'
            bat "dir"
        }
    }
        stage('build') {
            steps {
                echo 'Hello World'
            }
        }
        stage('test') {
            steps {
                echo 'Hello World'
            }
        }
    }
}
