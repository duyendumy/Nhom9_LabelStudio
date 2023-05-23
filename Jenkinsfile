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
     
        stage('Run Server and Selenium Tests') {
            parallel {
                stage('Start Server'){
                    steps {
                        script {
                            try{
                                    dir('label_studio'){
                                        withEnv(['PYTHONIOENCODING=utf-8']){
                                        bat 'python manage.py runserver 8080'
                                        sleep 20
                                        bat 'pytest -s -v test_selenium/test_signin.py'
                                        }
                                    }
                        } catch(Exception e){
                              echo "Selenium tests failed: ${e.getMessage()}"
                              throw e // Rethrow the exception to mark the build as a failure

                        } finally{
                             dir('label_studio'){
                                        bat 'pkill -f "python manage.py runserver 8080"'
                                    }
                        }
                        }
                    }
                }
        }
        }  
    }
}

