pipeline {
    agent any
  
    stages {
        stage('Setup') {
            steps {
                sh "bash jenkins/setup.sh"
            }
        }
    stages {
        stage('Build') {
            steps {
                sh "bash jenkins/build.sh"
            }
        }
        stage('Test') {
            steps {
                sh "bash jenkins/test.sh"
            }
        }
         stage('Push') {
            steps {
                sh "bash jenkins/push.sh"
            }
        }
        stage('Deploy') {
            steps {
                sh "bash jenkins/deploy.sh"
            }
        }
    }

