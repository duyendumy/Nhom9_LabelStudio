pipeline {
    agent {label 'linux'}

    environment {
    DOCKERHUB_CREDENTIALS = credentials('duyendu-dockerhub')
     }
    stages {

        stage('Build image') {
            steps {         
                    sh 'docker build -t duyendu/group09_label_studio:latest .'
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                    sh 'docker push duyendu/group09_label_studio:latest'
            }
        }

        stage('Install Dependencies') {
            steps {
                dir('deploy') {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Test Selenium') {
            steps {
               dir('label_studio'){
                    withEnv(['PYTHONIOENCODING=utf-8']) {
                    sh 'start /B python manage.py runserver 8080'
                    sleep 50
                    sh 'pytest -s -v test_selenium/test_signin.py'

                   
            }
               }
        }
        }


     

    }
}
