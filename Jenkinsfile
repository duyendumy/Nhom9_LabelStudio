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
                                bat 'python manage.py runserver 8080'
                                }
                            }
                        }
            }
        }
        stage('RunTests') {
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
        stage('Stop Django Server') {
            steps {
                // Find and kill the Django server process running on port 8080
                bat 'for /f "tokens=5" %a in (\'netstat -aon ^| findstr ":8080" ^| findstr "LISTENING"\') do taskkill /F /PID %a'
            }
        }
        
    }
}