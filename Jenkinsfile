
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'docker build -t mypython .'
            }
        }

        stage('Run') {
            steps {
                bat 'docker rm -f mycontainer || exit 0'
                bat 'docker run --name mycontainer mypython'
            }
        }
    }

    post {
        success {
            echo "Registration Successful"
        }
        failure {
            echo "Registration Failure"
        }
    }
}


