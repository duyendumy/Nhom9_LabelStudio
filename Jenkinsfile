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
                        withEnv(['PYTHONIOENCODING=utf-8']) {
                            bat 'python manage.py runserver 8080'
                        }
                    }
                }
            }
        }

        stage('Run Server and Selenium Tests') {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            parallel {
                stage('Run Tests') {
                    steps {
                        script {
                            dir('label_studio') {
                                sleep 30
                                withEnv(['PYTHONIOENCODING=utf-8']) {
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
