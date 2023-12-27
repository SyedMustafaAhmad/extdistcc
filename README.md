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
It is recommended to start with a python virtual environment. On Unix-based systems,
```console
python3 -m venv venv
```
On Windows,
```console
python -m venv venv
```

To enter venv (virtual environment) on Unix-based systems,
```console
source venv/bin/activate
```
On Windows,
```console
.\venv\Scripts\Activate.ps1
```

To pull this application's python dependencies use the command,
```console
pip install -r requirements.txt
```

To use package on Unix-based systems,
```console
python3 main.py [--OPTIONS] [COMMAND] [ARGUMENTS]
```
On Windows,
```console
python3 main.py [--OPTIONS] [COMMAND] [ARGUMENTS]
```

To get list of available commands and help on Unix-based systems,
```console
python3 main.py --help
```
On Windows,
```console
python main.py --help
```