from dataclasses import dataclass

from enum import Enum, auto


class State(Enum):
    QUESTION_ASKED = auto()
    QUESTION_ANSWERED = auto()
    ANSWER_WRONG = auto()
    ANSWER_CORRECT = auto()


@dataclass
class SSSEState:
    state: State
    active_team_id: int
