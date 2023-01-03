## System obsługujący bibliotekę filmów i seriali
import random
from datetime import date
 
# Klasa 'Movie' do przechowywania informacji na temat filmów znajdujących się w systemie
class Movie:
    # Domyślny konstruktor
    def __init__(self, title, release_date, genre):
        # Powiązanie parametrów z atrybutami
        self.title = title
        self.release_date = release_date
        self.genre = genre
        # Zmienne   
        self.displays = 0
    # Metoda 'play' zwiększająca liczbę odtworzeń danego tytułu o 1
    def play(self, step = 1):
        self.displays += step
    # Metoda '__str__' odpowiadająca za wygląd obiektu klasy 'Movie'
    def __str__(self):
        return f"{self.title} ({self.release_date})"    

# Klasa 'Series' przechowująca informację na temat seriali znajdujących się w systemie i dziedzicząca z klasy 'Movie'        
class Series(Movie):
    # Domyślny konstruktor
    def __init__(self, episode, season, *args, **kwargs):
        # Odwołanie do klasy 'Movie' po której odziedzicza klasa 'Series'
        super().__init__(*args, **kwargs)
        # Powiązanie parametrów z atrybutami
        self.episode = episode
        self.season = season
    # Metoda 'play' zwiększająca liczbę odtworzeń danego tytułu o 1    
    def play(self, step=1):
        return super().play(step)
    # Metoda '__str__' odpowiadająca za wygląd obiektu klasy 'Movie'
    def __str__(self):
        return f"{self.title} S{self.episode}E{self.season}"
#-----------------------------------------------------------------------------------------------------------------------        