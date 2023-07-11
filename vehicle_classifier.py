class Vehicle:
    def start(self):
        print("Vehicle Started")
    def stop(self):
        print("Vehicle Stopped")
class Car(Vehicle):
     def start(self):
         print("Car Started")
     def stop(self):
         print("Car Stopped")
class MotorCycle(Vehicle):
    def start(self):
        print("MotorCycle Started")
    def stop(self):
        print("MotorCycle Stopped")
obj = MotorCycle()
obj.start()
obj2 = Car()
obj.start()
obj3 = Vehicle()
obj.start()
obj.stop()