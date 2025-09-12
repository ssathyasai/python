from abc import ABC, abstractmethod

class Vehicle:
    def __init__(self, plate, owner, vtype):
        self.__plate = plate
        self.__owner = owner
        self.vtype = vtype
    def get_plate(self):
        return self.__plate
    def get_owner(self):
        return self.__owner
    def display(self):
        print(self.vtype, self.__plate, self.__owner)
    def fee(self,h):
        raise NotImplementedError

class Bike(Vehicle):
    def __init__(self, plate, owner):
        super().__init__(plate, owner, "Bike")
    def display(self):
        print("Bike:", self.get_plate(), self.get_owner())
    def fee(self,h):
        return 20*h

class Car(Vehicle):
    def __init__(self, plate, owner):
        super().__init__(plate, owner, "Car")
    def display(self):
        print("Car:", self.get_plate(), self.get_owner())
    def fee(self,h):
        return 50*h

class SUV(Vehicle):
    def __init__(self, plate, owner):
        super().__init__(plate, owner, "SUV")
    def display(self):
        print("SUV:", self.get_plate(), self.get_owner())
    def fee(self,h):
        return 70*h

class Truck(Vehicle):
    def __init__(self, plate, owner):
        super().__init__(plate, owner, "Truck")
    def display(self):
        print("Truck:", self.get_plate(), self.get_owner())
    def fee(self,h):
        return 100*h

class Spot:
    def __init__(self, sid, size):
        self.sid = sid
        self.size = size
        self.veh = None
    def assign(self,v):
        if v.vtype=="Bike" and self.size in ["S","M","L","XL"]:
            pass
        elif v.vtype=="Car" and self.size in ["M","L","XL"]:
            pass
        elif v.vtype=="SUV" and self.size in ["L","XL"]:
            pass
        elif v.vtype=="Truck" and self.size=="XL":
            pass
        else:
            return False
        if self.veh is None:
            self.veh=v
            return True
        return False
    def remove(self):
        v=self.veh
        self.veh=None
        return v
    def show(self):
        st="Free" if self.veh is None else "Busy"
        print("Spot",self.sid,self.size,st)

class Lot:
    def __init__(self):
        self.spots=[]
    def add(self,sid,size):
        self.spots.append(Spot(sid,size))
    def show(self):
        for s in self.spots:
            s.show()
    def park(self,v):
        for s in self.spots:
            if s.assign(v):
                print(v.vtype,"Parked at",s.sid)
                return True
        print("No spot for",v.vtype)
        return False
    def unpark(self,v,h):
        for s in self.spots:
            if s.veh==v:
                s.remove()
                amt=v.fee(h)
                print(v.vtype,"Unparked, Fee:",amt)
                return amt
        return 0

class Pay(ABC):
    @abstractmethod
    def process(self,amt):
        pass

class CashPay(Pay):
    def process(self,amt):
        print("Paid",amt,"by Cash")

class CardPay(Pay):
    def process(self,amt):
        print("Paid",amt,"by Card")

class UPIPay(Pay):
    def process(self,amt):
        print("Paid",amt,"by UPI")

lot=Lot()
lot.add(1,"S")
lot.add(2,"M")
lot.add(3,"L")
lot.add(4,"XL")

v1=Bike("AP01","Sai")
v2=Car("AP02","Ram")

v1.display()
v2.display()

lot.park(v1)
lot.park(v2)
lot.show()

amt=lot.unpark(v2,2)
p=UPIPay()
p.process(amt)
