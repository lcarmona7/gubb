#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

class domicilio(object):
	"""Clase Domicilio"""
	def __init__(self, barrio, tipo):
		self.barrio = barrio
		self.tipo = tipo

	def setbarrio(self, barrio):
		self.barrio = barrio

	def getbarrio(self):
		return self.barrio

	def settipo(self, tipo):
		self.tipo = tipo

	def gettipo(self):
		return self.tipo		