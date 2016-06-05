import nltk
from levenshtein.levenshtein_distance import levenshtein_distance, closest_words

def main():
    nltk.download('brown')
    from nltk.corpus import brown

    words = brown.words()
    print(words)

if __name__ == "__main__":
    levenshtein_distance("pezoitai", "paizete", print_tables=True)
    print(closest_words("babis", ["test", "zavarakatranemia", "babis"], 5))
    main()