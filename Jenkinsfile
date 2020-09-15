pipeline {
    
    environment {
        registry = "benspelledabc/jenkins-upload-test"
        registryCredential = 'dockerhub'
    }
    
    agent { dockerfile true }
    
    stages {
        stage('Say Hello World') {
            steps {
                echo 'hello world'
            }
        }//end say hello world stage
        
        
        stage('Building image') {
            steps{
                script {
                    //docker.build registry + ":$BUILD_NUMBER"
                    docker.build registry + ":latest"
                }
            }
        }//end build image stage
        
        
        stage('Deploy Image') {
            steps{
                script {
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }//end deploy image
        
        /*
        stage('Remove Unused docker image') {
            steps{
                sh "docker rmi $registry:$BUILD_NUMBER"
            }
        }*/
        //end remove image
        
    }//end of all stages
    
}
