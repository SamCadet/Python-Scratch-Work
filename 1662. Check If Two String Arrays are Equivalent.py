def arrayStringsAreEqual(word1, word2):
    # visualize answer https://tinyurl.com/y5bqkrla

    string1 = ''.join([str(item) for item in word1])
    string2 = ''.join([str(item) for item in word2])
    if string1 == string2:
        return True


word1 = ["issa", "c"]
word2 = ["isaac"]

arrayStringsAreEqual(word1, word2)
