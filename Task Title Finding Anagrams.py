# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

print("**This task was done according to the Anagram concept and examples in https://en.wikipedia.org/wiki/Anagram, article recommended on the LMS**")
print("It could be no case sensitive, with upper/lower functions, but according to a mentor recommendation I decided not to do that")


def find_anagram(word, anagram):
    # [assignment] Add your code here
    
    
    # including sentences or word(s) with spaces before and after them
    stripped_word = word.strip()
    stripped_anagram = anagram.strip()
    
    
    # including sentences or word(s) with spaces within them
    replaced_word = stripped_word.replace(" ", "")
    replaced_anagram = stripped_anagram.replace(" ", "")
    
    
    if len(replaced_word) == len(replaced_anagram):
        if sorted(replaced_word) == sorted(replaced_anagram):
            return True
        return False
    return False

