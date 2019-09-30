FROM wipp/wipp-plugins-base:imagej-fiji

# Update maintainer
MAINTAINER Plugin Maintainer

ARG EXEC_DIR="/opt/executable"

# Create exec folder
RUN mkdir -p ${EXEC_DIR}

#Copy executable (ImageJ compatible script, see https://imagej.net/Scripting) - example
COPY macro.ijm ${EXEC_DIR}/

WORKDIR /opt/fiji

# Default command. Additional arguments are provided through the command line
ENTRYPOINT ["entrypoint.sh", "--headless", "--ij2", "--console", "--run", "${EXEC_DIR}/macro.ijm"]