#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from lib.usuario import usuario
from lib.extra import generarid

nuevo = usuario("luis alberto","carmona","vasquez",generarid(),2)
print(nuevo.getclave())