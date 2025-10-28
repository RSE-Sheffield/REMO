# REMO - Replay with Modification

## Prerequisites
- Carla 0.9.15
- Python 3.8

## Installation Instructions
1. Set up and install Carla 0.9.15 according to its instructions
2. Clone this repository
3. Create a virtual environment and activate it

```
python3 -m venv ~/.venvs/carla
source ~/.venvs/carla/bin/activate
```
4. Install the required packages to the virtual environment for both carla and REMO

```
cd CARLA_ROOT/PythonAPI/examples
pip install -r requirements.txt
cd REMO_ROOT
pip install -r requirements.txt

```

5. Add the `REMO/src` folder to the python path


### Environment Configuration
Various environment variables can be configured to allow starting the carla server via the GUI etc.

TODO: Add instructions for this

## Usage
The REMO package can be used as a Python library or in GUI mode. To use the GUI,
run

```
python3 src/run_gui.py
```

Examples for using REMO as a library are given in the `src/examples` folder.

