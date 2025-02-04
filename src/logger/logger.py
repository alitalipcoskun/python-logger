import logging
import os
from datetime import datetime
from src.exceptions import InvalidRelationException, InvalidNameTypeException
from typing import Union
from ._utils import verify_name, normalize_level, create_log_directory


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
        
        
        CustomLogger.__verify_relation_level(level)
        self.__name = verify_name(name)
            
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
        # Err: this function removes the features of logging. Try to avoid it in implementation, otherwise remove it.
        
        level = normalize_level(level)
        
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
        
        level = normalize_level(level)
        CustomLogger.__verify_relation_level(level)
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(CustomLogger.RELATIONS[level])
        console_handler.setFormatter(cls.log_formatter())
        
        return console_handler
    
    @staticmethod
    def verify_relation_level(
            level: str
    ):
        
        relation_keys = list(CustomLogger.RELATIONS.keys())
        level = normalize_level(level)
        
        if level not in relation_keys:
            raise InvalidRelationException(relation=level)
    
    @classmethod
    def __initialize_file_handler(
            cls,
            log_directory: str,
            level: str="debug"
    ):
        
        level = normalize_level(level)
        CustomLogger.__verify_relation_level(level)
        
        log_filename = os.path.join(log_directory, f"{cls.get_current_date()}.log")
        create_log_directory(log_directory)
        
        file_handler = logging.FileHandler(log_filename)
        file_handler.setLevel(CustomLogger.RELATIONS[level])
        file_handler.setFormatter(cls.log_formatter())
        
        return file_handler
    
    
    @staticmethod
    def __verify_relation_level(
            level: str
    ):
        
        relation_keys = list(CustomLogger.RELATIONS.keys())
        level = normalize_level(level)
        
        if level not in relation_keys:
            raise InvalidRelationException(relation=level)
    
    