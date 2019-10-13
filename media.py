"""Defines the Movie class that contains the details of a movie."""
import webbrowser
class movie():
    """This class provides a way to store movie related information.
    Attributes:
        title: A string to store the title of the movie.
        storyline: A string to store the basic plot of the movie.
        poster_image_url: A string to store the URL of the movie poster.
        trailer_youtube_url: A string to store the URL of the movie trailer.
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """Initialises Movie class instance variables."""
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube

    def show_trailer(self):
        """Plays the movie trailer in the web browser."""
        webbrowser.open(self.trailer_youtube_url)
