import logging
import os
from datetime import datetime
from src.exceptions.log_exceptions import InvalidRelationException, InvalidNameTypeException
from typing import Dict, Union
__author__ = "alitalipcoskun"

class CustomLogger(object):
    
    def __init__(self,
                 level:str="debug",
                 date_format: str='%m_%d_%Y_%H_%M_%S',
                 name: Union[str | None]= None,
                 relations: Dict[str]= {
                        "debug": logging.DEBUG,
                        "info": logging.INFO,
                        "warning": logging.WARNING,
                        "error": logging.ERROR,
                        "critical": logging.CRITICAL
                }):
        
        self.__relations = relations
        
        # Format declarations
        self.__date_format = date_format
        self.__formatter = logging.Formatter('%(asctime)s - %(name)s - [%(lineno)d]- %(levelname)s  - %(message)s')
        
        self.__verify_relation_level(level)
        self.__name = self.__verify_name(name)
            
        # Initializing logger
        self.__logger = logging.getLogger(self.__name) # Getting the module name
        self.__logger.setLevel(self.__relations[level]) # Setting level as debug by default or given attribute
        
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
    def logger(self):
        return self.__logger
    
    
    def get_current_date(self) -> str:
        """
        It returns the date of the function execution.
        
        The default format is month-day-year-hour-minute-second.
        
        Returns:
            str: String formatted date 
        """
        
        return f"{datetime.now().strftime(self.__date_format)}"
    
    
    def log(self,
            message: str,
            level: str = "debug") -> None:
        """
        The method is created to use custom logger. It allows message and level to be seen in log file.

        Args:
            message (str): The message that will be parsed into the log file
            level (str, optional): 
            
            It is mandatory to enter the level value as lower case letters, and the given value should be one of the followings: ["debug", "info", "warning", "critical", "error"].
            
            Defaults to "debug".
        """
        
        # Python 3.10 supports match case structure, python 3.9 does not.
        level = self.__normalize_level(level)
        
         # Log the message at the correct level
        if level == "debug":
            self.logger.debug(message)
        elif level == "info":
            self.logger.info(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "critical":
            self.logger.critical(message)
        elif level == "error":
            self.logger.error(message)
        else:
            raise InvalidRelationException(relation=level)
    
    
    def __verify_name(self,
                      name):
        
        if name is None:
            return __name__
        
        if not isinstance(name, str) or name == "":
            raise InvalidNameTypeException(name)
        
        return name
    
    
    def __verify_relation_level(self,
                                level: str):
        
        relation_keys = list(self.__relations.keys())
        level = self.__normalize_level(level)
        
        if level not in relation_keys:
            raise InvalidRelationException(relation=level)
    
    
    def __initialize_console_handler(self,
                                     level:str="debug"):
        """
        It initializes the console logger.

        Returns:
            StreamHandler: to log on console
        """
        
        level = self.__normalize_level(level)
        self.__verify_relation_level(level)
        
        ch = logging.StreamHandler()
        ch.setLevel(self.__relations[level])
        ch.setFormatter(self.__formatter)
        
        return ch
    
    
    def __initialize_file_handler(self,
                                  log_directory: str,
                                  level: str="debug"):
        
        level = self.__normalize_level(level)
        self.__verify_relation_level(level)
        
        log_filename = os.path.join(log_directory, f"{self.get_current_date()}.log")
        self.__create_log_directory(log_directory)
        
        fh = logging.FileHandler(log_filename)
        fh.setLevel(self.__relations[level])
        fh.setFormatter(self.__formatter)
        
        return fh
        
    @staticmethod
    def __create_log_directory(
                                log_directory: str) -> None:
        
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)
            
    @staticmethod
    def __normalize_level(
                          level: str):
        
        return level.lower()
