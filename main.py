# from sensor.exception import SensorException
# import os
# import sys 


# def test_exception():
#     try:
#         a=1/0
#         except Exceptions as e:
# raise  SensorException(e,sys)

# if __name__ == '__main__':
#     try:
#         test_exception
#     except Exception as e:
#         print("Error while running sensor " + str(e))


import os
import sys
from sensor.exception import SensorException
from sensor.logger import logging

def test_exception():
    try:
        logging.info("kr le pura yae wala shi he project")
        a = 1 / 0
    except Exception as e:
        raise SensorException(e, sys)

if __name__ == '__main__':
    try:
        test_exception()
    except SensorException as e:
        print("Error while running sensor: " + str(e))


