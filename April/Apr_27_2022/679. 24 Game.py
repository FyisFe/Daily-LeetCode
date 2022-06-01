class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        if len(cards) == 1:
            return math.isclose(cards[0], 24)

        for _ in range(len(cards)):
            a = cards.pop(0)  # fetch first card
            for _ in range(len(cards)):
                b = cards.pop(0)  # fetch second card
                for value in [
                    a + b,
                    a - b,
                    a * b,
                    b and a / b,
                ]:  # calculate these two cards
                    cards.append(value)  # save value
                    if self.judgePoint24(cards):
                        return True
                    cards.pop()  # clear value
                cards.append(b)  # put second card back
            cards.append(a)  # put first card back
        return False
