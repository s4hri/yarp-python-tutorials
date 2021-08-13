ARG DOCKER_SRC

FROM $DOCKER_SRC

# Install essential for python3
RUN pip3 install matplotlib numpy 