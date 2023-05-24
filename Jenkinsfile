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
                    sleep(time: 10, unit: 'SECONDS')
                    bat 'taskkill /F /PID $(netstat -ano | findstr :8080 | awk "{print $5}")'
            }
               }
        }
        }


     

    }
}
