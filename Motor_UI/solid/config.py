from typing import List, Optional
from dataclasses import dataclass, field

@dataclass
class UiConfig:
    rpm: List[str] = field(default_factory=lambda: ["100","200","300","400","500"])
    port: Optional[List[str]] = None
    type: List[str] = field(default_factory=lambda: ["L", "W"])
