===============
nba_predictions
===============


nba_predictions is package that allows one to quickly scrape nba data and 
model points scored for a given player.


Installation
============

## Docker (recommended)
Make sure Docker is installed on your host machine. If not please visit this link to get 
docker installed https://docs.docker.com/get-docker/. 

Assuming you have Docker run the following steps to create our image and run a container:

.. code:: shell

    git clone https://github.com/brettharder/nba_predictions.git
    cd nba_predictions/docker
    sh build_image.sh
    sh run_container.sh

Note: After this initial setup you can exit and respin a new container anytime by using `sh run_container.sh`.
Once in the container the package will be installed and ready to use! 

## Via Virtualenv
To install into a virtualenv do the following steps in a directory where you wish to run the package:

.. code:: shell

    python3 -m venv venv
    source venv/bin/activate
    git clone https://github.com/brettharder/nba_predictions.git
    cd nba_predictions
    pip3 install .

Note: to do a regular install on your machine, skip the first two steps above. This is not guaranteed
to work however and will be dependant on your machine and python installation.  

Note
====

This project has been set up using PyScaffold 3.3.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
