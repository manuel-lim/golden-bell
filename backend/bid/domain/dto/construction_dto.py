from typing import Optional
from dataclasses import dataclass
from backend.bid.domain.construction import Construction


@dataclass
class ConstructionDTO(Construction):
    tmp_nm: Optional[str] = None
    rsrvtn_prce_rng_bgn_rate: Optional[str] = None
    rsrvtn_prce_rng_end_rate: Optional[str] = None
