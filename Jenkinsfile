pipeline {
    agent any
    stages {
        stage('Install Dependencies From Dev Branch') {
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
                    sleep 100
                    bat 'pytest -s -v test_selenium/test_signin.py'        
                }
               }
            }
        } 
        stage('reports') {
            steps {
            script {
                    allure([
                            includeProperties: false,
                            jdk: '',
                            properties: [],
                            reportBuildPolicy: 'ALWAYS',
                            results: [[path: 'label_studio/allure_reports']]
                    ])
            }
            }
        } 

    }
}