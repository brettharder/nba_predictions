===============
nba_predictions
===============


nba_predictions is package that allows one to quickly scrape nba data and 
model points scored for a given player.


Installation
============

Docker (recommended)
--------------------

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

Via Virtualenv
--------------

To install into a virtualenv do the following steps in a directory where you wish to run the package:


.. code:: shell

    python3 -m venv venv
    source venv/bin/activate
    git clone https://github.com/brettharder/nba_predictions.git
    cd nba_predictions
    pip3 install .


Note: to do a regular install on your machine, skip the first two steps above. This is not guaranteed
to work however and will be dependant on your machine and python installation.  


Usage
=====

Currently, main functionality for this package can be called through `/src/runner.py` which uses
argparser to allow for commandline args. This is added as an entrypoint to setup.py and setup.cfg
to allow for users to easily call the package. 

The main modes for this package are ``parse-player-data``, ``feature-engineer``, ``train-model``, and ``predict``. 
Each of which can be run sequentially to build a model and make predictions for a given players points 
per game. 

When the package is installed a user can see help for the package using


.. code:: shell

    nba_predictions -h


Below we go into the 4 differnt modes...


Parse Player Data
-----------------

Parsing player data hits https://www.basketball-reference.com/ and will save a csv of game logs for a given number of 
years for a player. The data will be saved in ``./data/``, or a directory of the user's choosing. 

E.g. Here we pull 2018-2020 data for James Harden


.. code:: shell

    nba_predictions \
    parse-data \
    --player-first-name James \
    --player-last-name Harden \
    --years 2018 2019 2020 \


Feature Engineer
----------------

Feature engineering will take in output of the above parser and prepare the data for modelling. 
Currently build the following features
  use past 10 games as input for predicting performance in next game:
    - average minutes played: MP
    - average field goal attempted: FGA
    - average field goal percentage: FG%
    - average 3point attempted: 3PA
    - average 3point percentage: 3P%
    - average free throw attempted: FTA
    - average free throw percentage: FT%    
    - average turnovers: TOV
    - average personal fouls: PF
    - average points: PTS
TOD: add more complex/different types of features. 
Perhaps keep data in a more raw state for sequential modelling (LSTM).


E.g. Run feature engineering on James Harden data pulled above.


.. code:: shell

    nba_predictions \
    feature-engineer \
    --player-data $(pwd)/../data/Lebron_James_2018_2019_2020.csv



Train Model
-----------

TODO... for now a test script trains and evaluates a model ``/scripts/xgb_model_test.py``

Predict
-------

TODO... 


Note
====

This project has been set up using PyScaffold 3.3.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
