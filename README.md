# Scribbler2-Python

Librería para controlar el robot Scribbler2 de Parallax vía Serial o Bluetooth:

- Implementa todas las funcionalidades de la librería MYRO del [IPRE](https://bitbucket.org/ipre)
- Implementa las funcionalidades de la tarjeta Fluke2 de BetterBots
    - La tarjeta Fluke usa un timeout de 300ms por lo cual se deberá utilizar un timeout apropiado en algunos métodos
    - En Linux, ModemManager bloquea el acceso bluetooth a la tarjeta Fluke por lo cual debe ser desactivado
- En el conector DB9 (hembra) del robot:
    - El S2 opera con lógica invertida
    - El S2 coloca 9V en el pin 7 (CTS) lo que puede destruir un conector USB a RS232 que opere con niveles TTL
    - El S2 acepta voltajes de entrada entre -12v (V-) y 12v (V+)
    - El voltaje presente en el pin 5 (DTR) se utiliza como V-
    - El pasar de V+ a V- en DTR ocasiona que el S2 se resetee
    - En el pin 2 (TXD) el S2 coloca 3.3V como V+ al transmitir
    - En el pin 3 (RXD) el S2 convierte V+ a 3.3v al recibir

## Instalación
    $ python -m venv .venv
    $ . ./.venv/bin/activate
    (.venv)$ pip install pyserial
    (.venv)$ pip install https://github.com/titos-carrasco/Scribbler2-Python/releases/download/v4.1.1/scribbler2-4.1.1-py3-none-any.whl

## Desarrollo
    $ python -m venv .venv
    $ . ./.venv/bin/activate
    (.venv)$ pip install pyserial setuptools wheel pdoc
    (.venv)$ pip install -e .

## Despliegue
    (.venv)$ python setup.py bdist_wheel

    (.venv)$ pdoc -o docs/ scribbler2
    (.venv)$ zip -r dist/docs.zip docs/

    (.venv)$ zip -r dist/demos.zip demos/


## Conexión serial
- Caso conversor USB a RS232 niveles TTL sin manipular DTR

<img src="./Images/Conexion_FTDI.png" width=480 align="left"/>
