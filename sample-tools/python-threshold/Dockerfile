FROM python:3
MAINTAINER National Institute of Standards and Technology

# Define exec and data folders
ARG EXEC_DIR="/opt/executables"
ARG DATA_DIR="/data"

# Create folders
RUN mkdir -p ${EXEC_DIR} \
    && mkdir -p ${DATA_DIR}/inputs \
    && mkdir -p ${DATA_DIR}/outputs

# Install python libraries
RUN pip install numpy scikit-image imagecodecs

# Copy Python script
COPY src ${EXEC_DIR}/

# Default command. Additional arguments are provided through the command line
ENTRYPOINT ["python", "/opt/executables/threshold.py"]
