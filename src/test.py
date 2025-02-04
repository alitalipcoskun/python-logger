from .logger import CustomLogger

name = __name__
class TestClass:
    def __init__(self):
        
        self.__logger = CustomLogger(name="test.py")
        self.__logger.logger.info("Class initialized")
        
        