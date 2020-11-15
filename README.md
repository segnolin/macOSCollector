# macOSCollector

macOSCollector is the artifact collector on macOS for malware analysis. For simplicity, we only include one submodule. Users can follow the instruction below to add their own submodules.

## Getting Started

Simply cloning the project.

```
git clone https://github.com/segnolin/macOSCollector.git
```

### Prerequisites

- Scripts require Python 3.6+

### Install Submodules

Go to the project directory.

```
cd macOSCollector
```

Run the installation script.

```
python3 run.py --install
```

### Collecting

After installing the submodules, run the collecting script.

```
python3 run.py --collect
```

The artifacts will be at `./artifacts` folder

## Documentation

This section shows to tweak and add the functionality of the collecting and detection tools.

### Usage of macOSCollector

```
usage: run.py [-h] [-i] [-c]

optional arguments:
  -h, --help     show this help message and exit
  -i, --install  installing requirements for submodules
  -c, --collect  collecting artifacts
```

### Adding Submodule

The procedure of adding submodule consists of the following three parts. Each part is necessary for the submodule to work properly.

#### Submodule Installation

The following properties of installation of submodules can be found in `requirements.json`:

```
[
  {
    "name": string (Name of submodule),
    "commands": array[string] (series of commands that install the submodule),
  },
  ...
]
```

#### Submodule Execution

The following properties of executing of submodules can be found in `submodules.json`:

```
[
  {
    "name": string (Name of submodule),
    "commands": array[string] (series of commands that run the submodule),
  },
  ...
]
```

#### Submodule Output Parsing

Each submodule should have its parsing script for output file consistency.
The script should be written in Python 3.6+ with the file name `[Name of submodule].py` inside `./modules` folder.
The output path of the parsing script should be `./artifacts/[Name of submodule]` folder.
The parsing function prototype describes as below:

```py
def parse():
  # parse the the artifacts file into json output
```

## Reference

* [CrowdStrike/automactc](https://github.com/CrowdStrike/automactc)
