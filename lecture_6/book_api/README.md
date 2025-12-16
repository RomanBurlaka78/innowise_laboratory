## Run docker
docker build --no-cache -t app:latest .
docker run -p 8081:8081 app:latest
open in browser http://localhost:8081/docs 