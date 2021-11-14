output_file = open("py_dev.txt", 'w+')
output_file.write("sentence,emoji\n")

with open("processed_dev.txt") as infile:
    for line in infile:
        line = line.strip()
        words = line.split(" ")
        emoji = []
        non_emoji = []
        for a in words:
            if len(a)>3 and a[0] == ':' and a[-1] == ':':
                emoji.append(a)
            else:
                non_emoji.append(a)
        output_file.write("\"")
        output_file.write(" ".join(non_emoji))
        output_file.write("\",")
        output_file.write(emoji[0])
        output_file.write("\n")

output_file.close()