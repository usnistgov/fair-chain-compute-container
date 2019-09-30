#@IgnoreInspection BashAddShebang
FROM gcc

MAINTAINER National Institute of Standards and Technology

ARG DATA_DIR="/data"

# Create data folders
RUN mkdir -p ${DATA_DIR}/inputs \
    && mkdir ${DATA_DIR}/outputs

# Update libs and install cmake
RUN apt-get update -y \
    && apt-get install -y cmake

# Install HTGS
RUN cd /tmp \
    && git clone https://github.com/usnistgov/HTGS.git \
    && cd HTGS \
    && mkdir build && cd build \
    && cmake .. \
    && make \
    && make install \
    && rm -rf /tmp/HTGS

# Install Fast Image
RUN cd /tmp \
    && git clone https://github.com/usnistgov/FastImage.git \
    && cd FastImage \
    && mkdir build && cd build \
    && cmake .. \
    && make \
    && make install \
    && rm -rf /tmp/FastImage