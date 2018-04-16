'''
Created on Apr 13, 2018
@author: juanioetc
@sumary: just a short example of the usage of imp
@attention: this method will be probably deprecated, see issue https://bugs.python.org/issue14551
'''

#there is no need to import a complete py using from ... import ...

import imp

print("Usage of the imp library, load_source in particular")
try:
	#Try to import the module located in the path given
	impPerson = imp.load_source("classPerson","./Person.py")
except IOError as errorImport:
	#Exception handler: file not found, inform this using console and skip this module
	print("File not imported, error: ", errorImport)
else:
	#import sucessfull cp = class Person
	cpPerson1 = impPerson.Person("Juan", "Robledo", 27)	#constructor of the class in the module imported.
	print("\n")
	print(cpPerson1)	#using __str__ in the class declaration
finally:
	cpPerson1.vchangeAge(5)
	print(cpPerson1)
	print("End of the example.")
	
