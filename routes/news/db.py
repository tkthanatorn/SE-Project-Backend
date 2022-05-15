from db import db

DEFAULT_NEWS_COLUMNS = ['id', 'title',
                        'description', 'text', 'icon', 'url', 'date']


def SelectNews(cols: list = DEFAULT_NEWS_COLUMNS, cond: list = []):
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
