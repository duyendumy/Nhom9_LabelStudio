pipeline {
    agent any
    stages {

        stage('Build image') {
            steps {
                withDockerRegistry(credentialsId: 'docker-hub', url: 'https://index.docker.io/v1/') {
                    bat 'docker build -t duyendu/group09_label_studio:latest .'
                    bat 'docker push duyendu/group09_label_studio:latest'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                dir('deploy') {
                    bat 'pip install -r requirements.txt'
                }
            }
        }

        stage('Test Selenium') {
            steps {
               dir('label_studio'){
                    withEnv(['PYTHONIOENCODING=utf-8']) {
                    bat 'start /B python manage.py runserver 8080'
                    sleep 50
                    bat 'pytest -s -v test_selenium/test_signin.py'

                   
            }
               }
        }
        }


     

    }
}
