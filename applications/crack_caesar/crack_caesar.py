# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

import string

chars = []


with open("ciphertext.txt", "r") as f:
    for c in f.read():
        chars.append(c)


num_chars = len(chars)

cipher = ''.join([str(elem) for elem in chars])

def decoded(s):
    tally = {}
    s = s.upper()
    freq_letters = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

    decode_cypher = {}
    for character in s:
        # if not char.isspace():
        # if char != " ":
        if character >= 'A' and character <= 'Z':
            if character not in tally:
                tally[character] = 1
            else:
                tally[character] += 1
    # print(sorted(tally.items(), key=lambda x: x[1], reverse=True))
    # sorted gives back a new function
    # sort works in place
    tally_list = list(tally.items())
    tally_list.sort(key=lambda x: x[1], reverse=True)
    print(tally_list)
    count = 0
    for pair in tally_list:
        decode_cypher[pair[0]] = freq_letters[count]
        count += 1

        
    decoded_string = ""
    for character in s:
        if character not in decode_cypher:
            decoded_string += character
        else:
        # for each character, look up its mapping
            unscrambled_character = decode_cypher[character]
        # build our return string
            decoded_string += unscrambled_character
    return decoded_string

print(decoded(cipher))



