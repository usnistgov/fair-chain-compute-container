FROM wipp/wipp-plugins-base:gcc-htgs-fastimage

# Update maintainer
MAINTAINER Plugin Maintainer

ARG EXEC_DIR="/opt/executable"

# Create exec folder
RUN mkdir -p ${EXEC_DIR}

# Build executable - example
COPY my-program ${EXEC_DIR}/
RUN cd ${EXEC_DIR}/my-program \
    && mkdir build && cd build \
    && cmake .. \
    && make main \
    
WORKDIR ${EXEC_DIR}

# Default command. Additional arguments are provided through the command line
ENTRYPOINT ["my-program/build/main"]
