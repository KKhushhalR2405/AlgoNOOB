def word_break(input_string, partial, dictionary={}):
    if len(input_string) == 0:
        print(partial)
        return

    for i in range(0, len(input_string)):
        word = input_string[:i+1]
        if word in dictionary:
            partial.append(word)
            word_break(input_string[i+1:], partial, dictionary)
            partial.pop()


dict = {"cats", "cat", "and", "sand", "dogs"}
input_string = "catsanddogs"
word_break(input_string, [], dict)
