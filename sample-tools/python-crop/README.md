# README

A simple WIPP Plugin for image crop operation written in Python using pillow library.
This folder contains:
- `src` folder containing the `crop_image.py` code
- `Dockerfile`
- `plugin.json` manifest
- `sample-data` folder with test data

## Build the Docker image
```
docker build . -t wipp/wipp-simple-python-crop:0.0.1
```

## Run the Docker image
From this directory:
```
docker run -v "$PWD"/sample-data:/data \
	wipp/wipp-simple-python-crop:0.0.1 \
	--image_dir /data/inputs \
	--xDim 256 --yDim 256  \
	--output_dir /data/outputs
```
`-v`: mounts a volume/folder from your machine inside of the Docker container
