import media
import fresh_tomatoes


def get_movies():
    m1 = media.Movie("Inception",
    "http://www.impawards.com/2010/posters/inception.jpg",
    "https://www.youtube.com/watch?v=8hP9D6kZseM")

    m2 = media.Movie("Shaun of the dead",
    "http://www.impawards.com/2004/posters/shaun_of_the_dead_ver2_xlg.jpg",
    "https://www.youtube.com/watch?v=LIfcaZ4pC-4")

    m3 = media.Movie("The grand Budapest hotel",
    "http://www.impawards.com/2014/posters/grand_budapest_hotel_ver17.jpg",
    "https://www.youtube.com/watch?v=1Fg5iWmQjwk")

    movies = [m1, m2, m3]

    return movies


def main():
    movies = get_movies()
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))