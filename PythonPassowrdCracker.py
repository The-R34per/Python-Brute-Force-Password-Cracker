import itertools
import time
import string

chars = string.printable.strip()
attempts = 0
password = input("Input the password to crack: ")

start_time = time.perf_counter()

for length in range(1, len(password) + 1):
    for guess_tuple in itertools.product(chars, repeat=length):
        attempts += 1
        guess = ''.join(guess_tuple)
        if guess == password:
            break

end_time = time.perf_counter()  # Fallback for no match
elapsed = end_time - start_time
print("Password was cracked in {:.2f} seconds, with {} attempts.".format(elapsed, attempts))
print(f"Your password was: {guess}")