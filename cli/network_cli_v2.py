'''
Created on Jan 4, 2014

@author: jeff
'''


class MyClass(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.name = 'jeff'
        self.anothername = 'coho'

    def print_name(self):
        print self.name

    def print_another_name(self):
        print self.anothername
