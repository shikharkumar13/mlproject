import sys
import logging
import logger

def error_message_detail(error, error_detail:sys):
    file_name = exc_tb.tb_frame.f_code.co_filename
    _,_,exc_tb = error_detail.exc_info()
    error_message = 'Error occured in Python Script name [{0}] line number [{1}] and error is [{2}]'.format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message

    def __str__(self):
        return self.error_message
    