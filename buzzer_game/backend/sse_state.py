from dataclasses import dataclass
from models import Team

from enum import Enum, auto


class State(Enum):
    QUESTION_ASKED = auto()


@dataclass
class SSSEState:
    players: list[Team]
    active_player: Team
