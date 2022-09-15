bytes = b'r\xc3\xa9sum\xc3\xa9'

word_decoded = bytes.decode()
print(word_decoded)

latin1_encoded = word_decoded.encode("latin1")
print(latin1_encoded)

latin1_decoded = latin1_encoded.decode("latin1")
print(latin1_decoded)