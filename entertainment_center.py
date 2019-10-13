"""Stores details of movies and displays them on a website."""
import fresh_tomatoes
import media

def main():
    """Creates six Movie objects, initialising these objects with title, storyline,
    poster image link, youtube video trailer link"""

    Avengers=media.movie("Avengers",
                            "Superhero film based on the Marvel Comics",
                            "https://en.wikipedia.org/wiki/Forrest_Gump#/media/File:Forrest_Gump_poster.jpg",
                            "https://www.youtube.com/watch?v=eOrNdBpGMv8")
    
    Mission_Impossible_Fallout=media.movie("Mission_Impossible_Fallout",
                   "Ethan Hunt, along with his IMF team, sets out to stop a gropu of terrorists who plan nuclear attacks on different cities.",
                   "Mission_Impossible_Fallout.jpg",
                   "https://www.youtube.com/watch?v=wb49-oV0F78")

    Avatar=media.movie("Avatar",
                   "A marine on an alien planet",
                   "Avatar.jpg",
                   "https://www.youtube.com/watch?v=5PSNL1qE6VY")
    
    Dark_Knight=media.movie("Dark Knight",
                              "The Caped Crusader begins to tread a fine line between heroism and vigilantism when a vile young criminal throws the town into chaos",
                              "Dark_Knight.jpg",
                              "https://www.youtube.com/watch?v=EXeTwQWrcwY")
    
    Deadpool=media.movie("Deadpool",
                              "The Caped Crusader begins to tread a fine line between heroism and vigilantism when a vile young criminal throws the town into chaos",
                              "Deadpool.jpg",
                              "https://www.youtube.com/watch?v=FyKWUTwSYAs")

    Incredibles=media.movie("Incredibles",
                      "Forced to adopt a civilian identity and stuck in a white-collar job, Mr Incredible itches to get back into action.",
                      "Incredibles.jpg",
                      "https://www.youtube.com/watch?v=SOKY7XyOHTA")

    Toy_story=media.movie("Toy Story",
                      "The story of Boy and his toys that come to life",
                      "Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")
    

    Shawshank_Redemption=media.movie("Shawshank Redemption",
                             "The story of a falsely convicted prson becoming the most unconventional prisoner",
                             "Shawshank_Redemption.jpg",
                             "https://www.youtube.com/watch?v=6hB3S9bIaco")
    
    Date_And_Switch=media.movie("Date_And_Switch",
                                "Friendship between two best friends tested when one of them reveals he is gay",
                                "Date_And_Switch.jpg",
                                "https://www.youtube.com/watch?v=ggehO3r1hMM")
    
    Playing_It_Cool=media.movie("Playing_It_Cool",
                                "Friendship between two best friends tested when one of them reveals he is gay",
                                "Playing_It_Cool.jpg",
                                "https://www.youtube.com/watch?v=BQnejVZLQ6w")                            
    
    22_Jump_Street=media.movie("22_Jump_Street",
                                " Two undercover cops are sent on a mission to a college to investigate the use of a recreational drug",
                                "22_Jump_Street.jpg",
                                "https://www.youtube.com/watch?v=v9S_dYuq0vE")
                                
    Blockers=media.movie("Blockers",
                                " Two undercover cops are sent on a mission to a college to investigate the use of a recreational drug",
                                "Blockers.jpg",
                                "https://www.youtube.com/watch?v=RfFcaV5O7SU")
    
    Gone_Girl=media.movie("Gone_Girl",
                                     "Woman goes missing",
                                     "Gone_Girl.jpg",
                                     "https://www.youtube.com/watch?v=QZsF7IRTgMQ")

    Fast_And_Furious_6=media.movie("Fast_And_Furious_6",
                                     "Hobbs enlists the help of Dom and his team to catch a global team of mercenary drivers",
                                     "Fast_And_Furious_6.jpg",
                                     "https://www.youtube.com/watch?v=dKi5XoeTN0k")                                
    
    Insidious=media.movie("Insidious",
                                     "a young family discovers that the body of their comatose boy has become a magnet for malevolent entities",
                                     "Insidious.jpg",
                                     "https://www.youtube.com/watch?v=zuZnRUcoWos")

    A_Quiet_Place=media.movie("A_Quiet_Place",
                                     "a young family discovers that the body of their comatose boy has become a magnet for malevolent entities",
                                     "A_Quiet_Place.png",
                                     "https://www.youtube.com/watch?v=p9wE8dyzEJE")    

    the_theory_of_everything=media.movie("Theory of Everything",
                                     "Autobiography of Stephen Hawkings",
                                     "The_Theory_of_Everything.jpg",
                                     "https://www.youtube.com/watch?v=Salz7uGp72c")

    Culture_High=media.movie("Culture_High",
                                     "Autobiography of Stephen Hawkings",
                                     "Culture_High.jpg",
                                     "https://www.youtube.com/watch?v=cGCraLGvUss")
    
    the_man_who_knew_infinity=media.movie("The Man Who Knew Infinity",
                                          "Autobiography of  Srinivasa Ramanujan",
                                          "The_Man_Who_Knew_Infinity.jpg",
                                          "https://www.youtube.com/watch?v=oXGm9Vlfx4w")

    Rampage=media.movie("Rampage",
                           "A sports film, selection of players on limited budget",
                           "Rampage.jpg",
                           "https://www.youtube.com/watch?v=coOKvrsmQiI")

    Jurassic_World=media.movie("Jurassic_World",
                           "A sports film, selection of players on limited budget",
                           "Jurassic_World.jpg",
                           "https://www.youtube.com/watch?v=RFinNxS5KN4")                       

    money_ball=media.movie("Money Ball",
                           "A sports film, selection of players on limited budget",
                           "https://en.wikipedia.org/wiki/Moneyball_(film)#/media/File:Moneyball_Poster.jpg",
                           "https://www.youtube.com/watch?v=-4QPVo0UIzc")
    
    

# Store the Movie objects in a list.
    movies=[Avengers, Mission_Impossible_Fallout, Avatar, Dark_Knight, Deadpool, Incredibles ,Toy_story, Shawshank_Redemption, Date_And_Switch, Playing_It_Cool , 22_Jump_Street, Blockers ,Gone_Girl, Insidious , A_Quiet_Place , the_theory_of_everything, Culture_High, the_man_who_knew_infinity ,money_ball]

# Open the movie website in the user's browser, featuring the movies above.
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
