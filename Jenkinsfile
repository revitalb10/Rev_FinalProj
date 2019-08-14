pipeline {
    agent any
    stages {
        stage('clone proj') {
            steps {
               git url 'https://github.com/revitalb10/Rev_FinalProj.git'
            }
        }
       stage('Docker compose') {
            steps {
               bat 'docker compose up -d'
            }
        }   
       stage('Run Selenium test') {
            steps {
               bat 'python FinalProj.py'
            }
        }      
   
    }
}
