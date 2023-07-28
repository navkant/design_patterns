from typing import List
from behavioural_patterns.observer_pattern.observer_pattern_if import Subject, Observer


class WeatherData(Subject):
    def __init__(self):
        self.observers: List[Observer] = []
        self.temperature: float = 0
        self.humidity: float = 0
        self.pressure: str = ""

    def register_observer(self, observer: "Observer"):
        self.observers.append(observer)

    def remove_observer(self, observer: "Observer"):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurement_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature: float, humidity: float, pressure: str):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurement_changed()
