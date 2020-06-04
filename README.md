# The-Movie-Universe-Project
Which actresses, actors, and movies are linked together?

The idea

  My wife and I like to play a thought-experiment game. The rules are that if an actress (or actor) is in multiple movies then those movies are considered to be in the same universe. By chaining together people and films you can create some very interesting universes.

Examples

  Ian McKellen plays, among other roles, both Gandalf in the Lord of the Rings movies and Magneto in a set of X-men movies between 2000 and 2014.
  In those X-men movies we have Patrick Stewart playing Professor Charles Xavier, and an the LotR movies we have Elijah Wood as Frodo.
  The Patrick Stewart connection allows for Star Trek: The Next Generation and its associated movies and actresses/actors to be included.
  So now we have Lord of the Rings and Star Trek in the same universe.
You can keep going as far as you like. The game can lead to some interesting combinations.


I had a suspicion that if you had a lot of knowledge of films then you'd probably end up with most or all of Hollywood's movies in the same universe. I'm not that great about remembering actors and movies, though, so I worked on putting together a Python script to look it up for me.

This is the script

I started trying to do this in R, but I had trouble with the available web-scraping tools.
I switched over to Python and the Beautifulsoup library for other web-scraping tools that worked better for the project.
Then I discovered that there's an IMDb library with an API that made this project much simpler.

This program is by no means the end of the project. There's plenty more that can be done.
1. I could include, for example, cases wherein a person acted as "self" in the film.
2. Perhaps add a way to omit or include movies or TV shows as desired.
3. Right now the program only goes two levels deep. It should be able to be extended to an arbitrary depth. Perhaps even a way to have it go until the list of people or of movies reaches a threshold or stops adding new items.
4. Is it possible to decide whether an input string is a movie or a person without haveing to ask for a separate input?
