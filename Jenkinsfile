// library identifier: 'jenkins-shared@master', retriever: modernSCM(
//  [$class: 'GitSCMSource',
//   remote: 'git@github.com:Eyobkibret15/docker_restapi.git',
//  ])
//
// pipeline {
// agent {
//     docker { image 'python:3.9' }
// }
// stages {
//     stage('Build') {
//         steps {
//             sh 'docker-compose up --build'
//         }
//     }
//
//     stage('Test') {
//         steps {
//             sh 'pytest'
//         }
//     }
//
//     stage('Deploy') {
//         steps {
//             sh 'echo not yet...'
//         }
//     }
// }
// }

// pipeline {
//     agent any
//
//     stages {
//
//         stage('Build') {
//
//
//                    steps {
//
//                 sh 'python --version'
//                 echo 'Building..'
//             }
//         }
//         stage('Test') {
//             steps {
//                 sh 'docker --version'
//                 echo 'Testing..'
//             }
//         }
//         stage('Deploy') {
//             steps {
//                 echo 'Deploying....'
//             }
//         }
//     }
// }


pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                bat 'docker-compose build'
            }
        }
        stage('test') {
            steps {
                bat 'docker-compose up'
            }
        }


        stage('deploy') {
            steps {
                echo 'Hello World'
            }
        }
    }
}