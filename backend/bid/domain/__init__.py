from dataclasses import dataclass


@dataclass
class Bid:
    def __init__(self, **kwargs):
        self.type_ = kwargs.get("type")
        self.data = dict(kwargs)

    def get_instance(self):
        pass


