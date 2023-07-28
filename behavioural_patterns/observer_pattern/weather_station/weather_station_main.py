import sys
sys.path.append("/Users/navkant/Documents/navkant/design_patterns")

from behavioural_patterns.observer_pattern.weather_station.weather_data import WeatherData
from behavioural_patterns.observer_pattern.weather_station.display_elements import CurrentConditionDisplay


class WeatherStation:
    def main(self):
        weather_data: WeatherData = WeatherData()
        current_condition_display: CurrentConditionDisplay = CurrentConditionDisplay()
        weather_data.register_observer(current_condition_display)

        weather_data.set_measurements(80, 65, "30.4f")
        weather_data.set_measurements(82, 70, "29.4f")
        weather_data.set_measurements(78, 90, "31.4f")


if __name__ == "__main__":
    weather_station = WeatherStation()
    weather_station.main()
