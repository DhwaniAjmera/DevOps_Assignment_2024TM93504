pipeline {
    agent any

    stages {

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

        stage('Code Quality - Flake8') {
            steps {
                bat 'flake8 .'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                echo "SonarQube integration placeholder"
            }
        }

        stage('Build (Skipped Docker)') {
            steps {
                echo "Docker build skipped (office restriction)"
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