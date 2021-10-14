pipeline {
    agent { docker {
    image 'python:3.8.0'
    args '-u root:root'
    } }
    stages {
        stage('build') {
            steps {
                sh 'pip install -r requirements.txt --user'
            }
        }
        stage('test') {
            steps {
                sh 'python test.py'
            }
        }
    }
}
