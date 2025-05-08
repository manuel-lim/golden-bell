from sqlalchemy import inspect

def row_to_dict(row) -> dict:
    return dict(row._mapping)
