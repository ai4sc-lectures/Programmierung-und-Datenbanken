#!/bin/bash

# Configuration
BRANCH="gh-pages"
HASH_FILE="/home/ploennigs/code/Programmierung-und-Datenbanken/commit_hash.txt"
POD_NAME="book-ml2"
NAMESPACE="books"

# Ensure the hash file exists
touch "$HASH_FILE"

# Get the latest commit hash from the remote branch
REMOTE_HASH=$(git rev-parse "origin/$BRANCH")

SAVED_HASH=$(cat "$HASH_FILE")

# Compare hashes and update if necessary
if [ "$REMOTE_HASH" != "$SAVED_HASH" ]; then
    echo "Updates found on branch $BRANCH. Restarting Pod."

    # Save the new commit hash
    echo "$REMOTE_HASH" > "$HASH_FILE"

    # Restart the Minikube pod
    #kubectl delete pod "$POD_NAME" -n "$NAMESPACE"
    microk8s kubectl scale deployment "$POD_NAME" -n "$NAMESPACE" --replicas=0
    sleep 5
    microk8s kubectl scale deployment "$POD_NAME" -n "$NAMESPACE" --replicas=1
else
    echo "No updates found on branch $BRANCH."
fi
