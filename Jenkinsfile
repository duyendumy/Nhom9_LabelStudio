pipeline {
    agent any
    stages {
        stage('Run Development Server') {
            steps {
                parallel(
                    "RunServer": {
                        script {
                            sh 'cd label-studio'
                            sh 'python manage.py runserver'
                        }
                    },
                    "RunTests": {
                        script {
                            sh 'cd label-studio'
                            sh 'pytest -s -v test_selenium/test_login.py '
                        }
                    }
                )
            }
        }
    }
}