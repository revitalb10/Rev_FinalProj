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
	post {
		failure {
			mail (
				to: 'revitalb10@gmail.com',
				from: 'Jenkins',
				subject:'FAILED !! Jenkins Build: $JOB_NAME Build Number: $BUILD_NUMBER',
				body: "<b>The below build FAILED on Jenkins: </b><br>Project: $JOB_NAME <br>Build Number: $BUILD_NUMBER ",
				charset: 'UTF-8',
				mimeType: 'text/html'
			);
		}
	}
}