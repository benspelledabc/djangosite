pipeline {
  environment {
    imagename = "benspelledabc/djangosite"
    registryCredential = 'dockerhub'
    dockerImage = ''
    certPath = '~/.ssh/AWSBob.private'
    sshUser = 'root'
    sshTarget = '104.248.122.83'
  }
  
  options {
    buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
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
    
    //def remote = [:]
    //remote.name = ""
    //remote.host = "benspelledabc.me"
    //remote.host = "104.248.122.83"
    //remote.allowAnyHosts = true
    stage("SSH Steps Rocks!") {
      steps {
        sh 'whoami'
        sh 'echo $HOME'
        //sh 'ssh -i ~.ssh/AWSBob.private benspelledabc.me "touch /data/django/fromJenkins"'
        sh 'ssh -i $certPath -oStrictHostKeyChecking=no $sshUser@$sshTarget "touch /data/django/fromJenkins2"'
        //writeFile file: 'test.sh', text: 'ls'
        //sshCommand remote: "104.248.122.83", command: 'for i in {1..5}; do echo -n \"Loop \$i \"; date ; sleep 1; done'
        //sshScript remote: remote, script: 'test.sh'
        //sshPut remote: remote, from: 'test.sh', into: '.'
        //sshGet remote: remote, from: 'test.sh', into: 'test_new.sh', override: true
        //sshRemove remote: remote, path: 'test.sh'
      }
    }
    
    
    
  }
}
