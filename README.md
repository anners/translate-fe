# translate-fe
This is the frontend service for my quick kubernetes demo. This doesn't do much without the [backend service](https://github.com/anners/translate-be). This displays a drop down menu with multiple languages, lets the user select a language and sends the language choice to the backend service. It is assumed you can resolve the backend service via dns as translate-service. Using kubernetes this is handled by it's [dns service](https://github.com/kubernetes/dns/blob/master/docs/specification.md). You could easily add an entry in your /etc/hosts file for local testing.

You will also need to set-up a service account and download the private JSON key. More information setting up Google Translate AP can be found [here](https://cloud.google.com/translate/docs/quickstart?csw=1).

The backend code can be found [here](https://github.com/anners/translate-be).

## docker set-up
This can be ran locally as a docker container.
```
pip3 install -r requirements.txt
docker run -d -p 5001:5001 translate-fe
```
alternatively you can run: ```docker pull anners/translate-fe:latest```

## python set-up
This can also just be ran as a python/flask app.
```
pip3 install -r requirements.txt
python3 index.py
```

## kubernetes quick and dirty set-up
Set up cluster with GKE (or any other way you prefer)
```
gcloud container clusters create translate
```
Create a secret with your private key
```
kubectl create secret generic translate-key --from-file=key.json=<path-to-key>.json
```
Create the deployment and service
```
kubectl create -f deployment/translate-fe-app.yaml
kubectl create -f deployment/translate-fe-service.yaml
```
Your service should now be available. You can use various kubectl commands to see what is running.
```
kubectl [get|describe] deployments
kubectl [get|describe] pods
kubectl [get|describe] services
```

## skaffold
Skaffold is a ridiculously easy command line tool that facilitates continuous development for Kubernetes.
For information on installing skaffold check out it's [GitHub page](https://github.com/GoogleContainerTools/skaffold).

To use it for this project change the image name in skaffold.yaml and deployment/tanslate-fe-app.yaml to match your docker repo and simply run ```skaffold dev```
