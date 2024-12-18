#methods:call,text,view,watch
class Phone:#parent class
    def __init__(self,brand,model,storage,color,release_year):
        self.model=model
        self.brand=brand
        self.storage=storage
        self.color=color
        self.release_year=release_year
    def capacity(self):#default constructor
        print(self.model," phone has a storage of",self.storage,"and it was released in the year",self.release_year)
    def specs(self):#method
        print(self.brand,"is one of the  phone that is commonly used and most ladies like it with a",self.color,"casing")
    def call(self):
        print("You can contact me using +254789643764")
    def text(self,message):#parameterized constructor
        print("Lately i have receiving calls from +254789564732 and texts that say ",message)
class Smartphone(Phone):#child class
    def __init__(self,brand,model,storage,color,release_year,price,camera):
        super().__init__(brand,model,storage,color,release_year)#inheritance
        self.price=price
        self.camera=camera
    def call(self):#polymorphism
        print("Many phone numbers are 10-digit eg +254789564732")
    def quality(self):
        print(self.brand,"has a camera with a resolution of",self.camera,"MP making it cost",self.price)
    def watch(self,website):
        print("Lately i havebeen watching movies from the",website,"website using my",self.brand,self.model)
ph=Phone("Apple","Iphone16","128GB","pink",2023)
ph.capacity()
ph.specs()
ph.call()
ph.text("'How did you win that lottery?'")
ph1=Smartphone("Samsung","GalaxyS23","128GB","black","2022","$7000","200")
ph1.quality()
ph1.watch("Goojara")
for x in(ph,ph1):
    x.call()


