pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/DhwaniAjmera/DevOps_Assignment_2024TM93504.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'echo "Run your tests here"'
            }
        }

        stage('Build Docker Image') {
            when {
                environment name: 'USE_DOCKER', value: 'true'
            }
            steps {
                sh 'docker build -t devops-app .'
            }
        }

        stage('Run Docker Container') {
            when {
                environment name: 'USE_DOCKER', value: 'true'
            }
            steps {
                sh 'docker run -d -p 5000:5000 devops-app'
            }
        }
    }
}