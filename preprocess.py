curr_line = []
output_file = open("processed_dev.txt", 'w+')



def process(line):
    global curr_line
    words = line.split(" ")
    if words == ['\n']:
        curr_line = curr_line[1:-1]
        sentence = " ".join(curr_line)
        sentence += "\n"
        sentence = sentence.lower()
        output_file.write(sentence)

        curr_line = []

    else:
        curr_line.append(words[0])
        if words[1] != 'O\n':
            curr_line.append(words[1][0:-1])



with open("dev.txt") as infile:
    for line in infile:
        process(line)