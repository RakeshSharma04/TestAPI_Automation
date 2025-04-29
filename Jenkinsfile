pipeline {
    agent any  // Runs on any available agent (can also specify 'linux', 'windows', etc.)

    environment {
        // You can set global env variables here if needed
        PYTHON = 'python3'
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Cloning repo..."
                checkout scm
            }
        }

        stage('Set up Python Environment') {
            steps {
                echo "Setting up Python environment..."
                sh '''
                    ${PYTHON} -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running tests with pytest..."
                sh '''
                    pytest tests/
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline completed."
        }
        success {
            echo "Build succeeded!"
        }
        failure {
            echo "Build failed!"
        }
    }
}
