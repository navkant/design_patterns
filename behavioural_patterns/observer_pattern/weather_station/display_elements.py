from behavioural_patterns.observer_pattern.observer_pattern_if import Observer, DisplayElement


class CurrentConditionDisplay(Observer, DisplayElement):
    def __init__(self):
        self.temperature: float = 0
        self.humidity: float = 0
        self.pressure: float = 0

    def update(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print(f"Current conditions: {self.temperature}F degrees {self.humidity} humidity and {self.pressure} pressure")
        print(f"Heat index is {self.temperature}")
