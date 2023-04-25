import random
# import random module


def main():
    sentence1 = make_sentence(1, "past")
    sentence2 = make_sentence(2, "past")
    sentence3 = make_sentence(1, "present")
    sentence4 = make_sentence(2, "present")
    sentence5 = make_sentence(1, "future")
    sentence6 = make_sentence(2, "future")
     # print sentences
    print(sentence1)
    print(sentence2)
    print(sentence3)
    print(sentence4)
    print(sentence5)
    print(sentence6)


def get_determiner(quantity):
    # Call the get_determiner function to
    # randomly chosen determiner for words like "the","a","one","some"
    # "many".
    # this function will return either "a","one" or "the"
     """Return a randomly chosen determiner. A determiner is
     a word like "the", "a", "one", "some", "many".
     If quantity is 1, this function will return either "a",
     "one", or "the". Otherwise this function will return
     either "some", "many", or "the".

        Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
     Return: a randomly chosen determiner.
     """
     if quantity == 1:
        words = ["a", "one", "the"]
     else:
        words = ["some", "many", "the"]

     # Randomly choose and return a determiner.
     word = random.choice(words)
     return word


def get_noun(quantity):
    # Call the get_noun function
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
    "bird", "boy", "car", "cat", "child",
    "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
    "birds", "boys", "cars", "cats", "children",
    dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
        the returned noun is single or plural.
        Return: a randomly chosen noun.
        """

    # Use the get_determiner function as an example to write the get_verb function
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
    "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
    "dogs", "girls", "men", "rabbits", "women"]

     # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_verb(quantity, tense):
    # Call the get_verb function
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
    "drank", "ate", "grew", "laughed", "thought",
    "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
    "drinks", "eats", "grows", "laughs", "thinks",
    "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
    "drink", "eat", "grow", "laugh", "think",
    "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
    "will drink", "will eat", "will grow", "will laugh",
    "will think", "will run", "will sleep", "will talk",
    "will walk", "will write"

    Parameters
    quantity: an integer that determines if the
        returned verb is single or plural.
    tense: a string that determines the verb conjugation,
        either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    # Write a function named make_sentence .
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    word = random.choice(words)
    return word


def make_sentence(quantity, tense):
    # call make_sentence functions to make a sentence with random words that
    # are given.
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    sentence = f"{determiner} {noun} {verb}"
    return sentence
        
# Print the results for the user to see.        
# Start this program by
# calling the main function

main()

    
      