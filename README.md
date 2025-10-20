Чтобы запустить приложение в терминале git bush:
-git clone https://github.com/godblessska/my_docker_app.git
-cd my_docker_app
-docker build -t my_docker_app .
-docker run -d -p 5000:5000 my_docker_app