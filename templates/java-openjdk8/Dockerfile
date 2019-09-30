FROM wipp/wipp-plugins-base:java-openjdk8

# Update maintainer
MAINTAINER Plugin Maintainer

ARG EXEC_DIR="/opt/executable"

# Create exec folder
RUN mkdir -p ${EXEC_DIR}

# Copy JAR - example
COPY target/my-program*.jar ${EXEC_DIR}/my-program.jar

# Set working directory
WORKDIR ${EXEC_DIR}

# Default command. Additional arguments are provided through the command line
ENTRYPOINT ["/usr/bin/java", "-jar", "my-program.jar"]