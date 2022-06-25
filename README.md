### "hexlet-code"(gendiff) python package
[![Actions Status](https://github.com/pavelkalenchuk/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/pavelkalenchuk/python-project-lvl2/actions)  [![Python CI](https://github.com/pavelkalenchuk/python-project-lvl2/actions/workflows/Test.yml/badge.svg)](https://github.com/pavelkalenchuk/python-project-lvl2/actions/workflows/Test.yml)  [![Maintainability](https://api.codeclimate.com/v1/badges/501f31bcfd20c55cdb47/maintainability)](https://codeclimate.com/github/pavelkalenchuk/python-project-lvl2/maintainability)  [![Test Coverage](https://api.codeclimate.com/v1/badges/501f31bcfd20c55cdb47/test_coverage)](https://codeclimate.com/github/pavelkalenchuk/python-project-lvl2/test_coverage)

### Description
Python package "hexlet-code"(gendiff) is a CLI tool that provides the ability to compare two configuration files.
With  CLI command 'gendiff' user get a difference between two configuration (JSON, YAML) files.
Result of a compare show a properties from a files and inform about value(s) of property, and  state of every property:
 - property was added
 - property was removed
 - property was not changed, values are equal for both files
 - property was not changed, values are different

'gendiff' can work with properties where value(s) is a JSON or YAML 

features:
 - support JSON, YAML(YML) files
 - 3 output format views

Present repository is a training python-package (student's training project on online educational platform [hexlet.io](https://ru.hexlet.io/)).
author: Pavel Kalenchuk
e-mail: pavel.kalenchuk@gmail.com.

Minimal Python version - 3.8

Project was created with next tools:
| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [poetry](https://poetry.eustace.io/)                                        | "Python dependency management and packaging made easy"  |
| [Py.Test](https://pytest.org)                                               | "A mature full-featured Python testing tool"            |
| [flake8](https://flake8.pycqa.org/en/latest/)                               | "Flake8: Your Tool For Style Guide Enforcement"         |
| [black](https://black.readthedocs.io/en/stable/#)                           | "The Uncompromising Code Formatter"                     |

### Installation
#### with poetry tool and make command:
clone a repository:
```sh
git clone https://github.com/pavelkalenchuk/python-project-lvl2.git
```
in repository directory type next command:
```sh
make build
```
```sh
make install
```
#### with pip (from test.PyPi):
```sh

```


### Usage:

#### stylish formatter(default formatter):
[![asciicast](https://asciinema.org/a/OsTHFFU0mKEqplxgtAwgI1tYQ.svg)](https://asciinema.org/a/OsTHFFU0mKEqplxgtAwgI1tYQ)

#### plain formatter:
[![asciicast](https://asciinema.org/a/EP2utRC3lD0Y3IEwN9kLnmrkx.svg)](https://asciinema.org/a/EP2utRC3lD0Y3IEwN9kLnmrkx)

#### json formatter:
[![asciicast](https://asciinema.org/a/usb8X130k34Gy06UxzBlY5L1Y.svg)](https://asciinema.org/a/usb8X130k34Gy06UxzBlY5L1Y)