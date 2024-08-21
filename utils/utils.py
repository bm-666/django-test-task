from uuid import UUID



def is_uuid(string: str) -> bool:
    """ проверка что в строке UUID
    param: string входящая строка
    """
    try:
        if isinstance(UUID(string), UUID):
            return True
    except:
        return False
