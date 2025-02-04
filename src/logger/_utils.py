from src.exceptions.log_exceptions import InvalidNameTypeException, InvalidRelationException
import os

def verify_name(
            name
):
        
        if name is None:
            return __name__
        
        if not isinstance(name, str) or name == "":
            raise InvalidNameTypeException(name)
        
        return name
    
def normalize_level(
        level: str
) -> str:
        return level.lower()

def create_log_directory(
        log_directory: str
) -> None:
        
        """
        The function checks whether the entered log_directory exist or not, if it does not exist, it creates it.

        Args:
            log_directory (str): The directory that should be 
        """
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)
    
