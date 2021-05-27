from datetime import datetime


def get_triplets(input_string):
    triplets_1 = []
    triplets_2 = []

    for i in range(0, len(input_string) + 1):
        substring = input_string[i: i + 3]
        while(len(substring) < 3):
            substring += '$'
        #triplet = {
        #    "triplet": substring,
        #    "position": i + 1
        #}
        triplet = substring
        mod_3 = i % 3

        if(mod_3 == 1):
            triplets_1.append(triplet)
        elif(mod_3 == 2):
            triplets_2.append(triplet)


    return triplets_1 + triplets_2


def bucket_sort(triplets, index):
    #buckets = { ''a': ['abr', 'asf']', }
    buckets = {}

    for i in range(len(triplets)):
        t = triplets[i]
        if t[index] in buckets.keys():
            buckets[t[index]].append(t)
        else:
            buckets[t[index]] = []
            buckets[t[index]].append(t)

    sorted_list = []
    for key in sorted(buckets.keys()):
        sorted_list = sorted_list + buckets[key]

    return sorted_list


def encode(sorted_triplets, triplets, zeichenvergleiche):
    encoded_triplets = []
    without_duplicates = list(dict.fromkeys(list(map(lambda x: "".join(x), sorted_triplets))))
    for triplet in list(map(lambda x: "".join(x), triplets)):
        encoded_triplets.append(str(without_duplicates.index(triplet) + 1))
        zeichenvergleiche += 1

    has_duplicates = len(without_duplicates) < len(sorted_triplets)
    return encoded_triplets, has_duplicates, zeichenvergleiche

def divideKS(input, recursion, zeichenvergleiche):
    triplets = get_triplets(input)
    a = bucket_sort(triplets, 2)
    a = bucket_sort(a, 1)
    sorted_triplets = bucket_sort(a, 0)
    #print(sorted_triplets)
    encoded, has_duplicates, zeichenvergleiche = encode(sorted_triplets, triplets, zeichenvergleiche)
    print(len(encoded))
    if has_duplicates:
        encoded, recursion, zeichenvergleiche = divideKS(encoded, recursion + 1, zeichenvergleiche)
    return encoded, recursion, zeichenvergleiche


hound_of_baskerville = open('HoundOfBaskerville.txt', 'r+', encoding='utf-8').read()
s = "abracadabra"
sl = []
sl[:0] = s
encoded, recursion, zeichenverlgeiche = divideKS(hound_of_baskerville, 0, 0)
#encoded, recursion, zeichenverlgeiche = divideKS(sl, 0, 0)

#print('encoded: ', encoded)
print('rekursionen: ', recursion)
print('zeichenverleiche: ', zeichenverlgeiche)