pipeline {
    agent any
    stages {
   
        stage('Install Dependencies') {
            steps {
                dir('deploy'){
                     bat 'pip install -r requirements.txt'
                }
            }
        }
     
        stage('Run Development Server') {
            steps {
                parallel(
                    "RunServer": {
                        script {
                             dir('label_studio'){
                                 withEnv(['PYTHONIOENCODING=utf-8']){
                                    bat 'python manage.py runserver 8080'
                                 }
                             }
                        }
                    },
                    "RunTests": {
                        script {
                            dir('label_studio'){
                                withEnv(['PYTHONIOENCODING=utf-8']){
                                    bat 'pytest -s -v test_selenium/test_login.py'
                                }
                            }
                        }
                    }
                )
            }
        }
    }
}