import random

verbs = ["Leverage", "Sync", "Target", "Gamify"]
adjectives = ["A/B Testing", "Freemium", "Hyperlocal", "Siloed"]
nouns = ["Early Adopter", "Low-hanging fruit", "Pipeline", "Splash page", "Productivity"]

verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)

phrase = verb + " " + adjective + " " + noun

print(phrase)

dog_name = input("What is your dog's name?")
dog_age = int(input("What is your dog's age?"))
print("Your dog", dog_name, "is", dog_age, "years old in human years")
human_age = dog_age * 7
print(human_age)

random_choice = random.randint(0, 10)
print("computer chooses: ", random_choice)