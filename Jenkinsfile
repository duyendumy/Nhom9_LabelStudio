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

        stage('Start Local Server') {
            steps {
               dir('label_studio'){
                    withEnv(['PYTHONIOENCODING=utf-8']) {
                    bat 'start /B python manage.py runserver 8080'
                    bat 'pytest -s -v test_selenium/test_signin.py'

                   
            }
               }
        }
        }


     

    }
}
