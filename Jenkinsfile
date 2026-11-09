pipeline{
    agent any{
        stages{
            stage('Build'){
                steps{
                    bat 'docker build -t mypython' 
                }
            }
            stage('Run'){
                steps{
                    bat 'docker rm mycontainer:5000|| exit 0'
                    bat 'docker run mypython'
                }
            }
            POST{
                success{
                    echo"Registration Successful"
                }
                failure{
                    echo"Registration Failure"
                }
            }
        }
    }
}