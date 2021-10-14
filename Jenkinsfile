pipeline {
    agent none
    stages {
        stage('build') {
            agent {
                docker {
                    image ''

                }
            }
            steps {
                sh 'pip install -r requirements.txt'

            }
        }
    }
}

