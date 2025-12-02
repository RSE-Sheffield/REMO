# REMO - Replay with Modification

## Prerequisites
- Carla 0.9.15
- Python 3.8

## Installation Instructions
### Python 3.8
#### Install using PyEnv (recommended)
Install the `pyenv` application via your package manager, e.g.

`sudo apt install pyenv`

Install Python 3.8 using pyenv:

`pyenv install 3.8`

Open a shell using Python 3.8:

`pyenv shell 3.8`

### Carla
Set up and install [Carla 0.9.15](https://github.com/carla-simulator/carla/releases/tag/0.9.15) according to [its instructions](https://carla.readthedocs.io/en/latest/start_quickstart/)

### REMO

1. Clone this repository
2. Create a virtual environment using the Python 3.8 shell and activate it

```
python -m venv ~/.venvs/carla
source ~/.venvs/carla/bin/activate
```
3. Install the required packages to the virtual environment for both carla and REMO

```
cd REMO_ROOT
pip install -r requirements.txt

```

4. Add the `REMO/src` folder to the python path


### Environment Configuration
Two environment variables should be configured to allow starting the carla server via  etc.

#### Virtual Environment
If using a virtual environment, edit the `activate` script in a text editor, e.g.

`vim ~/.venvs/carla/bin/activate`

Append the following two lines and update the paths according to your installation

    export REMO_SCENARIO_RUNNER_ROOT="/path/to/scenario_runner"
    export REMO_CARLA_SERVER_ROOT="/path/to/carla_server"
    
Reactivate your virtual environment to load the updated environment:

`source ~/.venvs/carla/bin/activate`


## Usage
Examples for using REMO as a library are given in the `src/examples` folder.

