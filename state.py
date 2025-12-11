from collections.abc import Callable

class State:
    def __init__(self, name, condition: Callable[[], bool], action: Callable):
        self.name = name
        self.condition = condition
        self.action = action

    def __repr__(self):
        return f'State({self.name})'

def check_state(state):
    if not state.condition():
        raise AssertionError(f'Unexpected state, expected {state.name}')

