class Car:
       total_car=0
       def __init__(self,brand,model):
           self.__brand=brand
           self.__model=model
           Car.total_car+=1
       def full_name(self):
             return f"{self.__brand}{self.__model}"
       def get_brand(self):
             return self.__brand+" !"
       def get_model(self):
             return self.__model
       def fuel_type(self):
             return "Petrol or Disel"
       def speed(self):
             return "120KM"
       @staticmethod
       def general_description():
             return "cars are means of transport"
       @property
       def model(self):
             return self.__model
class battery:
      def battery_info(self):
            return "This is Battery"
class engine:
      def engine_info(self):
          return "This is engine"
class ElectricCarTwo(battery,engine,Car):
      pass
class ElectricCar(Car):
      def __init__(self,brand,model,battery_size):
            super().__init__(brand,model)
            self.battery_size=battery_size
      def fuel_type(self):
            return "Electric charge"
      def speed(self):
           return "100KM"
      @staticmethod
      def general_description():
            return "car is trasport"
# my_tesla=ElectricCar("TATA","Safari","85KWh")
my_tesla1=ElectricCarTwo("Tesla","model S")
print(my_tesla1.battery_info())
print(my_tesla1.engine_info())
# print(my_tesla.fuel_type())
# print(my_tesla.speed())
# safari=Car("TATA","safari")
# Car=("TATA","Nexon")
# print(safari.get_model())
# print(safari.model)
# print(isinstance(my_tesla,ElectricCar))
# print(isinstance(my_tesla,Car))
# print(safari.general_description())
# print(safari.fuel_type())
# print(safari.speed())
# print(Car.total_car)
# print(my_tesla.model)
# print(my_tesla.brand)
# print(my_tesla.battery_size)
# print(my_tesla.get_brand())
# print(my_tesla.get_model())
# my_car=Car("Toyota","Corolla")
# print(my_car.full_name())
# print(my_car.brand)
# print(my_car.model)