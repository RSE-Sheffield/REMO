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

### Test Suite
A test suite is provided which uses the `pytest` framework. The tests are present in the `src/tests` folder and can be run by using the `pytest` command from the `src` directory.

### API
To run an example, navigate to the `src` folder and run the command:

`python3 examples/EXAMPLE_NAME`

where `EXAMPLE_NAME` is one of the following:

- `launch_server.py` Starting the UE4 Carla server via the API
- `nearby_objects.py` Querying a set of environment objects within a given radius of a given location, and then filtering that set to only include those of type "Poles"
- `api_example_run_scenario.py` Launching a scenario, using manual control to control the ego vehicle. The scenario is recorded for 20 seconds, after which the metadata is written to the default location. The metadata and replay file are then reloaded, with the ego vehicle replaced by a new one which is independently controlled.
- `play_replay.py` Launching a replay with modified ego vehicle without first immediately recording the scenario. N.B. you must run the `api_example_run_scenario.py` example before running this one, or there will be no replay metadata to load.
- `verify_stable_ids.py` Verifies that object ids are consistent across multiple replays of a scenario
- `remove_fences.py` Shows how to remove objects of a certain type within a given radius of the ego vehicle

### GUI
TODO

