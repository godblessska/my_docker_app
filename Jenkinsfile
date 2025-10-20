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
                git branch: 'main', url: 'https://github.com/godblessska/my_docker_app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
            }
        }

        stage('Test Docker Image') {
            steps {
                echo "Running container to test..."
                sh 'docker run -d -p 5000:5000 --name calc-test $IMAGE_NAME:$IMAGE_TAG'
                sh 'sleep 5'
                sh 'curl -f http://localhost:5000/health'
            }
            post {
                always {
                    sh 'docker stop calc-test || true'
                    sh 'docker rm calc-test || true'
                }
            }
        }

        stage('Push to Docker Hub') {
            when {
                expression { return env.DOCKER_HUB_USER != null }
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin'
                    sh 'docker push $IMAGE_NAME:$IMAGE_TAG'
                }
            }
        }
    }

    post {
        success {
            echo "✅ Build successful! Docker image: $IMAGE_NAME:$IMAGE_TAG"
        }
        failure {
            echo "❌ Build failed!"
        }
    }
}
