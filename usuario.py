#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

class usuario(object):
	"""Clase usuario"""
	def __init__(self, clave, cantidad):
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