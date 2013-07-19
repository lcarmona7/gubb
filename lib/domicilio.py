#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

class domicilio():
	"""Clase Domicilio"""
	def __init__(self, clave, barrio, tipo, mes, anio, dueno):
		self.clave = clave
		self.barrio = barrio
		self.tipo = tipo
		self.mes = mes
		self.anio = anio
		self.dueno = dueno

	def setclave(self, clave):
		self.clave = clave

	def getclave(self):
		return self.clave

	def setbarrio(self, barrio):
		self.barrio = barrio

	def getbarrio(self):
		return self.barrio

	def settipo(self, tipo):
		self.tipo = tipo

	def gettipo(self):
		return self.tipo

	def setmes(self, mes):
		self.mes = mes

	def getmes(self):
		return self.mes

	def setanio(self, anio):
		self.anio = anio

	def getanio(self):
		return self.anio

	def setdueno(self, dueno):
		self.dueno = dueno

	def getdueno(self):
		return self.dueno