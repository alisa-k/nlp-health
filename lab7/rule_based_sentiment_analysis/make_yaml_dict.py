with open("senti_data/negative-words.txt", "r") as f:
    negative_lines = [line.rstrip('\n') + ": [negative]\n" for line in f]
with open("senti_data/positive-words.txt", "r") as f:
    positive_lines = [line.rstrip('\n') + ": [positive]\n" for line in f]

with open("senti_data/negative-words.yml", "w") as f: 
    f.writelines(negative_lines)
with open("senti_data/positive-words.yml", "w") as f: 
    f.writelines(positive_lines)