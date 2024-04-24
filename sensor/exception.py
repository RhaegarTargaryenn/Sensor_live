# import sys
# import os


# def error_message_details(error , error_details:sys):
#        _,_,exc_tb = error_detail.exc_info()

# filename = exc_tb.tb_frame.f_code.co_filename
# error_message = "error occured and the filename is [{0}] the line number is [{1}] and the error is [{2}],".format( 
# filename,exc_tb.tb_lineno,str(error))
# return error_message


# class SensorException(Exception):

#     def __init__(self,error_message,error_detail:sys):

# super().__init__(error_message)

  
#   self.error_message= error_message_details(error_message,error_detail=error_detail)

#   def __str__(self):
#    return self.error_message


import sys
import os

def error_message_details(error, error_details):
    _, _, exc_tb = error_details.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = "error occurred and the filename is [{0}], the line number is [{1}], and the error is [{2}]".format(
        filename, exc_tb.tb_lineno, str(error))
    return error_message

class SensorException(Exception):
    def __init__(self, error_message, error_details):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_details=error_details)

    def __str__(self):
        return self.error_message


