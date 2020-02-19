x = 0

# Read in data just to check we can
# Path relative to root directory doesn't work
# Path relative to this file also doesn't work:
# with open("../data/file.txt", 'r') as f:
with open("data/file.txt", 'r') as f:
    data = f.readlines()

loss = 1 - x

print("loss: {}".format(loss))
