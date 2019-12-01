from pyjavaproperties import Properties
from source.utilities import globals


class ReadConfig:

    @staticmethod
    def get_properties():
        prop = Properties()
        prop.load(open(globals.PROPERTIES_PATH, mode='r'))
        return prop

    @staticmethod
    def get_url():
        prop = ReadConfig.get_properties()
        return prop.getProperty("URL")

    @staticmethod
    def get_browser():
        prop = ReadConfig.get_properties()
        return prop.getProperty("Browser")

    @staticmethod
    def get_implicit_wait():
        prop = ReadConfig.get_properties()
        return int(prop.getProperty("I_wait"))

    @staticmethod
    def get_explicit_wait():
        prop = ReadConfig.get_properties()
        return int(prop.getProperty("e_wait"))
