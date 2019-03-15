import media
import fresh_tomatoes

#    This module creates the objects required to populate a list and this
# operation happens in the media.py file. Lastly, said list goes as an
# argument for open_movies_pages() function, in fresh_tomatoes.py file,
# generating the webpage.

movies_list = []

toy_story = media.Movie(
                'Toy Story',
                'The secret life of a boy\'s toys.',
                'https://upload.wikimedia.org/wikipedia/pt/d/dc/'
                'Movie_poster_toy_story.jpg',
                'https://www.youtube.com/watch?v=KYz2wyBy3kc',
                movies_list)

avatar = media.Movie(
                'Avatar',
                'A marine in an alien world.',
                'https://upload.wikimedia.org/wikipedia/pt/b/b0/'
                'Avatar-Teaser-Poster.jpg',
                'https://www.youtube.com/watch?v=6ziBFh3V1aM',
                movies_list)

school_of_rock = media.Movie(
                'School of Rock',
                'Fake teacher transform a class attitude.',
                'https://upload.wikimedia.org/wikipedia/en/1/11/'
                'School_of_Rock_Poster.jpg',
                'https://www.youtube.com/watch?v=XCwy6lW5Ixc',
                movies_list)

kings_speech = media.Movie(
                'The King\'s Speech',
                'A story of King George VI, who suffered with stammering.',
                'https://i.etsystatic.com/6849517/r/il/2834d9/327672898/'
                'il_fullxfull.327672898.jpg',
                'https://www.youtube.com/watch?v=EcxBrTvLbBM',
                movies_list)

beautiful_mind = media.Movie(
                'A Beautiful Mind',
                'The life of John Nash, mathematician.',
                'https://upload.wikimedia.org/wikipedia/en/thumb/b/b8/A_Beau'
                'tiful_Mind_Poster.jpg/220px-A_Beautiful_Mind_Poster.jpg',
                'https://www.youtube.com/watch?v=9wZM7CQY130',
                movies_list)

free_solo = media.Movie(
                'Free Solo',
                'Alex Honold\'s Free Rider ascent free solo'
                ' in El Cap\'n.',
                'https://upload.wikimedia.org/wikipedia/pt/4/43/'
                'Free_Solo_2018.png',
                'https://www.youtube.com/watch?v=urRVZ4SW7WU',
                movies_list)

fresh_tomatoes.open_movies_page(movies_list)
