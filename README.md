# Scribbler2-Python

Librería para controlar el robot Scribbler2  de Parallax:
- Implementa todas las funcionalidades de la librería MYRO del IPRE
- Implementa las funcionalidades de la tarjeta [Fluke2](http://www.betterbots.com/cshop/fluke2)
    - La tarjeta Fluke usa un timeout de 300ms por lo cual se deberá utilizar un timeout apropiado en algunos métodos
    - En Linux, ModemManager bloquea el acceso bluetooth a la tarjeta Fluke por lo cual debe ser desactivado
- En el conector DB9:
    - El S2 coloca 9v en CTS lo que puede destruir un conector USB a RS232 que opere con niveles TTL
    - El S2 requiere que DTR tenga un voltaje alto. Un voltaje bajo lo resetea


## Instalación
1. Requiere el paquete pyserial (`pyserial`)
2. Descargue el último release desde [GitHub](https://github.com/titos-carrasco/Scribbler2-Python)
2. Instale el wheel con `pip install scribbler2-x.y.z-py3-none-any.whl`


## Demos
- Descarge los demos desde la zona de release de github


## Desarrollo
- Utilizar venv
- La librería se puede instalar para desarrollo con `pip install -e .`
- La documentación se genera con `pdoc -o docs/ scribbler2`
- El wheel debe ser generado con `python setup.py bdist_wheel`

## Conexión
- Con FTDI: usar DTR=None (default) o DTR=True
![](./Images/Conexion_FTDI.png)
