import sys

def error_message_details(error, error_data:sys):
    _, _, exc_tb = error_data.exc_info()
    error_message = "Error occured in file [{0}] at line number [{1}] error message: [{2}]".format(
        exc_tb.tb_frame.f_code.co_filename,
        exc_tb.tb_lineno,
        str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(self.error_message, error_detail)
    
    def __str__(self):
        return self.error_message