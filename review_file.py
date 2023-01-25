import optparse

opts = optparse.OptionParser()

opts.add_option("-f", "--file", dest='fname', help="This is the file name that you would like to read")
opts.add_option("-i", "--interface", dest='iface', help="This is the inteface that you would like to search")

(options, arguments) = opts.parse_args()
print("*** Using *** ", options.fname, " File***")
print("***Searching for *** ", options.iface, " Interface***")

# Open file
file = open(options.fname, 'r')

data = None
save_line = None

for line in file:
    words = line.split("=")
    if options.iface in words[1]:
        data = words[0].strip()
        save_line = line
        break
file.close()

# Print index
print("Have index: ", data[len(data) - 1])

iface_prefix = data[0:19]
iface_index = data[len(data) - 1]

lines = []
file = open(options.fname, 'r')

for line in file:
    words = line.split("=")
    prefix = words[0].strip()[0:19]
    sufix = words[0].strip()[len(words[0].strip()) - 1]
    if(prefix == iface_prefix and sufix == iface_index):
        lines.append(line)

# print(lines)
for line in lines:
    print(line)
