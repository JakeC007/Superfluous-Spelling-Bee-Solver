"""
Solves spelling bee
J. Chanenson
11/29/23
"""
from itertools import permutations
import enchant
import math

##TODO: spelling bee requies every word to use the cen ter letter; modify this

def count_permutations(input_letters):
    """
    Calculate and prints the number of permutations for words of length 1 to n.

    Parameters:
    - input_letters (str): The input letters

    Returns:
    - None
    """
    n = len(input_letters)

    permutations_count = []

    for r in range(1, n + 1):
        #Permutations formula P(n, r) = n! / (n-r)!
        permutation = math.factorial(n) // math.factorial(n - r)
        permutations_count.append(permutation)

    for i, count in enumerate(permutations_count, start=1):
        print(f"Number of possible words of length {i}: {count}")
    
    print("-"*10)
    return None

def generate_words(input_letters, n = 0):
    """
    Generate a sorted list of valid English words that can be formed from a given set of letters.

    Parameters:
    - input_letters (str): A string containing the set of letters to generate words from.
    - n (int): Maximum length of words to consider.

    Returns:
    - list: A sorted list of valid English words formed from the input letters, sorted first by string length
      and then by starting letter.
    """
    # If no num entered, change n to max
    if n == 0:
        n = len(input_letters)

    # Load English dictionary
    english_dict = enchant.Dict("en_US")

    sorted_words = []

    # Generate all permutations for lengths 1 to n
    for length in range(1, n+1):
        # Generate all permutations of the input letters for the current length
        all_permutations = [''.join(p) for p in permutations(input_letters, length)]

        # Filter valid English words
        valid_words = [word for word in all_permutations if english_dict.check(word)]

        # Append to the result list
        sorted_sub = sorted(valid_words, key=lambda x: (len(x), x))
        sorted_words.extend(sorted_sub)
        
        print(f"Words of length {length} ({len(sorted_sub)} words): {', '.join(sorted_sub)}")

    return sorted_words

if __name__ == "__main__":
    input_letters = input("Please input chars: ")
    
    if not input_letters.isalpha():
        print("Error: Input contains non-alphabetic characters. Exiting.")
        exit()

    print(f"\nGiven the following letters: {', '.join(list(input_letters))}")
    count_permutations(input_letters)

    result = generate_words(input_letters)
    print(f"\nThere are {len(result)} words")
