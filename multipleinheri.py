#multiple inheritance


#class triangle
class Triangle:
    
    def __init__(self,base=3,height=5):
        self.base=base
        self.height=height
        self.area=0.5*base*height
    def display(self):
    
         print("the area of triangle is ",self.area)
        # class sphere
class sphere:
    def __init__(self,radius=2):
       self.radius=radius
       self.area=3.4*radius**2
    def display(self):
        print("area of sphere :",self.area)
        
   
        # class cone 
class cone(Triangle,sphere):
    
    def __init__(self,radius=3,height=5):
        Triangle.__init__(self)
        sphere.__init__(self)
        self.radius=radius
        self.height=height
        self.volume=(3.14*radius**2)*height/3
    def display(self,*args):
        Triangle.display(self)
        sphere.display(self)
        print("the volume of the cone is",self.volume)
            
        for i in args:
            
            print(i)
            
coneobj=cone()
coneobj.display(12,34,55)

