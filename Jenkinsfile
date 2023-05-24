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
                    def serverProcess = bat(script: 'python manage.py runserver 8080', returnStdout: true, background: true)
                    sleep(time: 10, unit: 'SECONDS')
                    bat(script: "kill ${serverProcess}")
            }
               }
        }
        }


     

    }
}
