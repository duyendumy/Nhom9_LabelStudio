pipeline {
    agent any
    stages {
        stage('Run Development Server') {
            steps {
                parallel(
                    "RunServer": {
                        script {
                             dir('label_studio'){
                                 sh 'python manage.py runserver 8080'
                             }
                        }
                    },
                    "RunTests": {
                        script {
                            dir('label_studio'){
                                sh 'pytest -s -v test_selenium/test_login.py '
                            }
                        }
                    }
                )
            }
        }
    }
}