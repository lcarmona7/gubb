#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

class persona(object):
	"""Clase Persona """
	def __init__(self, nombre, paterno, materno):
		self.nombre = nombre
		self.paterno = paterno
		self.materno = materno

	def setnombre(self, nombre):
		self.nombre = nombre

	def getnombre(self):
		return self.nombre

	def setpaterno(self, paterno):
		self.paterno = paterno

	def getpaterno(self):
		return self.paterno

	def setmaterno(self, materno):
		self.materno = materno

	def getmaterno(self):
		return self.materno