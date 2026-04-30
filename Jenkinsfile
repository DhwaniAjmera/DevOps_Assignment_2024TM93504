pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                bat 'sonar-scanner'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t aceest-fitness:latest .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                bat 'docker tag aceest-fitness DhwaniAjmera/aceest-fitness'
                bat 'docker push DhwaniAjmera/aceest-fitness'
            }
        }
    }

    post {
        success {
            echo 'Build Successful ✅'
        }
        failure {
            echo 'Build Failed ❌'
        }
    }
}