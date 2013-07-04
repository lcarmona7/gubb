#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from uuid import uuid4

def generarid():
	idx = str(uuid4().hex)[27:32]
	return idx

def dbname():
	return 'gubb.db'