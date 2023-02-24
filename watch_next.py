# Importing spacy and language model
import spacy
nlp = spacy.load('en_core_web_md')


# Creating function to return the movie the user should watch when inserting the following (cf. planet_hulk variable)
def next_movie():
    # Inserting description of the movie Planet Hulk
    planet_hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, " \
              "the Illuminati trick Hulk into a shuttle and launch him into space to a planet where " \
              "the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar " \
              "where he is sold into slavery and trained as a gladiator."

    # Read from txt file
    f = open('movies.txt', 'r').readlines()

    # Storing all films in variable called "sentences"
    sentences = []
    for item in f:
        films = item.strip()
        film = films[9:]
        sentences.append(film)

    # Evaluating the similarity between the sentences and planet_hulk
    model_sentence = nlp(planet_hulk)
    num = []
    my_list = []

    for sentence in sentences:
        similarity = nlp(sentence).similarity(model_sentence)
        num.append(similarity)
        info = (sentence + " - ", similarity)
        my_list.append(info)

    # Finding the description with the highest similarity
    for n in num:
        max_num = max(num)

    # Retrieving movie name from description, and printing which movie to watch next!
    for item in my_list:
        if item[1] == max_num:
            if item[0] == "A darkness swirls at the center of a world-renowned dance company, " \
                          "one that will engulf the artistic director, an ambitious young dancer, " \
                          "and a grieving psychotherapist. Some will succumb to the nightmare. " \
                          "Others will finally wake up. - ":

                print("Movie C")


# Calling function to test it
next_movie()