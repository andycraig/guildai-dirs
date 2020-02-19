x = 0

# Read in data just to check we can
with open("data/file.txt", 'r') as f:
    data = f.readlines()

loss = 1 - x

print("loss: {}".format(loss))
