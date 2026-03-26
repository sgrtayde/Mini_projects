import time
import random


sentences = [
            "Python is a great programming language.", 
            "I love coding in Python.",
            "Python is widely used in data science.",
            "The Python community is very supportive."
             ]

def measury_acuracy(original, user_input):
    original_words = original.split()
    user_words = user_input.split()
    correct_words = sum(1 for o, u in zip(original_words, user_words) if o == u)
    return correct_words / len(original_words) * 100

def typing_test():
    sentence = random.choice(sentences)
    print("Type the following sentence:")
    print(sentence)
    
    input("Press Enter when you're ready...")
    start_time = time.time() #measure the start typing
    user_input = input()
    end_time = time.time() #measure the end typing
    time_taken = end_time - start_time
    words_count = len(sentence.split())

    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Time taken in minutes: {time_taken / 60:.2f} minutes")
    print(f"Words typed: {words_count}")
    print(f"Speed: {words_count / time_taken * 60:.2f} words per minute")
    accuracy = measury_acuracy(sentence, user_input)
    print(f"Accuracy: {accuracy:.2f}%")
    

typing_test()


