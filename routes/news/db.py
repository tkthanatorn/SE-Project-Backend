from db import db

DEFAULT_NEWS_COL = ['id', 'title',
                    'description', 'icon', 'url', 'sentiment', 'polarity', 'date']


def SelectNews(cols: list = DEFAULT_NEWS_COL, cond: list = []):
    # Query preparing
    cols_query = ','.join(cols)
    cond_query = ' '.join(cond)
    query = f"select {cols_query} from news {cond_query};"

    # Query
    cur = db.cursor()
    cur.execute(query)
    data = cur.fetchall()

    # Result preprocessing
    result = []
    for item in data:
        tmp = {}
        for ind, col in enumerate(cols):
            if type(item[ind]) == str:
                tmp[col] = str(item[ind]).strip()
            else:
                tmp[col] = item[ind]
        result.append(tmp)

    # close & return
    cur.close()
    return result


def GetNewsByTagsID(tags_id: int, cond: list = []):
    col_query = ','.join([f"n.{item}" for item in DEFAULT_NEWS_COL])
    cond_query = ' '.join(cond)
    query = f"select {col_query} from news as n join news_tags as nt on n.id = nt.news_id join tags as t on t.id=nt.tags_id where t.id={tags_id} {cond_query};"

    cur = db.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()

    result = []
    for item in data:
        tmp = {}
        for ind, col in enumerate(DEFAULT_NEWS_COL):
            if type(item[ind]) == str:
                tmp[col] = str(item[ind]).strip()
            else:
                tmp[col] = item[ind]
        result.append(tmp)

    return result
