import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vxyZH85NQC4")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A story of some blue aliens",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=vxyZH85NQC4")

#print(avatar.title)

#toy_story.show_trailer()

inception = media.Movie("Inception",
                       "Dreaming in dreams",
                       "http://t2.gstatic.com/images?q=tbn:ANd9GcRo9vfJCM6dzPkZHIHBVCtlJnAnew9Ai26kEdrli0-tfmatmciD",
                       "https://www.youtube.com/watch?v=YoHD9XEInc0")

#inception.show_trailer()

school_of_rock = media.Movie("School of Rock",
                     "Using rock music to learn",
                     "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                     "https://www.youtube.com/watch?v=vxyZH85NQC4")

ratatoulli = media.Movie("Ratatouille",
                     "A rat is a chef in Paris",
                     "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                     "https://www.youtube.com/watch?v=vxyZH85NQC4")

hunger_games = media.Movie("Hunger Games",
                     "A really real reality show",
                     "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                     "https://www.youtube.com/watch?v=vxyZH85NQC4")
movies = [toy_story, avatar, inception, school_of_rock, ratatoulli, hunger_games]
#fresh_tomatoes.open_movies_page(movies)

# Testing class variable valid_ratings
#print(media.Movie.VALID_RATINGS)
print("media.Movie.__?__")
print("The name of the class is "+media.Movie.__name__)
print("The name of the module is "+media.Movie.__module__)

