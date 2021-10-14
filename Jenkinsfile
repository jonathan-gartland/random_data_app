pipeline {
    agent { docker { image 'python:3.8.0' } }
    stages {
        stage('build') {
            steps {
                sh 'pip install -r requirements.txtq
            }
        }
        stage('test') {
            steps {
                sh 'python test.py'
            }
        }
    }
}
