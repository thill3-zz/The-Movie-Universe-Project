from imdb import IMDb
ia = IMDb()

##############################################################3

def get_people_from_movie(movie_id):
    movie = ia.get_movie(movie_id)
    movie_cast = movie.get('cast')
    people = {}
    for person in movie_cast:
        person_name = person['name']
        person_id = person.personID
        people[person_id] = person_name
    return people


def get_movies_from_person(person_id):
    #Note that only the things in filmography[0] are the acting roles
    #usefully that gives only the show titles and not the episode titles

    #Have to get the filmography part dynamically because it's not always the same
    persons_filmo = ia.get_person(person_id)['filmography']
    for i in range(len(persons_filmo)):
        act_cred = persons_filmo[i]
        if list(act_cred.keys())[0] == 'actor' or list(act_cred.keys())[0] == 'actress':
            ind = i
            break

    try:
        persons_filmo = ia.get_person(person_id)['filmography'][ind]['actor']
    except:
        persons_filmo = ia.get_person(person_id)['filmography'][ind]['actress']
    movies = {}
    for movie in persons_filmo:
        movie_name = movie['title']
        movie_id = movie.movieID
        movies[movie_id] = movie_name
    return movies

###############################################################
#First loop through

ma = input('Movie or Actor/Actress: ')
universe_movies = {}
universe_people = {}

if ma.lower() == 'm':
    movie_name = input('Movie Name: ')
    movies = ia.search_movie(movie_name)

    movie_id = movies[0].movieID
    movie_name = movies[0]['title']

    print('Start movie name and id = ', movie_name, movie_id)
    print('Number of universe people = ', len(get_people_from_movie(movie_id)))

    for k, v in get_people_from_movie(movie_id).items():
        universe_movies.update(get_movies_from_person(k))
        print('Person = ', v, k)
        print('Number of universe movies = ', len(universe_movies))
    #The Matrix gives 1254 movies
    # The Rainmaker gives 1798 movies

elif ma.lower() == 'a':
    person_name = input('Person Name: ')
    people = ia.search_person(person_name)

    person_id = people[0].personID
    person_name = people[0]['name']

    print('Number of universe movies = ', len(get_movies_from_person(person_id)))

    for k, v in get_movies_from_person(person_id).items():
        universe_people.update(get_people_from_movie(k))
        print('Movie = ', v, k)
        print('Number of universe people = ', len(universe_people))
    #Nichelle Nichols gives 2639 people through 68 movies/shows
    #Keanu Reeves gives 3963 people

#############################################################3
