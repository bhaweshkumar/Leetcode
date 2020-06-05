def output_result(score):
    if score >= 90:
        print("Reading level oof 5th grade")
    elif score >= 80:
        print("Reading level of 6th grade")
    elif score >= 70:
        print("Reading level of 7th grade")
    elif score >= 60:
        print("Reading level of 8-9th grade")
    elif score >= 50:
        print("Reading level of 10-12th grade")
    elif score >= 30:
        print("Reading level of college student")
    else:
        print("Reading level of college graduate")


def count_sentences(text):
    count = 0
    terminals = '.;?!'
    for char in text:
        if char in terminals:
            count += 1
    return count


def count_syllables(words):
    count = 0
    for word in words:
        count = count + count_syllables_in_words(word)
    return count


def count_syllables_in_words(word):
    count = 0
    endings = '.,;!?:'
    last_char = word[-1]

    if last_char in endings:
        processed_word = word[:-1]
    else:
        processed_word = word

    if len(processed_word) <= 3:
        return 1

    if processed_word[-1] in 'eE':
        processed_word = processed_word[:-1]

    vowels = 'aeiouAEIOU'
    prev_char_was_vowel = False

    for char in processed_word:
        if char in vowels:
            if not prev_char_was_vowel:
                count += 1
            prev_char_was_vowel = True
        else:
            prev_char_was_vowel = False

    if processed_word[-1] in 'yY':
        count += 1

    return count


def compute_readability(text):
    total_words = text.split()
    word_count = len(total_words)
    total_sentences = count_sentences(text)
    total_syllables = count_syllables(total_words)
    score = (206.835 - 1.015 * (word_count / total_sentences) - 84.6 * (total_syllables / word_count))

    print("Total words", word_count)
    print("Total sentences", total_sentences)
    print("Total syllables", total_syllables)
    print("Flesch-Kineaid score", score)

    output_result(score)


def get_reading_score():
    text = input("Please enter some text to be scored\n")
    compute_readability(text)


get_reading_score()
