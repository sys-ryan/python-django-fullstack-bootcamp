import re

patterns = ['term1', 'term2']
text = 'This is a string with term1, but not the other'

for pattern in patterns:
    print("I'm searching for: " + pattern)

    if re.search(pattern, text):
        print("MATCH")
    else: 
        print("NO MATCH")





match = re.search('term1', text)
print(type(match))
print(match.start())

split_term = '@'
email = 'user@gmail.com'
print(re.split(split_term, email))



print(re.findall('match', 'test phrase match in match middle'))


def multi_re_find(patterns, phrase):
    for pat in patterns: 
        print("Searching for patterns {}".format(pat))
        print(re.findall(pat, phrase))
        print('\n')

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dsssssss...sdddddd'

# test_patterns = ['sd+'] # s followed by zero or more d
# test_patterns = ['sd+'] # s followed by one or more d
# test_patterns = ['sd?'] # s followed by either zero or one d
# test_patterns = ['sd{3}'] # s followed by three ds
test_patterns = ['sd{1,3}'] # s followed by one or three ds
multi_re_find(test_patterns, test_phrase)


test_patterns = ['s[sd]+'] # s followed by one or more  (s or d)
multi_re_find(test_patterns, test_phrase)
 


test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
test_patterns = ['[^!.?]+']
multi_re_find(test_patterns, test_phrase)



test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
test_patterns = ['[a-z]+']
multi_re_find(test_patterns, test_phrase)

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
test_patterns = ['[A-Z]+']
multi_re_find(test_patterns, test_phrase)

test_phrase = 'This is a string witwh numbers 12312 and a symbol #hashtag'
# test_patterns = [r'\d+'] #digits 
# test_patterns = [r'\D+'] #non digits
# test_patterns = [r'\s+'] #space
# test_patterns = [r'\S+'] #non space
# test_patterns = [r'\w+'] #alpha numeric (letters and numbers)
test_patterns = [r'\W+'] #non alpha numeric
multi_re_find(test_patterns, test_phrase)

