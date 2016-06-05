def levenshtein_distance(wordA, wordB, deletion_cost=1, insertion_cost=1, replacement_cost=2, print_tables=False):
    table = [[0 for j in range(len(wordB) + 2)] for i in range(len(wordA) + 2)]
    table[0][0] = ''

    for j in range(len(wordB) + 1):
        if(j==0):
            table[0][j+1] = '#'
        else:
            table[0][j+1] = wordB[j-1]
        table[1][j + 1] = j

    for i in range(len(wordA) + 1):
        if(i==0):
            table[i+1][0] = '#'
        else:
            table[i+1][0] = wordA[i-1]
        table[i + 1][1] = i

    for i in range(len(wordA)):
        for j in range(len(wordB)):
            temp_replacement_cost = 2
            if (wordA[i] == wordB[j]):
                temp_replacement_cost = 0
            table[i + 2][j + 2] = min(table[i + 1][j + 2] + deletion_cost, table[i + 2][j + 1] + insertion_cost,
                                      table[i + 1][j + 1] + temp_replacement_cost)

    if(print_tables):
        for i in range(len(wordA) + 2):
            for j in range(len(wordB) + 2):
                print('{0:1}'.format(table[i][j]), end = ' ')
            print()

    return table[len(wordA)+1][len(wordB)+1]

def closest_words(word, vocabulary, max_distance):
    distances = [levenshtein_distance(word, v) for v in vocabulary]
    return [w for i,w in enumerate(vocabulary) if distances[i] < max_distance]