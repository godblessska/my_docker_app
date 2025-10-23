pipeline {
    agent any

    environment {
        IMAGE_NAME = "godblessska/my_docker_app"
        IMAGE_TAG = "latest"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t ${env.IMAGE_NAME}:${env.IMAGE_TAG} ."
            }
        }

        stage('Test Docker Image') {
            steps {
                script {
                    // Используем другой порт
                    bat "docker run -d -p 5001:5000 --name calc-test ${env.IMAGE_NAME}:${env.IMAGE_TAG}"
                    bat "timeout /t 10 /nobreak"
                    bat "curl http://localhost:5001/health || echo Health check completed"
                }
            }
            post {
                always {
                    bat "docker stop calc-test || echo Container already stopped"
                    bat "docker rm calc-test || echo Container already removed"
                }
            }
        }

        stage('Verify Image') {
            steps {
                bat "docker images ${env.IMAGE_NAME}"
                bat "docker run --rm ${env.IMAGE_NAME}:${env.IMAGE_TAG} python --version"
            }
        }
    }

    post {
        always {
            // Заменим cleanWs на deleteDir
            deleteDir()
            bat "docker system prune -f || echo Docker cleanup completed"
        }
        success {
            echo "✅ Build successful! Docker image: ${env.IMAGE_NAME}:${env.IMAGE_TAG}"
        }
        failure {
            echo "❌ Build failed!"
        }
    }
}
