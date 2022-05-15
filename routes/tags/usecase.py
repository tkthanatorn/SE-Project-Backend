from .db import SelectTags


def SearchTags(search: str):
    cond = f"where name like '{search}%' or key like '{search}%' or symbol like '{search}%'"
    result = SelectTags(cond)
    return result
