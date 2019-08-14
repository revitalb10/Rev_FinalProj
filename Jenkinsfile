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
				subject: '$JOB_NAME - Build # $BUILD_NUMBER - ${currentBuild.currentResult}!',
                body: '$JOB_NAME - Build # $BUILD_NUMBER - ${currentBuild.currentResult}: Check console output at $BUILD_URL to view the results.'
			);
		}
	}
}