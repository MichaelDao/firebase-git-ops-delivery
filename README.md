# firebase-git-ops-delivery
Proof of concept based on https://cloud.google.com/kubernetes-engine/docs/tutorials/gitops-cloud-build

Currently looking to deploy sample firestore data to my very own GCP project with a Continous delivery approach.

## What I needed:
- Mirror this repo in cloud source repositories
- Cloud build API
- Cloud build trigger to point to cloudbuild.yaml and cloudbuild-delivery.yaml
