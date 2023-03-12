sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above
sentence_list = sentence.split()
result = {word:len(word) for word in sentence_list}
# Write your code below:

print(result)
