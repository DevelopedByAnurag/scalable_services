# Commands to run the 

### Build Docker image
docker build -t anuragbatra706/scalable_api:latest .

### Push Docker image to DockerHub
docker push anuragbatra706/scalable_api:latest

### Apply Kubernetes configuration
kubectl apply -f flask-deployment.yaml


##### This Flask application now has the following API endpoints:

- /greet: Greets the specified user.
- /save_name: Saves the name sent using a POST request to the MongoDB Atlas collection.
- /fetch_names: Fetches the list of names from the MongoDB Atlas collection.
