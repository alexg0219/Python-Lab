from lxml import etree as ET
xml = ET.parse('movies.xml')
entries_movies = xml.getroot()

def parse_xml_to_json(entries):
  response = {}

  for child in entries:
    if child.tag in response:
      if type(response[child.tag]) == list:
        response[child.tag].append(add_tag(child))
      else:
        response[child.tag] = [response.get(child.tag),add_tag(child)]
    else:
      dict = add_tag(child)
      if child.attrib:
        for i in child.attrib:
          dict[i] = child.attrib[i]
      response[child.tag] = dict

  return response

def add_tag(child):
  dict = {}

  if len(child) > 0:
    dict = parse_xml_to_json(child)
  else:
    dict["text"] = child.text

  return dict

parsed = parse_xml_to_json(entries_movies)
print(parsed)