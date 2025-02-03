
class InvalidRelationException(Exception):
    """
    The exception occurs when the entered relation is not available
    on the log relations.

    Args:
        Exception (str): The exception that is incorrect.
    """
    def __init__(self,
                 relation: str,
                 msg="The entered relation is invalid, check the entered relation"):
        
        self.relation = relation
        self.msg = msg
        
        super().__init__(self.msg)
        
        
    def __str__(self): 
        
        return f"{self.relation} -> {self.msg}"

    

class InvalidNameTypeException(Exception):
    
    
    def __init__(self,
                 name,
                 msg="The entered name type is invalid. It must be string."):
        
        self.name_type = type(name)
        self.name = name
        self.msg = msg
        
        super().__init__(self.msg)

    
    def __str__(self):
        
        return f"Type({self.name_type}) {self.name} -> {self.msg}"
        