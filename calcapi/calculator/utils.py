import math
from rest_framework.exceptions import APIException, ValidationError


def calculator(operator, a, b):
    result = None
    try:
        if operator == "add":
            result = a + b
        elif operator == "sub":
            result = a - b
        elif operator == "mul":
            result = a * b
        elif operator == "div":
            result = a / b
        else:
            raise ValueError("Enter only add/sub/mul/div!")
    except Exception as ex:
        raise APIException("Calc Error : " + str(ex))
    return result