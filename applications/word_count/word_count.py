import re
def word_count(s):
    # Your code here
    counts = {}
    remove_count = 0
    original_string = s
    characters_remove = ['"', ':', ';', ',', '.', '-', '+', '=', '/',  '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
  
  # print(re.sub("|".join(characters_remove), "", original_string))
    for char in characters_remove: 
        new_string = original_string.replace(char, '')
        if len(original_string) != len(new_string):
            remove_count += 1

        original_string = new_string


    if remove_count == 0:
      return counts
    words = original_string.lower().split()

  

    for word in words:
      if word in counts: 
        counts[word] += 1
      else: 
        counts[word] = 1

    return counts


if __name__ == "__main__":
    print(word_count('+*-*-*-*-[}]{"'))
    print(word_count("Hello+"))
    print(word_count("Hello    hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))