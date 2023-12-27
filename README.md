# extdistcc
Extended tools for the distcc utility

## Getting Started
To get this package, download it through releases or to get souruce code,
```console
git clone https://github.com/SyedMustafaAhmad/extdistcc.git
```
The dependencies are listed in the [requiremments.txt](https://github.com/SyedMustafaAhmad/extdistcc/blob/main/requirements.txt) package and can be automatically installed by following the below setup instructions.

<hr/>

## Setup
It is recommended to start with a python virtual environment. On Linux,
```console
python3 -m venv venv
```
<br/>

To enter venv (virtual environment) on Linux,
```console
source venv/bin/activate
```
On Windows,
```console
.\venv\Scripts\Activate.ps1
```
<br/>

To pull this application's python dependencies use the command,
```console
pip install -r requirements.txt
```
<br/>

To use application on Linux,
```console
python3 main.py [--OPTIONS] [COMMAND] [ARGUMENTS]
```
<br/>

To get list of available commands and help on Linux,
```console
python3 main.py --help
```