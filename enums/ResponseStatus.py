from enum import StrEnum

class ResponseStatus(StrEnum) :
    SUCCESS = 'success'
    OBJECT_DOES_NOT_EXIST = 'object_not_exist'
    INCORRECT_PARAMETER = 'incorrect_parameter'
