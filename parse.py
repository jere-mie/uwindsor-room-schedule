import pprint
import re
pp = pprint.PrettyPrinter(indent=4)
with open('F22.txt', 'r') as f:
    text = f.read().split('Section')
    text = [i.replace('\n', '').strip() for i in text]
    text = filter(lambda x: 'synchronous' not in x.lower(), text)
    text = [re.sub(r',\w+', '', i) for i in text]
    text = [re.sub(r' \(-\).+', '', i) for i in text]
    text = [re.sub(r'\d\d\d\d-\d\d-\d\d', '', i) for i in text]
    text = [re.search(r'(M|T|W|TH|F|MW|TTH) (\d\d:\d\d) (AM|PM) (\d\d:\d\d(AM|PM))(BiologyBuilding|Erie Hall|Dillon Hall|Toldo HealthEducationCtr|Chrysler HallSouth|Chrysler HallNorth|OdetteBuilding|LambtonTower|Essex Hall|MemorialHall|HK Building|EducationBuilding|LeddyLibrary|West Library|FreedomWay|JackmanDramatic ArtCntre)[ ]*(B\d+|G\d+|\d+)', i) for i in text]
    text = [i.groups() if i is not None else '' for i in text]
    text = list(filter(lambda x: x != '', text))
    # groups = [i[5] for i in text]


# pp.pprint(text)
# print(text)
for i in text:
    # print(f'|{i}|')
    print(f'{{"day":"{i[0]}", "start":"{i[1]+i[2]}", "end":"{i[3]}", "building":"{i[5]}", "room":"{i[6]}"}},')
    # print('------')
print(len(text))
# for i in groups:
#     print(f'|{i}|\n---')
# ggroups = set(groups)
# for i in ggroups:
#     print(f'|{i}|\n----------')
