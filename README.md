# Scribbler2-Python

Librería para controlar el robot Scribbler2  de Parallax:
- Implementa todas las funcionalidades de la librería MYRO del IPRE
- Implementa las funcionalidades de la tarjeta [Fluke2](http://www.betterbots.com/cshop/fluke2)
    - La tarjeta Fluke usa un timeout de 300ms por lo cual se deberá utilizar un timeout apropiado en algunos métodos
    - En Linux, ModemManager bloquea el acceso bluetooth a la tarjeta Fluke por lo cual debe ser desactivado


## Instalación
1. Requiere el paquete pyserial (`pyserial`)
2. Descargue el último release desde [GitHub](https://github.com/titos-carrasco/Scribbler2-Python)
2. Instale el wheel con `pip install scribbler2-4.0.0-py3-none-any.whl`


## Demos
- Descarge los demos desde la zona de release de github


## Desarrollo
- La librería se puede instalar para desarrollo con `pip3 install --user -e .`
- Verificar formato del código con `pydocstyle scribbler2`
- La documentación se genera con `pdoc -o docs/  scribbler2 scribbler2.robot`
- El wheel debe ser generado con `python setup.py bdist_wheel`


