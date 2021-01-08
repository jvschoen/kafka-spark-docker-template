#!/bin/bash

# This script is used to create the docker images with unique 
# container name with github repo name appended.


# Get the name of the repo
repo_name=$(basename -s .git `git config --get remote.origin.url`)

# Making the service name in the docker-compose match the github repo name
echo "Editing Dockerfile with repo name ($repo_name) as service name"
sed "s/INSERT_REPO_NAME/${repo_name}/g" docker-compose.yml.tmpl > docker-compose.yml
#rm docker-compose.yml.tmpl

docker-compose up