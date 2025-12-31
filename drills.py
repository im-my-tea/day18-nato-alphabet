first = [1, 1, 2, 3, 5, 8, 13]


sq = [x*x for x in first]
print(sq)

ev = [x for x in first if x%2 == 0]
print(ev)

od = [x for x in first if x%2]
print(od)

sentence = "What is the Airspeed Velocity of an Unladen Swallow ?".split()
length = {word: len(word) for word in sentence}
print(length)