from setuptools import setup

SETUP = {
    "name": "scribbler2",
    "version": "4.1.1",
    "description": "Control del robot Scribbler S2 (Parallax) y tarjeta Fluke2 (BetterBots)",
    "license": "MIT",
    "author": "Roberto Carrasco",
    "author_email": "titos.carrasco@gmail.com",
    "maintainer": "Roberto Carrasco",
    "maintainer_email": "titos.carrasco@gmail.com",
    "packages": ["scribbler2", "scribbler2.Fluke2", "scribbler2.S2"],
    "package_dir": {"scribbler2": "scribbler2/"},
}

setup(**SETUP)
