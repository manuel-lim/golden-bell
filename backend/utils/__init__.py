from datetime import datetime

def props(cls):
    return {i: v for i, v in cls.__dict__.items() if i[:1] != '_'}
