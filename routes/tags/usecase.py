from .db import SelectTags, GetTagsByNewsID


def SearchTags(search: str, limit: int = 5):
    search = f"where name like '{search}%' or key like '{search}%' or symbol like '{search}%'"
    result = SelectTags([search, f"limit {limit}"])
    return result


def GetTagsByNewsID(news_id: int):
    return GetTagsByNewsID(news_id)
