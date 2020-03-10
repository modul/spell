import re
from setuptools import setup

version = re.search(
    r'^VERSION\s=\s"(.*)"',
    open('spell/spell.py').read(),
    re.M
    ).group(1)

name = re.search(
    r'^NAME\s=\s"(.*)"',
    open('spell/spell.py').read(),
    re.M
    ).group(1)

setup(
    name = name,
    version = version,
    packages = [name],
    install_requires = [
        "pyyaml"
    ],
    package_data = {
        "spell": ["tables/*.yml"]
    },
    entry_points = {
        "console_scripts": ["spell=spell.spell:main"]
    },
    description = "Spell text using a spelling alphabet",
    long_description = "Commandline utility to spell any given text using different spelling alphabets.",
    author = "Remo Giermann",
    author_email = "mo@liberejo.de",
)
