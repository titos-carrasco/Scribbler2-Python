# -*- coding: utf-8 -*-

"""
Instalación de la libreria del S2.

Utilizar para uso normal:
    - $ pip install --user .
    - $ pip3 install --user .

Utilizar para desarrollo:
    - $ pip install --user -e .
    - $ pip3 install --user -e .
"""

from setuptools import setup
from codecs import open
from os import path

if __name__ == "__main__":
    #here = path.abspath(path.dirname(__file__))

    setup(
        name='S2-Python',
        version='3.2.4',
        description='Library for controlling the Parallax Scribbler S2 robot using the Fluke2 card from BetterBots',
        #long_description=long_description,
        url='https://github.com/titos-carrasco/Scribbler2-Python',
        author='Roberto Carrasco',
        author_email='titos.carrasco@gmail.com',
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
        packages=['rcr','rcr.robots', 'rcr.robots.scribbler2', 'rcr.robots.fluke2', 'rcr.robots.net2', 'rcr.utils'],
    )
