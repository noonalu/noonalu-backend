
# noonalu-backend
The back-end of noonalu!

## Development

### Setup Dev Environment
1. Setup virtual env
    - From the root of this directory
        ```py
        python3 -m venv venv
        ```
    - From any terminal you will be running python scripts in, to enter the virtual env run the following. 
        ```py
        source myvenv/bin/activate
        ```
    - In an activated terminal, from the root of the directory
        ```py
        pip3 install -r requirements.txt
        ```
2. Setup MongoDB
    - This is mostly painless using the docker image provided [here](https://hub.docker.com/_/mongo/). 
        ```py
        - docker pull mongo 
        - docker run -p 27017:27017 --name noon -v /my/own/datadir:/data/db -d mongo 
        ```
        This runs the docker container, opening port 27017 and linking the /my/own/datadir on your local machine to /data/db in the mongo container.
    - In a venv activated terminal, from the root of the directory, run
        ```py
        python3 setup/setup.py
        ```    
    - This should go through an instantiate the collection needed to store our data
3. Confirm all is working
    - In the venv, from the `src` directory, run
        ```py
        python3 -m flask run
        ```
        This brings up the api. 
    - In a separate (still venv activated) terminal, from the root directory, run
        ```py
        python3 test/api_test.py
        ```
        This will go through the existing endpoints and ensure they are running correctly.
