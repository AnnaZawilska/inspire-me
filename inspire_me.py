#takes a seed word, a rough number of words, and creates an inspiration poem based on a pre-trained model
def test_fnc(seed_word = 'the',roughly_number_words=100 ):
    import autocomplete
    reload(autocomplete)
    from random import randint
    import string
    import random

    autocomplete.load()

    #the seed for the poem
    prior_word = seed_word

    #the prose you generate
    poem = prior_word

    for i in range(0,roughly_number_words):
        random_seed = random.choice(string.letters)
        x = randint(0,9)
        if x <= 1:
            poem = poem + '\n'
        else:
            new_prediction=autocomplete.predict(prior_word, random_seed)
            if len(new_prediction)>=1:
                y = randint(0,len(new_prediction)-1)
                new_word = new_prediction[y][0]
                poem = poem + ' ' + new_word

    print "\n\n****Words of inspiration:****\n\n"
    print poem

if __name__ == "__main__":
    
    test_fnc('the',100)
