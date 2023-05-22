# parent image
FROM python:3
LABEL maintainer="National Institute of Standards and Technology"

#copy file from host to current working directory
#COPY VERSION /

# Our environment, do not modified
ENV DEBIAN_FRONTEND noninteractive
ARG EXEC_DIR="/opt/executables"
ARG DATA_DIR="/data"
 
#Create folders (like every other plugin), do not modified
RUN mkdir -p ${EXEC_DIR}
RUN mkdir -p ${DATA_DIR}/inputs \
    && mkdir ${DATA_DIR}/outputs

#Run pip install for image crop operation
RUN pip3 install pillow numpy 

# Image Crop
# Copy Python script
COPY src ${EXEC_DIR}/

# Default command. Additional arguments are provided through the command line
ENTRYPOINT ["python3", "/opt/executables/crop_image.py"]

