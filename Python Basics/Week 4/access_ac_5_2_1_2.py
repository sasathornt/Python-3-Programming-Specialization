##For each string in wrds, add ‘ed’ to the end of the word (to make the word past tense). Save these past tense words to a list called past_wrds.

wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds = []
for word in wrds:
    word = word + "ed"
    past_wrds.append(word)