pipeline {
    agent {label 'Revital-PC'}
    stages {
        stage('clone proj') {
            steps {
                git 'https://github.com/revitalb10/Rev_FinalProj.git'
            }
        }
       stage('Docker compose') {
            steps {
               bat 'docker-compose up -d'
            }
        }   
       stage('Run Selenium test') {
            steps {
               bat 'python FinalProj.py'
            }
        }      
    }
}
