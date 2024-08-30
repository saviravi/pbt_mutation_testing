#!/bin/bash

mkdir -p /home/myuser/app
chmod 777 /home/myuser/app

# Check if repository URL is provided
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <repository-url>"
  exit 1
fi

REPO_URL=$1

git clone "$REPO_URL" repo


