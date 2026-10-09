from arena import Call, RaiseTo


class QueenAgent:
    def act(self, observation, legal_actions):
        # Queen strategy: bet whenever possible; otherwise call.
        if observation.toy_private_card != "Q":
            return legal_actions[0]

        for action in legal_actions:
            if isinstance(action, RaiseTo):
                return action

        for action in legal_actions:
            if isinstance(action, Call):
                return action

        # Safety fallback: always return a legal action.
        return legal_actions[0]


def create_agent():
    return QueenAgent()
