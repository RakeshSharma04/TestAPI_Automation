pipeline {
    agent any  // Use any available Jenkins agent (node) to run the pipeline

    environment {
        // Define the full path to Python executable (Windows-specific)
        // This makes Python accessible via the %PYTHON% variable in bat blocks
        PYTHON = 'C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Cloning repo..."  // Log message to the Jenkins console output
                checkout scm  // Checkout source code from the repository configured in Jenkins job
            }
        }

        stage('Set up Python Environment') {
            steps {
                echo "Setting up Python environment..."  // Log message
                bat '''
                    %PYTHON% -m pip install --upgrade pip  // Upgrade pip to the latest version
                    %PYTHON% -m pip install -r requirements.txt  // Install required Python packages from requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running tests with pytest..."  // Log message
                bat '''
                    %PYTHON% -m pytest tests/  // Execute all pytest tests inside the 'tests/' folder
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline completed."  // Always runs after the pipeline ends, regardless of result
        }
        success {
            echo "Build succeeded!"  // Runs only if the pipeline completes successfully
        }
        failure {
            echo "Build failed!"  // Runs only if the pipeline fails at any stage
        }
    }
}
