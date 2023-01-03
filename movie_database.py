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
# # Przykładowe obiekty
moneyball = Movie(title = 'Moneyball', release_date = 'September 9, 2011', genre = 'Drama')
witcher = Series (title = 'The Witcher', release_date = 'December 20, 2019', genre = 'Fantasy', episode = '01', season = '01')
jaws = Movie(title = 'Jaws', release_date = 'June 20, 1975', genre = 'Thriller')
vikings = Series (title = 'Vikings', release_date = 'March 3, 2013', genre = 'Historical', episode = '01', season = '01')
fight_club = Movie(title = 'Fight Club', release_date = 'September 10, 1999', genre = 'Thriller')
billions = Series (title = 'Billions', release_date = 'January 1, 2016', genre = 'Drama', episode = '01', season = '01')
kiler = Movie(title = 'Kiler', release_date = 'November 17, 1997', genre = 'Comedy')
breakingbad = Series (title = 'Breaking Bad', release_date = 'December 6, 2007', genre = 'Criminal', episode = '01', season = '01')
riobravo = Movie(title = 'Rio Bravo', release_date = 'March 18, 1959', genre = 'Western')
chernobyl = Series(title = 'Chernobyl', release_date = 'May 6, 2019', genre = 'Drama', episode = '01', season = '01')
darkknight = Movie(title = 'The Dark Knight', release_date = 'July 14, 2008', genre = 'Action')
lastdance = Series(title = 'The Last Dance', release_date = 'April 10, 2020', genre = 'Documentary', episode = '01', season = '01')
#-----------------------------------------------------------------------------------------------------------------------
# Lista przechowująca filmy i seriale
list = [moneyball, witcher, jaws, vikings, fight_club, billions, kiler, breakingbad, riobravo, chernobyl, darkknight, lastdance]
#-----------------------------------------------------------------------------------------------------------------------
# Funkcja 'get_series' zwraca listę seriali
def get_series():
    print("|Lista seriali|:")
    for i in list:
        if isinstance(i, Series):
            print(str(i))
        else:
            continue
    return print("") 
#-----------------------------------------------------------------------------------------------------------------------
# Funkcja 'get_movie' zwraca listę filmów
def get_movie():
    print("|Lista filmów|:")
    for i in list:
        if isinstance(i, Series):
            continue
        else:
            print(str(i))
    return print("")
#-----------------------------------------------------------------------------------------------------------------------
# Funkcja 'search' wyszukuje film lub serial po jego tytule
def search():
    search_for = input("Proszę wprowadź nazwę szukanego tytułu: " ) # Zmienna przechowująca nazwę szukanego tytułu
    search_for = str(search_for)
    list_length = len(list) # Zmienna przechowująca liczbę tytułów znajdującą się w bibliotece
    n = 1 # Zmienna do inkrementacji
    result = "" # Przechowująca wynik 
    for i in list:
        if i.title == search_for:
            result = result + f"Tytuł {search_for} znajduje się w Bibliotece Filmów, zapraszamy do oglądania :)"
            break
        elif n == list_length:
            result = result + f"Tytuł {search_for} jest niedostępny :/"
            break
        else:
            n = n + 1
    return print(result)
#-----------------------------------------------------------------------------------------------------------------------
# Funkcja 'generate_views', która losowo wybiera element z biblioteki,
# a następnie dodaje mu losową (z zakresu od 1 do 100) ilość odtworzeń.
def generate_views():
    random_title = random.choice(list)
    random_number = random.randrange(1,101)
    random_title.displays += random_number
    return random_title.displays
#-----------------------------------------------------------------------------------------------------------------------
# Funkcja 'multiply_generate_views' uruchamia 'generate_views' 10 razy.
def multiply_generate_views():
    for i in range(1,11):
        generate_views()
    return ''
#-----------------------------------------------------------------------------------------------------------------------
# Funkcja 'top_titles' zwraca wybraną ilość najpopularniejszych tytułów z biblioteki.
def top_titles():
    by_titles = sorted(list, key = lambda _displays : _displays.displays)
    for i in range(0,3):
        print(f"{i+1}. {by_titles[i]}")
    return print('')

if __name__ == '__main__':
    print("|Biblioteka filmów|\n")
    get_movie()
    get_series()
    multiply_generate_views()
    print(f"Najpopularniejsze filmy i seriale dnia {date.today(): %d.%m.%Y}:")
    top_titles()
    search()       