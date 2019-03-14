import webbrowser
from operator import attrgetter


class Movie():

    ''' Defines this class instance variables (for modeling movies) while storing
    pointers to every instance of Movies in a list upon construction. Lastly,
    sorts said list alphabetically.'''

    def __init__(self, title, story, image, trailer, list):
        self.title = title
        self.story = story
        self.image = image
        self.trailer = trailer

        self.sorting(list)

    def sorting(self, list):
        list.append(self)
        list.sort(key=attrgetter('title'))
