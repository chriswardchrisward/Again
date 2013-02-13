#!/usr/bin/env python

#!/usr/bin/env python

class Node:
    def __init__( self , _value = None , _next = None ):
        self.value = _value
        self.next = _next
    def __str__( self ):
        return str(self.value )
        
class LinkedList:
    '''
    self.__count__= 0
    self.__listHead__ = None
    self.__listTail__ = None
    self.__listName__ = None
    '''
    def __str__(self):
        string = ""
        self.__node__ = self.__listHead__
        while self.__node__ != None:
            string = string + str(self.__node__.value) + " "
            self.__node__ = self.__node__.next
        print string
            
    def __init__(self, value):
        self.__count__ = 1
        self.__newNode__ = Node()
        self.__newNode__.__init__(value, None)
        self.__listHead__ = self.__newNode__
        
    def length(self):
        return self.__count__
    
    def addNode(self, new_value):
        self.__newNode__ = Node()
        self.__newNode__.__init__(new_value, None)
        self.__node__ = self.__listHead__
        while self.__node__.next != None:
            self.__node__ = self.__node__.next
        self.__node__.next = self.__newNode__
        self.__newNode__.next = None
        
        self.__count__ += 1
        
    def addNodeAfter(self, new_value, after_node):
        self.__newNode__ = Node()
        self.__newNode__.__init__(new_value, None) #correct None part later
        self.__node__ = self.__listHead__
        while self.__node__ != after_node:
            self.__node__ = self.__node__.next
            if self.__node__ == None:
                print "After Node not found"
                return
        self.__newNode__.next = self.__node__.next
        self.__node__.next = self.__newNode__
        
        self.__count__ += 1
        
    def addNodeBefore(self, new_value, before_node):
        self.__newNode__ = Node()
        self.__newNode__.__init__(new_value, None) # correct this later
        self.__node__ = self.__listHead__.next
        self.__pnode__ = self.__listHead__
        while self.__node__ != before_node:
            self.__pnode__ = self.__node__
            self.__node__ = self.__node__.next
            if self.__node__ == None:
                print "Before Node not found"
                return
        self.__newNode__.next = self.__node__
        self.__pnode__.next = self.__newNode__
        
        self.__count__ += 1
        
    def removeNode(self, node_to_remove):
        self.__pnode__ = self.__listHead__
        self.__node__ = self.__listHead__.next
        while self.__listHead__ == node_to_remove:
            self.__listHead__ = self.__listHead__.next
            self.__count__ -= 1
            return
        while self.__node__ != node_to_remove:
            self.__node__ = self.__node__.next
            self.__pnode__ = self.__pnode__.next
            if self.__node__ == None:
                print "These aren't the nodes you're looking for"
                return
        self.__pnode__.next = self.__node__.next
        self.__count__ -= 1


    def removeNodesByValue(self, value):
        while self.__listHead__.value == value:
            self.__listHead__ = self.__listHead__.next
            self.__count__ -= 1
            print 'deleted a begining node'
        self.__node__ = self.__listHead__.next
        self.__pnode__ = self.__listHead__
        while self.__node__ != None:
            if self.__node__.value == value:
                self.__pnode__.next = self.__node__.next
                self.__count__ -= 1
                print 'deleted a node'
            else:
                print 'did not delete a node'
            self.__pnode__ = self.__pnode__.next
            self.__node__ = self.__pnode__.next
            
    def reverse(self):
        if self.__listHead__ == None:
            return
        if self.__listHead__.next == None:
            return
        self.__pnode__ = self.__listHead__
        self.__cnode__ = self.__listHead__
        self.__nnode__ = self.__listHead__.next
        self.__listHead__.next = None
        while self.__nnode__ != None:
            self.__cnode__ = self.__nnode__
            self.__nnode__ = self.__cnode__.next
            self.__cnode__.next = self.__pnode__
            self.__pnode__ = self.__cnode__
        self.__listHead__ = self.__cnode__
        
