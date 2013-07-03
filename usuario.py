#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from persona import persona

class usuario(persona):
	"""Clase usuario"""
	def __init__(self, nombre, paterno, materno, clave, cantidad):
		self.nombre = nombre
		self.paterno = paterno
		self.materno = materno
		self.clave = clave
		self.cantidad = cantidad

	def setclave(self, clave):
		self.clave = clave

	def getclave(self):
		return self.clave

	def setcantidad(self, cantidad):
		self.cantidad = cantidad

	def getcantidad(self):
		return self.cantidad		