# PLANT-AI

## Install:

### MacOs:

* Open a terminal
* Install _Homebrew_: https://brew.sh/
* Install _pyenv_ using _Homebrew_: https://github.com/pyenv/pyenv#unixmacos
* Install _Python 3.12_ using _pyenv_: `pyenv install 3.12`
* Install _poetry_: https://python-poetry.org/docs/
* Inside the _plantAI_ folder, install the python dependencies running the following 2 commands:
  * `poetry shell`
  * `poetry install`
* Run the App: `python plantai/main.py`

## Using the App:

![plantAI.png](images%2FplantAI.png)

* Press the _Start_ button to start sending OSC messages
* If needed, adjust the individual dispatch time for each plant
* Each plant can also have its messages turned on / off using the toggle switch
* The format of the OSC messages is:

  `/plant1: ('1954', '4095', '173', '301765', '112')`

  `/plant2: ('1760', '4095', '80', '518974', '113')`

  `/plant3: ('1786', '4095', '2544', '613606', '114')`

  `/plant4: ('1780', '4095', '161', '677640', '115')`

  `/plant5: ('1843', '4095', '170', '752548', '116')`

  `/plant6: ('1819', '4095', '2548', '1266141', '118')`

* The OSC server is running on _localhost_ port _2222_