FROM tensorflow/tensorflow:2.0.0rc0-gpu-py3
MAINTAINER National Institue of Standards and Technology

ENV DEBIAN_FRONTEND noninteractive

ARG EXEC_DIR="/opt/executables"
ARG DATA_DIR="/data"

#Create folders
RUN mkdir -p ${EXEC_DIR} \
    && mkdir -p ${DATA_DIR}/images \
    && mkdir -p ${DATA_DIR}/masks \
    && mkdir -p ${DATA_DIR}/outputs

# Install additional libraries
RUN apt -y install graphviz
RUN pip3 install lmdb scikit-image