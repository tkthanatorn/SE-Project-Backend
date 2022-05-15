from db import db

DEFAULT_TAG_COL = ['id', 'name', 'key', 'symbol']


def SelectTags(cond: list = []):
    # Query preparing
    col_query = ','.join(DEFAULT_TAG_COL)
    cond_query = ''.join(cond)
    query = f"select {col_query} from tags {cond_query}"
    print(query)

    # Query
    cur = db.cursor()
    cur.execute(query)
    data = cur.fetchall()

    # Result preprocessing
    result = []
    for item in data:
        tmp = {}
        for ind, col in enumerate(DEFAULT_TAG_COL):
            tmp[col] = item[ind]
        result.append(tmp)

    # close & return
    cur.close()
    return result
