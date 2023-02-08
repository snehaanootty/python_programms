class A:
   var1=None  #public data member
   _var2=None  #protected data member
   __var3=None  #private data member

#constructor
   def __init__(self,var1,var2,var3):
       self.var1=var1
       self._var2=var2
       self.__var3=var3
   def displayPublicMembers(self): #public member function
       print("public data member:",self.var1) #accessing public datamember
   def _displayProtectedMember(self):
       print("protected data member:",self._var2)
   def __displayPrivateMember(self):
       print("private data member:",self.__var3)
   def accesPrivateMember(self):
        self.__displayPrivateMember()

#derived class
class B(A):
   def __init__(self,var1,var2,var3): #constructor
        A.__init__(self,var1,var2,var3)

   def accessProtectedMembers(self): #accessing protected me
        self._displayProtectedMember()

#creating objects of derived class
obj=B('pub_red',"pro_white","private_green")
#calling public member function of the class
obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accesPrivateMember()
#obj.accessprivate member
#object can access public member
print("object is accessing public member:",obj.var1)
print("object is accessing protected member:",obj._var2)
print(obj._A__var3)