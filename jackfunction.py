from arena import Check, Fold, RaiseTo

LOW_CHIPS = 3
HIGH_CHIPS = 10


def jack_action(card, legal_actions, chips, should_bluff):
    
    if card == "J":
        can_check = any(isinstance(a, Check) for a in legal_actions)
        if chips >= HIGH_CHIPS and can_check and should_bluff():
            for action in legal_actions:
                if isinstance(action, RaiseTo):
                    return action

        
        for action in legal_actions:
            if isinstance(action, (Check, Fold)):
                return action

        return legal_actions[0]

    return None  