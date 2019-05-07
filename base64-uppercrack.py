#!/usr/bin/python3
import base64
raw = 'aGVsbG8gZnJpZW5kIGhvdyBhcmUgeW91IHRvZGF5Cg=='
encoded = raw.upper()

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

print(b64_chunks)

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
b64_combos2 = []
s = ''
index = 0
valid_str = list(' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
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
    b64_combos.insert(index, [chunk, dec_buffer])
    b64_combos2.insert(index, dec_buffer)

print(b64_combos2)




