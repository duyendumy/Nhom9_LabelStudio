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
                                    script {
                                        def retryInterval = 15
                                        def maxRetries = 2
                                        def retries = 0
                                        boolean serverStarted = false

                                        while (!serverStarted && retries < maxRetries) {
                                            sleep retryInterval
                                            serverStarted = checkServerStatus()
                                            retries++
                                        }

                                        if (!serverStarted) {
                                            error('Failed to start the server')
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
                                    sleep 30
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
