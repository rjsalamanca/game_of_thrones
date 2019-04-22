from characters import characters
from houses import houses
# print(characters[0])
# print(characters[0]['name'])

# jon_snow = {"url":"https://anapioficeandfire.com/api/characters/583","name":"Jon Snow","gender":"Male","culture":"Northmen","born":"In 283 AC","died":"","titles":["Lord Commander of the Night's Watch"],"aliases":["Lord Snow","Ned Stark's Bastard","The Snow of Winterfell","The Crow-Come-Over","The 998th Lord Commander of the Night's Watch","The Bastard of Winterfell","The Black Bastard of the Wall","Lord Crow"],"father":"","mother":"","spouse":"","allegiances":["https://anapioficeandfire.com/api/houses/362"],"books":["https://anapioficeandfire.com/api/books/5"],"povBooks":["https://anapioficeandfire.com/api/books/1","https://anapioficeandfire.com/api/books/2","https://anapioficeandfire.com/api/books/3","https://anapioficeandfire.com/api/books/8"],"tvSeries":["Season 1","Season 2","Season 3","Season 4","Season 5","Season 6"],"playedBy":["Kit Harington"]}

# # print out the key names individually
# # for k in jon_snow:
# #     print(k)

# # print out just the values
# # for k in jon_snow:
# #     print(jon_snow[k])

# # print both the key and the value
# for k in jon_snow:
#     print("%s: %s" % (k, jon_snow[k]))

count_names_a = 0
count_names_z = 0
count_dead = 0
most_titles_count = 0
valyrian_count = 0
hot_pie = ''
not_tv = 0
targaryen = []
house_histogram = {}

for key in houses:
    house_histogram[houses[key]] = 0

for i in range(len(characters)):
    if characters[i]['name'][0] == 'A':
        count_names_a += 1
    elif characters[i]['name'][0] == 'Z':
        count_names_z += 1
    
    if(characters[i]['died'] != ''):
        count_dead += 1

    if(len(characters[i]['titles']) > most_titles_count):
        most_titles_count =  len(characters[i]['titles'])
        most_titles_winner = characters[i]['name']

    if(characters[i]['culture'] == 'Valyrian'):
        valyrian_count += 1

    if(characters[i]['name'] == 'Hot Pie'):
        hot_pie = characters[i]['playedBy']

    if(characters[i]['playedBy'][0] == ''):
        not_tv += 1

    if(characters[i]['name'].find('Targaryen') != -1):
        targaryen.append(characters[i]['name'])

    #if(characters[i]['allegiances'] == houses[characters[i]['allegiances']]):
    #print(houses[characters[i]['allegiances']])
    if(len(characters[i]['allegiances']) > 0):
        if(characters[i]['allegiances'][0] in houses):
            house_histogram[houses[characters[i]['allegiances'][0]]] += 1

# How many characters names start with "A"?
print(count_names_a)

# How many characters names start with "Z"?
print(count_names_z)

# How many characters are dead?
print(count_dead)

# Who has the most titles?
print(most_titles_winner)

# How many are Valyrian?
print(valyrian_count)

# What actor plays "Hot Pie" (and don't use IMDB)?
print(''.join(hot_pie))

# How many characters are *not* in the tv show?
print(not_tv)

# Produce a list characters with the last name "Targaryen"
print(targaryen)

# Create a histogram of the houses (it's the "allegiances" key)
for key in house_histogram:
    print(key, '-', house_histogram[key])