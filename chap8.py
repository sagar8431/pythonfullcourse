import random
import string
import time

target_id = "nithin_sr_shettigere"

possible_chars = string.ascii_lowercase + "_"

cracked_id = ""
total_attempts = 0

print("\n--- Cracking Started ---\n")

start_time = time.time()

for i in range(len(target_id)):
    guess = ""
    attempts = 0
    
    while guess != target_id[i]:
        guess = random.choice(possible_chars)
        attempts += 1
        total_attempts += 1
        print(f"Current Progress: {cracked_id}{guess}", end="\r")
    
    cracked_id += guess
    print(f"Found '{guess}' in {attempts} tries")

end_time = time.time()

print("\n\n✅ Success!")
print("Cracked Text:", cracked_id)
print("Total Attempts:", total_attempts)
print("Time Taken:", round(end_time - start_time, 4), "seconds")
