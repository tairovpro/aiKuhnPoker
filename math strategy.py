import random


class StrategyMath:
    BASE_BLUFF_RATE = 1 / 3

    def __init__(self):
        self.rng = None
        self.player_id = None
        self.score = 0

    def new_match(self, context):
        self.player_id = context.player_id

        self.rng = random.Random(
            f"{context.seed}:{context.player_id}"
        )

        self.score = 0

    def update_score(self, hand_result):
        self.score += hand_result.payout_for(self.player_id)

    def bluff_probability(self):
        
        probability = self.BASE_BLUFF_RATE

        if self.score >= 3:
            probability += 0.10

        elif self.score <= -3:
            probability -= 0.10

        return max(0.10, min(0.50, probability))

    def should_bluff(self):
        probability = self.bluff_probability()

        return self.rng.random() < probability
