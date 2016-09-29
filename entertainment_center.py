import fresh_tomatoes
from media import Movie


def get_movies():
    # Builds the list of movies to generate the site with

    m1 = Movie("Inception",
               "http://www.impawards.com/2010/posters/inception.jpg",
               "https://www.youtube.com/watch?v=8hP9D6kZseM")

    m2 = Movie("Shaun of the dead",
               "http://www.impawards.com/2004/posters/"
               "shaun_of_the_dead_ver2_xlg.jpg",
               "https://www.youtube.com/watch?v=LIfcaZ4pC-4")

    m3 = Movie("The grand Budapest hotel",
               "http://www.impawards.com/2014/posters/"
               "grand_budapest_hotel_ver17.jpg",
               "https://www.youtube.com/watch?v=1Fg5iWmQjwk")

    movies = [m1, m2, m3]
    return movies

# Entry point of the program
if __name__ == '__main__':
    movies = get_movies()
    fresh_tomatoes.open_movies_page(movies)
