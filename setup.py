# -*- coding: utf-8 -*-

"""
Instalación de la libreria del S2.

Utilizar para uso normal:
    - $ pip install .
    - $ pip3 install .

Utilizar para desarrollo:
    - $ pip install -e .
    - $ pip3 install -e .
"""

from setuptools import setup
from codecs import open
from os import path

if __name__ == "__main__":
    #here = path.abspath(path.dirname(__file__))

    setup(
        name='S2-python',
        version='3.2.2',
        description='Library for controlling the Parallax Scribbler S2 robot using the Fluke2 card from BetterBots',
        #long_description=long_description,
        url='https://github.com/titos-carrasco/Scribbler2-Python',
        author='Roberto Carrasco',
        author_email='titos.carrasco@gmal.com',
        license='The MIT License (MIT)',
        classifiers=[
            'Development Status :: 5 - Production/STable',
            'Intended Audience :: Education',
            'Topic :: Education :: Computer Aided Instruction (CAI)',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
        ],
        keywords='robot education programming',
        packages=['rcr.utils','rcr.robots.scribbler2'],
    )
