import abc


class AbstractHouseBuilder(abc.ABC):
    @abc.abstractmethod
    def set_building_type(self, building_type):
        """set building type"""

    @abc.abstractmethod
    def set_wall_material(self, wall_material):
        """set wall material"""

    @abc.abstractmethod
    def set_number_of_doors(self, number):
        """set number of doors"""

    @abc.abstractmethod
    def set_number_of_windows(self, number):
        """set number of windows"""

    @abc.abstractmethod
    def get_result(self):
        """return the final product"""
