# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def get_word(self):
        return self._word
    
    def set_word(self, word):
        self._word = word

    def match(self, list):
        anagram_list = []
        for i in range(len(list)):
            if sorted([letter for letter in self.word]) == sorted([letter for letter in list[i]]):
                anagram_list.append(list[i])
        return anagram_list
    word = property(get_word, set_word)


listen = Anagram("listen")
listen.match(['enlists', 'google', 'inlets', 'banana'])