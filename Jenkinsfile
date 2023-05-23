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

        stage('Start Server'){
            steps {
                script {
                            dir('label_studio'){
                                withEnv(['PYTHONIOENCODING=utf-8']){
                                bat 'python manage.py runserver 8080'
                                }
                            }
                             waitForServer()
                        }
            }
        }


    }

    post {
        always {
            steps {
                script {
                            dir('label_studio'){
                                withEnv(['PYTHONIOENCODING=utf-8']){
                                bat 'pkill -f "python manage.py runserver"'
                                }
                            }
                             waitForServer()
                        }
            }
        }
    }
}

def waitForServer() {
    timeout(time: 5, unit: 'MINUTES') {
        def serverReady = false
        def maxRetries = 30
        def retryCount = 0

        while (!serverReady && retryCount < maxRetries) {
            def response = sh(returnStdout: true, script: 'curl -s -o /dev/null -w "%{http_code}" http://localhost:8080/')
            if (response.trim() == '200') {
                serverReady = true
            } else {
                retryCount++
                sleep 10
            }
        }

        if (!serverReady) {
            error('Server did not start within the specified time')
        }
    }
}
