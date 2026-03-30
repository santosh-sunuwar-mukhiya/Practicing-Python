word_count = {}
try:
    with open("poem.txt", "r") as f:
        # print(f.readline())
        for line in f:
            words = line.split(" ")
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    print(word_count)

    word_occurrence = list(word_count.values())
    max_count = max(word_occurrence)
    print("Max occurrences of any word is:", max_count)

    print("Words with max occurrences are: ")
    for word, count in word_count.items():
        if count == max_count:
            print(word)
except FileNotFoundError:
    print("File was not found.")