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
                script {
                        dir('label_studio'){
                            withEnv(['PYTHONIOENCODING=utf-8']){
                            bat 'JENKINS_NODE_COOKIE=dontKillMe  python manage.py runserver 8080'
                            }
                        }
                        }
            }
        }
        stage('Run Tests') {
            steps {
                  script {
                            dir('label_studio'){
                                withEnv(['PYTHONIOENCODING=utf-8']){
                                bat 'pytest -s -v test_selenium/test_signin.py'
                                }
                            }
                        }
            }
        }
        
    }
}