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

                // Upgrade pip to the latest version
                // Install required Python packages from requirements.txt
                bat '''
                    %PYTHON% -m pip install --upgrade pip
                    %PYTHON% -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running tests with pytest..."  // Log message

                  // Execute all pytest tests inside the 'tests/' folder
                bat '''
                    %PYTHON% -m pytest --junitxml=test-results.xml tests/
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
