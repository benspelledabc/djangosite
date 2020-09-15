pipeline {
  environment {
    imagename = "benspelledabc/djangosite"
    registryCredential = 'dockerhub'
    dockerImage = ''
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git([url: 'https://github.com/benspelledabc/djangosite.git', branch: 'develop', credentialsId: 'ben-github-global'])
        //git([url: 'https://github.com/benspelledabc/djangosite.git', branch: 'master', credentialsId: 'ben-github-global'])
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
            //on develop branch, we are only going to push to latest
            //master will push to some other special sauce
            dockerImage.push("0.$BUILD_NUMBER")
            dockerImage.push('latest')
          }
        }
      }
    }
    stage('Remove Unused docker image') {
      steps{
        //we may not have pushed them all, but we're going to clean them all up
        sh "docker rmi $imagename:0.$BUILD_NUMBER"
        sh "docker rmi $imagename:latest"
      }
    }
    
    stage("SSH Steps Rocks!") {
        writeFile file: 'test.sh', text: 'ls'
        sshCommand remote: remote, command: 'for i in {1..5}; do echo -n \"Loop \$i \"; date ; sleep 1; done'
        sshScript remote: remote, script: 'test.sh'
        sshPut remote: remote, from: 'test.sh', into: '.'
        sshGet remote: remote, from: 'test.sh', into: 'test_new.sh', override: true
        sshRemove remote: remote, path: 'test.sh'
    }
    
    
  }
}
