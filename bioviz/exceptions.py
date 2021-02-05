
class InvalidColorMapException(Exception):

    def __init__(self, *args):
        if len(args)==1 and isinstance(args[0], str):
            self.message  = args[0]
        else:    
            self.message = "Invalid colormap."

class InvalidFileFormatException(Exception):

    def __init__(self, *args):
        if len(args)==1 and isinstance(args[0], str):
            self.message  = args[0]
        else:   
            self.message = "Invalid fileformat for this type of diagram."