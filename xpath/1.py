from lxml import etree as ET
tree = ET.parse('movies.xml')
entries_title_runtime = tree.xpath("//Title[@runtime]")

dictionary = {}
#print(entries_title_runtime)
for i in entries_title_runtime:
    if len(i.values()) != 0:
        dictionary[i.text] = i.values()[0]

print(dictionary)
