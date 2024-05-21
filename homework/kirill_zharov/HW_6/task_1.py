some_text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero."

punctuation_marks = [":", ".", "!", "?", ",", ";"]

list_words = some_text.split()

new_words = []
for word in list_words:
    if word[-1] in punctuation_marks:
        new_word = word[:-1] + 'ing' + word[-1]
    else:
        new_word = word + 'ing'
    new_words.append(new_word)

new_text = ' '.join(new_words)

print(new_text)
