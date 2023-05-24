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
                    bat 'python manage.py runserver 8080'
            }
               }
        }
        }


     

    }
}
