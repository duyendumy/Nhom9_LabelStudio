pipeline {
    agent {
        docker {
            image 'maven:3.8.4'  // Use a Docker image as the Jenkins agent
            args '-v /var/run/docker.sock:/var/run/docker.sock'  // Mount Docker socket
        }
    }

    environment {
    DOCKERHUB_CREDENTIALS = credentials('duyendu-dockerhub')
     }
    stages {

        stage('Build image') {
            steps {         
                    bat 'docker build -t duyendu/group09_label_studio:latest .'
                    bat 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                    bat 'docker push duyendu/group09_label_studio:latest'
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
