FROM wipp/wipp-plugins-base:python3-tesnorflow-skimage
MAINTAINER National Institue of Standards and Technology

# Update maintainer
MAINTAINER Plugin Maintainer

ARG EXEC_DIR="/opt/executable"

# Create exec folder
RUN mkdir -p ${EXEC_DIR}

#Copy executable - example
COPY src ${EXEC_DIR}/

WORKDIR ${EXEC_DIR}

# Default command. Additional arguments are provided through the command line
ENTRYPOINT ["python3", "my-program.py"]