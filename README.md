# s4hri-docker
Template for building S4HRI experiments using Docker

# Minimum requirements

1. Ubuntu (20.04 tested)
2. make

    sudo apt-get install make


# Quickstart (development)

1. Define your .env entries (root folder)
2. Fill your docker image in the file Dockerfile (root folder)
3. Create the Project DOCKER IMAGE using the command:

    cd .docker && make init

4. Build the LOCAL DOCKER IMAGE:

    cd .docker && make build

5. Define your additional services in the docker-compose.yml
6. Run the docker image:

    cd .docker && make run


7. Create a release on github to trigger the event for pushing the EXPERIMENT DOCKER IMAGE on dockerhub

# Quickstart (production)

1. Setup, build and run the LOCAL DOCKER IMAGE:

    cd .docker && make run


# Setup
Automatic setup has been designed for Ubuntu systems (hard check for /etc/os-release).

    cd .docker && make setup

Will perform a check for:
- docker (will install latest docker-ce)
- docker-compose (will install 1.29.2)
- nvidia-container-runtime (will install for correct ubuntu only if the nvidia kernel driver is loaded)
- will add current user to group docker if not added

Please notice that the setup runs automatically during the building/running process.
