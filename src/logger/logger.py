import logging
import os
from datetime import datetime
from src.exceptions.log_exceptions import InvalidRelationException, InvalidNameTypeException
from typing import Dict, Union
__author__ = "alitalipcoskun"

class CustomLogger(object):
    RELATIONS = {
                        "debug": logging.DEBUG,
                        "info": logging.INFO,
                        "warning": logging.WARNING,
                        "error": logging.ERROR,
                        "critical": logging.CRITICAL
    }
    DATE_FORMAT='%m_%d_%Y_%H_%M_%S'
    
    LOG_FORMAT = '%(asctime)s - %(name)s - [%(lineno)d]- %(levelname)s  - %(message)s'
    
    def __init__(
        self,         
        level:str="debug",
        name: Union[str, None]= None, # After python 3.10, it is used with '|'
    ):
        
        
        self.__verify_relation_level(level)
        self.__name = self.__verify_name(name)
            
        # Initializing logger
        self.__logger = logging.getLogger(self.__name) # Getting the module name
        self.__logger.setLevel(CustomLogger.RELATIONS[level]) # Setting level as debug by default or given attribute
        
        # Handler initialization
        ch = self.__initialize_console_handler()
        fh = self.__initialize_file_handler(log_directory="logs")

        # Adding handlers
        self.__logger.addHandler(ch)
        self.__logger.addHandler(fh)
        
    
    __doc__ = {
        ""
    }
    
    @property
    def logger(
        self
    ):
        return self.__logger
    
    
    @property
    def date_format(
        self
    ):
        return self.__date_format
    
    @classmethod
    def get_current_date(
            cls
    ) -> str:
        """
        It returns the date of the function execution.
        
        The default format is month-day-year-hour-minute-second.
        
        Returns:
            str: String formatted date 
        """
        
        return f"{datetime.now().strftime(cls.DATE_FORMAT)}"
    
    @classmethod
    def log_formatter(
        cls
    ):
        return logging.Formatter(cls.LOG_FORMAT)
    
    
    def log(
            self,
            message: str,
            level: str = "debug"
    ) -> None:
        """
        The method is created to use custom logger. It allows message and level to be seen in log file.

        Args:
            message (str): The message that will be parsed into the log file
            level (str, optional): 
            
            It is mandatory to enter the level value as lower case letters, 
            and the given value should be one of the followings: 
            
            ["debug", "info", "warning", "critical", "error"].
            
            Defaults to "debug".
        """
        # TO-DO: Refactor this function
        
        level = self.__normalize_level(level)
        
        if level == "debug":
            self.logger.debug(message)
        elif level == "info":
            self.__logger.info(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "critical":
            self.logger.critical(message)
        elif level == "error":
            self.logger.error(message)
        else:
            raise InvalidRelationException(relation=level)
    
    
    @classmethod
    def __initialize_console_handler(
            cls,
            level:str = "debug"
    ):
        """
        It initializes the console logger.

        Returns:
            StreamHandler: to log on console
        """
        
        level = CustomLogger.__normalize_level(level)
        CustomLogger.__verify_relation_level(level)
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(CustomLogger.RELATIONS[level])
        console_handler.setFormatter(cls.log_formatter())
        
        return console_handler
    
    @classmethod
    def __initialize_file_handler(
            cls,
            log_directory: str,
            level: str="debug"
    ):
        
        level = CustomLogger.__normalize_level(level)
        CustomLogger.__verify_relation_level(level)
        
        log_filename = os.path.join(log_directory, f"{cls.get_current_date()}.log")
        CustomLogger.__create_log_directory(log_directory)
        
        file_handler = logging.FileHandler(log_filename)
        file_handler.setLevel(CustomLogger.RELATIONS[level])
        file_handler.setFormatter(cls.log_formatter())
        
        return file_handler
    
    
    @staticmethod
    def __verify_name(
            name
    ):
        
        if name is None:
            return __name__
        
        if not isinstance(name, str) or name == "":
            raise InvalidNameTypeException(name)
        
        return name
    
    
    @staticmethod
    def __verify_relation_level(
            level: str
    ):
        
        relation_keys = list(CustomLogger.RELATIONS.keys())
        level = CustomLogger.__normalize_level(level)
        
        if level not in relation_keys:
            raise InvalidRelationException(relation=level)
    
    
    @staticmethod
    def __create_log_directory(
        log_directory: str
    ) -> None:
        
        """
        The function checks whether the entered log_directory exist or not, if it does not exist, it creates it.

        Args:
            log_directory (str): The directory that should be 
        """
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)
            
    @staticmethod
    def __normalize_level(
        level: str
    ) -> str:
        return level.lower()
    
