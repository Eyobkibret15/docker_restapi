pipeline {
    agent any

    stages {
  stage('Checkout external proj') {
        steps {
            git branch: 'my_specific_branch',
                credentialsId: 'my_cred_id',
                url: 'ssh://git@test.com/proj/test_proj.git'
            sh "ls"
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
