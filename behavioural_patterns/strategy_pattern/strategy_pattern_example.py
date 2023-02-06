# This example takes into account a problem that can be solved with strategy design pattern. In this example we take
# a problem of vehicles. Suppose we have a vehicle class which has a method drive() method, which results in moving a
# vehicle.
# Now if we extend this base class into classes like passenger vehicle, sports vehicle, SUV vehicle etc.
# Now when we subclass this Vehicle class we will need to implement this drive() method. As such there is no problem
# with that but imagine this, there could be any number of subclasses derived from Vehicle class and its much probable
# that they will be implementing this drive() method in same way which will lead to code duplicacy. Here we can use
# strategy pattern. We can have an interface(abstract class) called DriveStrategy which will have an abstract method
# drive(). This DriveStrategy can be subclasses with concrete strategies which will be use by actual vehicle class.
# Then subclasses will have an attribute to store reference to this strategy. Lets implement this now.


from abc import ABC, abstractmethod


class DriveStrategy(ABC):
    @abstractmethod
    def drive(self):
        print("Vehicle is driving.")


class SportsDriveStrategy(DriveStrategy):
    def drive(self):
        print("Sports car is driving.")


class PassengerCarDriveStrategy(DriveStrategy):
    def drive(self):
        print("Passenger car is driving.")


class MuvDriveStrategy(DriveStrategy):
    def drive(self):
        print("MUV car is driving")


class Vehicle:
    def __init__(self, drive_strategy: DriveStrategy):
        self.drive_strategy = drive_strategy

    def drive(self):
        self.drive_strategy.drive()


if __name__ == "__main__":
    passenger_vehicle = Vehicle(drive_strategy=PassengerCarDriveStrategy())
    passenger_vehicle.drive()

    sports_vehicle = Vehicle(drive_strategy=SportsDriveStrategy())
    sports_vehicle.drive()