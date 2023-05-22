# README

A simple WIPP Plugin for thresholding written in Python using scikit-image.
This folder contains:
- `src` folder containing the `threshold.py` code
- `Dockerfile`
- `plugin.json` manifest
- `sample-data` folder with test data

## Build the Docker image
```
docker build . -t wipp/wipp-simple-python-thresh:0.0.1
```

## Run the Docker image
From this directory:
```
docker run -v "$PWD"/sample-data:/data \
	wipp/wipp-simple-python-thresh:0.0.1 \
	--inputImages /data/inputs \
	--threshold 1000 \
	--output /data/outputs
```
`-v`: mounts a volume/folder from your machine inside of the Docker container
