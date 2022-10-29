pipeline {
    agent any
    stages {
        stage('Clone'){
            steps{
                sh "git clone https://github.com/AmbreenShabbir/QA-Project-Movies.git" 
            }
        }
    stage('Build'){
            steps{
                sh "python3 app.py" 
            }
        }
    stage('Test'){
            steps{
                sh "python3 -m pytest --cov" 
            }
        }
    stage('Deploy'){
            steps{
                sh "python3 -m pytest --cov" 
            }
        }
    }
}

