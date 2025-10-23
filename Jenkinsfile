pipeline {
    agent any

    environment {
        IMAGE_NAME = "godblessska/my_docker_app"
        IMAGE_TAG = "latest"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Cloning repository..."
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                bat "docker build -t %IMAGE_NAME%:%IMAGE_TAG% ."
            }
        }

        stage('Test Docker Image') {
            steps {
                echo "Running container to test..."
                script {
                    bat "docker run -d -p 5000:5000 --name calc-test %IMAGE_NAME%:%IMAGE_TAG%"
                    bat "timeout /t 5 /nobreak"  
                }
            }
            post {
                always {
                    bat "docker stop calc-test || echo \"Container already stopped\""
                    bat "docker rm calc-test || echo \"Container already removed\""
                }
            }
        }

        stage('Push to Docker Hub') {
            when {
                expression { return env.DOCKER_HUB_CREDS != null }
            }
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        bat "echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin"
                        bat "docker push %IMAGE_NAME%:%IMAGE_TAG%"
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up workspace..."
            cleanWs()
            bat "docker system prune -f || echo \"Docker cleanup failed\""
        }
        success {
            echo "✅ Build successful! Docker image: %IMAGE_NAME%:%IMAGE_TAG%"
        }
        failure {
            echo "❌ Build failed!"
        }
    }
}
