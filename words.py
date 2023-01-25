import optparse

opts = optparse.OptionParser()

opts.add_option("-f", "--file", dest='fname', help="This is the file name that you would like to read")
opts.add_option("-w", "--word", dest='word', help="This is the word that you would like to search")

(options, arguments) = opts.parse_args()
print(options.fname)
print(options.word)

# Open file
file = open(options.fname, 'r')
# Save word in a Dict with count
counts = dict()

for line in file:
    words = line.split()
    for word in words:
 	    counts[word] = counts.get(word, 0) + 1


print("The word: {} appears {} times in {} file".format(options.word, counts.get(options.word), options.fname))
