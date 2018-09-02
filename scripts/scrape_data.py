from bs4 import BeautifulSoup
from bs4.element import NavigableString
import json
import requests


def scrape_data(spell_id):
    soup = BeautifulSoup(requests.get('https://www.dnd-spells.com/spell/{}'.format(spell_id), timeout=0.5).text)
    attrs = {}
    p_tags = soup.findAll('p')
    attrs['name'] = soup.find('h1').find('span').text
    attrs['school'] = p_tags[1].text

    text = ''
    for i in p_tags[2].children:
        if isinstance(i, NavigableString):
            text += str(i)
        else:
            text += i.text
    for i in [i.strip() for i in text.strip().split('\n')]:
        k, v = i.split(':')
        v = v.strip()
        attrs[k.lower()] = v.strip()

    attrs['desc'] = p_tags[4].text.strip() # Test on spell
    first_h4 = soup.find('h4')
    if first_h4.text.strip().startswith('At higher level'):
        attrs['higher_level_desc'] = first_h4.findNext('p').text.strip()

    for tag in p_tags:
        t = tag.text.strip()
        if t.startswith('Page:'):
            attrs['page'] = t
        if t.startswith('A\n'):
            attrs['classes'] = [i[:-1].strip() for i in t.split('\n')[1:-1]]
    return attrs

# I am error-prone! :O
spells = []
for i in range(413, 466):
    print('\r{}/{}'.format(i, 465), end='')
    spells.append(scrape_data(i))
print()

with open('dnd_spells.json', 'w') as f:
    json.dump(spells, f)