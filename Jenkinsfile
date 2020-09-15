pipeline {
  environment {
    imagename = "benspelledabc/jenkins-upload-test"
    registryCredential = 'dockerhub'
    dockerImage = ''
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git([url: 'https://github.com/benspelledabc/djangosite.git', branch: 'auto_push', credentialsId: 'ben-github-global'])

      }
    }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build imagename
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push("$BUILD_NUMBER")
             dockerImage.push('latest')

          }
        }
      }
    }
    stage('Remove Unused docker image') {
      steps{
        sh "docker rmi $imagename:$BUILD_NUMBER"
         sh "docker rmi $imagename:latest"

      }
    }
  }
}

//old kinda works, build but  no push
/*
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
    }
}
*/
