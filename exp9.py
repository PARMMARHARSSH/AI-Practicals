class MovieRecommendationSystem:
    def __init__(self):
        self.movies = {
            'The Shawshank Redemption': {'genre': 'Drama', 'rating': 9.3, 'year': 1994, 'cast': ['Tim Robbins', 'Morgan Freeman']},
            'The Godfather': {'genre': 'Crime', 'rating': 9.2, 'year': 1972, 'cast': ['Marlon Brando', 'Al Pacino']},
            'The Dark Knight': {'genre': 'Action', 'rating': 9.0, 'year': 2008, 'cast': ['Christian Bale', 'Heath Ledger']},
            'Pulp Fiction': {'genre': 'Crime', 'rating': 8.9, 'year': 1994, 'cast': ['John Travolta', 'Uma Thurman']},
            'Forrest Gump': {'genre': 'Drama', 'rating': 8.8, 'year': 1994, 'cast': ['Tom Hanks', 'Robin Wright']},
            'Inception': {'genre': 'Sci-Fi', 'rating': 8.8, 'year': 2010, 'cast': ['Leonardo DiCaprio', 'Joseph Gordon-Levitt']},
            'The Matrix': {'genre': 'Action', 'rating': 8.7, 'year': 1999, 'cast': ['Keanu Reeves', 'Laurence Fishburne']},
            'Schindler\'s List': {'genre': 'Biography', 'rating': 8.9, 'year': 1993, 'cast': ['Liam Neeson', 'Ben Kingsley']},
            'The Lord of the Rings: The Return of the King': {'genre': 'Adventure', 'rating': 8.9, 'year': 2003, 'cast': ['Elijah Wood', 'Ian McKellen']},
            'Fight Club': {'genre': 'Drama', 'rating': 8.8, 'year': 1999, 'cast': ['Brad Pitt', 'Edward Norton']},
            'The Godfather: Part II': {'genre': 'Crime', 'rating': 9.0, 'year': 1974, 'cast': ['Al Pacino', 'Robert De Niro']},
            'The Silence of the Lambs': {'genre': 'Thriller', 'rating': 8.6, 'year': 1991, 'cast': ['Jodie Foster', 'Anthony Hopkins']},
            'The Usual Suspects': {'genre': 'Crime', 'rating': 8.5, 'year': 1995, 'cast': ['Kevin Spacey', 'Gabriel Byrne']},
            'Gladiator': {'genre': 'Action', 'rating': 8.5, 'year': 2000, 'cast': ['Russell Crowe', 'Joaquin Phoenix']},
            'Saving Private Ryan': {'genre': 'War', 'rating': 8.6, 'year': 1998, 'cast': ['Tom Hanks', 'Matt Damon']},
            'The Green Mile': {'genre': 'Drama', 'rating': 8.6, 'year': 1999, 'cast': ['Tom Hanks', 'Michael Clarke Duncan']},
            'The Departed': {'genre': 'Crime', 'rating': 8.5, 'year': 2006, 'cast': ['Leonardo DiCaprio', 'Matt Damon']},
            'The Prestige': {'genre': 'Mystery', 'rating': 8.5, 'year': 2006, 'cast': ['Christian Bale', 'Hugh Jackman']},
            'Se7en': {'genre': 'Crime', 'rating': 8.6, 'year': 1995, 'cast': ['Morgan Freeman', 'Brad Pitt']},
            'Goodfellas': {'genre': 'Biography', 'rating': 8.7, 'year': 1990, 'cast': ['Robert De Niro', 'Ray Liotta']},
            'The Lion King': {'genre': 'Animation', 'rating': 8.5, 'year': 1994, 'cast': ['Matthew Broderick', 'Jeremy Irons']},
            'Forrest Gump': {'genre': 'Drama', 'rating': 8.8, 'year': 1994, 'cast': ['Tom Hanks', 'Robin Wright']},
            'The Social Network': {'genre': 'Biography', 'rating': 7.7, 'year': 2010, 'cast': ['Jesse Eisenberg', 'Andrew Garfield']},
            'The Grand Budapest Hotel': {'genre': 'Comedy', 'rating': 8.1, 'year': 2014, 'cast': ['Ralph Fiennes', 'F. Murray Abraham']},
            'Interstellar': {'genre': 'Sci-Fi', 'rating': 8.6, 'year': 2014, 'cast': ['Matthew McConaughey', 'Anne Hathaway']},
            'The Revenant': {'genre': 'Adventure', 'rating': 8.0, 'year': 2015, 'cast': ['Leonardo DiCaprio', 'Tom Hardy']},
            'La La Land': {'genre': 'Musical', 'rating': 8.0, 'year': 2016, 'cast': ['Ryan Gosling', 'Emma Stone']},
            'Black Panther': {'genre': 'Action', 'rating': 7.3, 'year': 2018, 'cast': ['Chadwick Boseman', 'Michael B. Jordan']},
            'Parasite': {'genre': 'Drama', 'rating': 8.6, 'year': 2019, 'cast': ['Kang-ho Song', 'Sun-kyun Lee']}
        }

    def recommend_movies(self):
        print("Welcome to Movie Recommendation System!")
        print("Please provide your preferences:")

        genre = input("Enter your preferred genre: ")
        min_rating = float(input("Enter minimum rating you'd like to watch (0.0 - 10.0): "))
        max_year = int(input("Enter the maximum release year you prefer: "))

        recommended_movies = []
        for movie, info in self.movies.items():
            if info['genre'] == genre and info['rating'] >= min_rating and info['year'] <= max_year:
                recommended_movies.append(movie)

        if recommended_movies:
            print("\nRecommended movies:")
            for movie in recommended_movies:
                print(f"{movie} ({self.movies[movie]['year']})")
                print("  Rating:", self.movies[movie]['rating'])
                print("  Cast:", ', '.join(self.movies[movie]['cast']))
        else:
            print("Sorry, no movies found matching your preferences.")

# Main
if __name__ == "__main__":
    system = MovieRecommendationSystem()
    system.recommend_movies()
