'''
Created on Apr 14, 2018
@author: juanitoetc
@summary: simple Person class
'''

print("\nloading module...")			#This is absolutly not necessary and should be removed.
									#helps to understand that the module will not only laod, but also initilize the module.

class Person(object):

    def __init__(self, firstname, lastname, age):
        #For each class we need the constructor
        #this is where each instance is created
        #return an instance of the class
        self.strFirstName = firstname
        self.strLastName = lastname
        self.intAge = age
    
    def __str__(self):
        #method used to print the instance, usign print(<instance>)
        return self.strFirstName + " " + self.strLastName + ", " +str(self.intAge)
    
    def __eq__(self, other):
        #method used to compare to instances
        #return boolan True or False
        return self.strLastName==other.strLastName and self.strFirstName==other.strFirstName and  self.intAge==other.intAge

    def vchangeAge(self, intNewAge):
		self.intAge = intNewAge

print("module loaded")			#This is absolutly not necessary and should be removed.
									#helps to understand that the module will not only laod, but also initilize the module.
