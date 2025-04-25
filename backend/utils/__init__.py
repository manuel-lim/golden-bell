from datetime import datetime

def is_builtin_instance(obj):
    return type(obj).__module__ == 'builtins'

def props(cls):
    return {i: v for i, v in cls.__dict__.items() if i[:1] != '_'}


