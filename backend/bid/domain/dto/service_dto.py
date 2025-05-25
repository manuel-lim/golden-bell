from dataclasses import dataclass
from backend.bid.domain.service import Service


@dataclass
class ServiceDTO(Service):
    pass