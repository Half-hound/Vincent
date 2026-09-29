# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 

def counting_vowels_and_consonants(paragraph):
    vow=0
    con=0
    for i in paragraph.lower():
        if i.isalpha()==True:
            if i in "aeiou":
                vow = vow+1
            else:
                con = con+1
    return (vow,con)

def average_vowels_and_consonants(paragraph):
    vow=0
    con=0
    sent=""
    sentlst=[]
    numlst=[]
    sumnumvow=0
    sumnumcon=0
    for i in paragraph:
        if i not in ".!":
           sent=sent+i
        else:
            sentlst.append(sent)
            sent=""
    for i in sentlst:
        numlst.append(counting_vowels_and_consonants(i))
    for i in numlst:
        sumnumvow=sumnumvow+i[0]
        sumnumcon=sumnumcon+i[1]
    return (len(sentlst),sumnumvow/len(sentlst),sumnumcon/len(sentlst))

print(f"The result of counting_vowels_and_consonants for the paragraph returns {average_vowels_and_consonants(paragraph)[1]} as the average vowels per sentence, and {average_vowels_and_consonants(paragraph)[2]} as average consonants per sentence.")