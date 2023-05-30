# Commands to run the 

### Build Docker image
docker build -t anuragbatra706/scalable_api:latest .

### Push Docker image to DockerHub
docker push anuragbatra706/scalable_api:latest

### Apply Kubernetes configuration
kubectl apply -f flask-deployment.yaml
