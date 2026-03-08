from RatingSystem import RatingSystem

class OurSystem(RatingSystem):
    """
    Nasz system
    """
    def __init__(self):
        super().__init__()
    def rate(self, user, movie):
        return 2.5
    def __str__(self):
        return 'Maciej Szukało - Kacper Paluch'
