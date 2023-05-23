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
                        // Start the server and store its process ID
                        def serverProcess = sh(returnStdout: true, script: 'python manage.py runserver 8080 & echo $!')
                        // Store the process ID in an environment variable
                        env.SERVER_PROCESS_ID = serverProcess.trim()
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
                        sh 'pytest -s -v test_selenium/test_signin.py'
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
                    sh "kill -9 ${env.SERVER_PROCESS_ID}"
                }
            }
        }
    }
}
