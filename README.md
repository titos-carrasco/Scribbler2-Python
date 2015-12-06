Scribbler2-Python
=================

Código Python para controlar a través de bluetooth el robot Scribbler2 (S2)
con la tarjeta Fluke2 (F2), ver detalles en www.betterbots.com / www.parallax.com.

* Implementa todas las funciones del S2 (Firmware IPRE)
* Implementa la mayoría de las funciones de la tarjeta F2

El problema mayor lo genera la Fluke2 dado que al interactuar con el Scribbler2 maneja un timeout
de 3000ms. Si el Scribbler2 tarda más de ese tiempo los siguientes comandos quedarán
fuera de sincronismo.

La documentación se encuentra en el proyecto Scribbler2-Java en JavaDoc

##Ambiente de desarrollo
Todo el desarrollo se realiza utilizando Geany en Linux Debian, configurando un proyecto y asociando comandos en Set Build Commands:

* Para compilar en Python: python -m py_compile "%f"
* Para ejecutar Python: python "%f"

***
##Historia
* Dic 05, 2015: Implementa funciones de control de los servo
* Abr 22, 2015: Se mueve todo el código Python hacia el proyecto Scribbler2-Python
* Abr 19, 2015: V2.0.1 con el código en Java y en Python más cercano a OO
* Abr 15, 2015: Preparando V2.0.0 en branch developer con código Java más cercano a OO. Queda pendiente el código Python y el Cpp
* Abr 02, 2015: Se depuran las operaciones de PATH. Se reescribe el código python tomando
como base el código en Java
* Mar 29, 2015: Implementa versión en Java corrigiendo una serie de
errores ocasionados por el timeout de 3000ms impuesto por la Fluke2 en
su ciclo principal. El código es reescrito completamente
* May 9, 2014: Primer commit

