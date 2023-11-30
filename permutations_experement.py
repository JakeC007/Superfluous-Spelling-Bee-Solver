import timeit
from itertools import permutations
import random
import string

def generate_random_string(n):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(n))


def generate_permutations_recursive(input_letters):
    if len(input_letters) == 1:
        return [input_letters]

    result = []
    for i in range(len(input_letters)):
        current_char = input_letters[i]
        remaining_chars = input_letters[:i] + input_letters[i + 1:]
        sub_permutations = generate_permutations_recursive(remaining_chars)

        for perm in sub_permutations:
            result.append(current_char + perm)

    return result


def generate_permutations_for_loop(input_letters):
    def permute(current_str, remaining_letters, result):
        if not remaining_letters:
            result.append(current_str)
            return

        for i in range(len(remaining_letters)):
            next_letter = remaining_letters[i]
            new_current_str = current_str + next_letter
            new_remaining_letters = remaining_letters[:i] + remaining_letters[i+1:]
            permute(new_current_str, new_remaining_letters, result)

    result = []
    permute("", input_letters, result)
    return result


def main():
    length_of_string = 100
    input_letters = generate_random_string(length_of_string)
    print("Starting String Generated!")


    implementations = [
        ("permutations", lambda: [''.join(p) for p in permutations(input_letters)]),
        ("recursive", lambda: generate_permutations_recursive(input_letters)),
        ("for loop", lambda: generate_permutations_for_loop(input_letters))
    ]

    results = {}

    for name, implementation in implementations:
        start_time = timeit.default_timer()
        result = implementation()
        end_time = timeit.default_timer()
        elapsed_time = end_time - start_time

        results[name] = {"time": elapsed_time, "result": result}

    # Pretty print results
    for name, info in results.items():
        print(f"{name.capitalize()} Implementation | Time: {info['time']:.6f} seconds")
        # print(f"Result: {info['result']}\n")

if __name__ == "__main__":
    main()
