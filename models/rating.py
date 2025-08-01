import os 
os.system('cls')

class Rating:

    def __init__(self, client, score):
        self._client = client
        self._score = score

    def __str__(self):
        return f'Rating from {self._client}: Score {self._score}'