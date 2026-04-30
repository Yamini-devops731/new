pipeline {
    agent any

    environment {
        OPENAI_API_KEY = credentials('openai-key')
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-ai-app ./app'
            }
        }

        stage('Intentional Failure') {
            steps {
                sh 'echo "Simulating failure..."'
                sh 'exit 1'  // force failure
            }
        }
    }

    post {
        failure {
            echo "Pipeline failed. Running AI log analysis..."

            sh '''
            echo "Sample error: Docker build failed due to missing dependency" > log.txt
            python3 analyze_logs.py > ai_output.txt
            cat ai_output.txt
            '''
        }
    }
}
