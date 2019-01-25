import sys
from urllib.request import urlopen

# URL example http://sixty-north.com/c/t.txt


def fetch_words(url):
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words

def find_prime_factors(n):
    i = 2
    while n > 1:
        while n % i == 0:
            yield i
            n //= i
        i += 1

def print_items(items):
    for item in items:
        print(item)


def main():
    url = sys.argv[1]
    words = fetch_words(url)
    print_items(words)


if __name__== '__main__':
    fetch_words(url)

