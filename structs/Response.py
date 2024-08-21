from enums.ResponseStatus import ResponseStatus
from typing import Any

class BaseResponse:
    msg: ResponseStatus
    data: Any
    def __init__(self, msg: ResponseStatus, data: Any = None) -> None:
        self.msg = msg
        if data is not None:
            self.data = data
