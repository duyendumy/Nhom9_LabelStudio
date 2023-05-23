pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                dir('deploy') {
                    bat 'pip install -r requirements.txt'
                }
            }
        }

        stage('Start Server') {
            steps {
                script {
                    dir('label_studio') {
                        withEnv(['PYTHONIOENCODING=utf-8']){
                        // Start the server and store its process ID
                        bat 'python manage.py runserver 8080'
                        // Store the process ID in an environment variable
                        env.SERVER_PROCESS_ID = serverProcess.trim()
                        }
                    }
                }
            }
        }

        stage('Run Tests') {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                script {
                    dir('label_studio') {
                        sleep 30
                        // Run pytest
                        bat 'pytest -s -v test_selenium/test_signin.py'
                    }
                }
            }
        }

        stage('Stop Server') {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                script {
                    // Stop the server using the stored process ID
                    bat "kill -9 ${env.SERVER_PROCESS_ID}"
                }
            }
        }
    }
}
