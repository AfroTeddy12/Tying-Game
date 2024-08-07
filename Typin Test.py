import time
import random

# List of sentences
sentences = [
    "The quick brown fox jumped over the lazy dog.",
    "J Cole is a rapper.",
    "Practice makes perfect.",
    "Make sure to lock your door at night.",
    "Sprite is the best tasting soda",
    "The slippery slope is so slippery that I slipped down the slope.",
    "Polysocrylic 50, Sleeveless - Cotton 7",
    "This is the last sentence in the code"
]

def typing_test():
    sentence = random.choice(sentences)
    print("Type the sentence as fast as you can:")
    print(sentence)
    print()

    input("Press Enter to start...")

    start_time = time.time()
    user_input = input()
    end_time = time.time()

    time_taken = end_time - start_time

    words_count = len(sentence.split())
    words_typed = len(user_input.split())

    if user_input == sentence:
        wpm = (words_count / time_taken) * 60
        print("Congrats, you finished!")
    else:
        wpm = (words_typed / time_taken) * 60
        print("There are some errors... Try again.")

    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Your typing speed is {wpm:.2f} words per minute")

if __name__ == "__main__":
    while True:
        typing_test()
        continue_input = input(" Type 'end' to terminate the program, or press Enter to continue: ")
        if continue_input.lower() == 'end':
            print("Ending the program... Have a nice day!!")
            break
