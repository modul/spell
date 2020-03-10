<img align="right" width="25%" src="./icon.svg" alt="spellbook icon"/>

# Spell

Spell is a CLI tool and library to spell a given text using different spelling alphabets:

```sh
$ spell Foobar fantastic!
FOXTROTT, oscar, oscar, bravo, alfa, romeo
foxtrott, alfa, november, tango, alfa, sierra, tango, india, charlie, !
$
```

## Installation

Clone this repository and use `pip` or `setup.py` to install:

```sh
# With pip:
cd spell
pip install --user .

# With setup.py:
python setup.py install --user
```

## Usage

```
spell [-h] [--version] [--table {german,itu}] text [text ...]

Spell text using a spelling alphabet

positional arguments:
  text                  text to be spelled

optional arguments:
  -h, --help            show this help message and exit
  --version, -v         show program's version number and exit
  --table {german,itu}, -t {german,itu}
                        spelling table to use (default: itu)
```

## Credits

Icon by [Chanut is Industries](https://www.iconfinder.com/Chanut-is).
