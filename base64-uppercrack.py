#!/usr/bin/python3
import time
import base64
#raw = 'aGVsbG8gZnJpZW5kIGhvdyBhcmUgeW91IHRvZGF5Cg=='
raw = 'aGVsbG8gZnJpZW5kIGhvdyBhcmUgeW91IHRvZGF5IGFyZSB5b3UgcmVhZHkgdG8gc29sdmUgdGhpcyBwcm9ibGVtIHRoYXQgaXMgaGFyDOG='
encoded = raw.upper()
valid_str = list(' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

# pad b64 to valid length
while len(encoded) % 4 != 0:
    encoded += '='

# generate b64 chunks of len 4
b64_chunks = []
for a in range(0,len(encoded),4):
    try:
        b64_chunks.append(encoded[a:a+4])
    except:
        pass

#print(b64_chunks)

# generate binary matrix
bin = [True, False]
combo_matrix = [(a,b,c,d) for a in bin for b in bin for c in bin for d in bin]


# create matrix of possible decoded values
# generates b64_combos list matrix 
#           
#         b64 chunk    possible decoded values
#             |            |
#            \./          \./ 
#       [
#         [ 'AGVS', ['heR', 'hel'] ],
#         [ 'BG8G', ['lo ', 'lo '] ],
#         [ 'ZNJP', ['frO', 'fri'] ],
#         [ 'ZW5K', ['enJ', 'end', 'enJ', 'end'] ],
#         [ 'IGHV', [' hU', ' ho'] ]
#       ]

b64_combos = []
corpus = []
s = ''
index = 0
for chunk in b64_chunks.copy():
    dec_buffer = []
    for combo in combo_matrix:
        for i in range(0,4):
            if combo[i]:
                s += chunk[i].upper()
            else:
                s += chunk[i].lower()
        flag = True
        try:
            dec = base64.standard_b64decode(s).decode("utf-8")
            for char in dec:
                if char not in valid_str:
                    flag = False
            # dedupe dec_buffer before adding it to b64_combos matrix
            if flag and dec not in dec_buffer:
                #  print("Base64 Chunk: {} Decoded Chunk: {}".format(s, dec))
                dec_buffer.append(dec)

        except:
            pass
        s = ''
    index += 1
    if dec_buffer != []:
        b64_combos.insert(index, [chunk, dec_buffer])
        corpus.insert(index, dec_buffer)

#print(corpus)

#  pools = [tuple(pool) for pool in corpus]
#  result = [[]]
#  for pool in pools:
    #  result = [x+[y] for x in result for y in pool]
#  for prod in result:
    #  ret = ''
    #  for val in prod:
        #  ret += val
#
    #  time.sleep(.01)
    #  print("\r{}".format(ret), end="" )


output = ''
for options in corpus:
    print(output,)
    try:
        if len(options) <= 1:
            output += options[0]
        else:
            for i in range(len(options)):
                print("{}) {}".format(i+1, options[i]))
            answer = input('> ')
            output += options[int(answer)-1]
    except: 
        break

