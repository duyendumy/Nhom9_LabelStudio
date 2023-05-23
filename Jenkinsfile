def checkServerStatus() {
    try {
        sh 'curl -s http://localhost:8080'
        return true
    } catch (Exception e) {
        return false
    }
}
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

        stage('Run Server and Selenium Tests') {
            parallel {
                stage('Start Server') {
                    steps {
                        script {
                            dir('label_studio') {
                                withEnv(['PYTHONIOENCODING=utf-8']) {
                                    // Start the server in the background
                                    bat 'start /B python manage.py runserver 8080'
                                }
                            }
                        }
                    }
                }

                stage('Wait for Server') {
                    steps {
                        script {
                            dir('label_studio') {
                                withEnv(['PYTHONIOENCODING=utf-8']) {
                                    // Wait for the server to start
                                   timeout(time: 20, unit: 'MINUTES') {
                                        waitUntil {
                                            return checkServerStatus()
                                        }
                                    }
                                }
                            }
                        }
                    }
                }

                stage('Run Tests') {
                    steps {
                        script {
                            dir('label_studio') {
                                withEnv(['PYTHONIOENCODING=utf-8']) {
                                    // Run Selenium tests
                                    bat 'pytest -s -v test_selenium/test_signin.py'
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
