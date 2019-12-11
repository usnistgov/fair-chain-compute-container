FROM fiji/fiji:fiji-openjdk-8

MAINTAINER National Institute of Standards and Technology

ARG DATA_DIR="/data"
USER root

# Create data folders
RUN mkdir -p ${DATA_DIR}/inputs \
    && mkdir ${DATA_DIR}/outputs