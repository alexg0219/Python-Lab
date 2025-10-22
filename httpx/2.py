import httpx
import re
from lxml import etree as ET,html

def find_links(queue,second_l, path,from_links_in_title):
    link = queue.pop(0)
    r = httpx.get(link)
    tree = html.fromstring(r.text)
    entries_title = tree.xpath("//div[@class='mw-body']")[0]
    entries_title = entries_title.xpath("//a[@title]")
    base_url = "https://ru.wikipedia.org"

    for href in entries_title:
        if href.attrib["title"] not in path:
            if re.match("^/wiki/", href.values()[0]):
                print(href.attrib["title"],href.values()[0])
                from_links_in_title[base_url+href.values()[0]] = href.attrib["title"]
                path[href.attrib["title"]] = from_links_in_title[link]
                if href.attrib["title"] == second_l:
                    path[base_url+"/wiki/"+second_l] = link
                    return True
                queue.append(base_url+href.values()[0])

def find(first_link,second_link):
    queue = [first_link]
    second_l = second_link.split("https://ru.wikipedia.org/wiki/")[1]
    first_l = first_link.split("https://ru.wikipedia.org/wiki/")[1]
    path = {first_l : ""}
    from_links_in_title = {first_link : first_l}
    while len(queue):
        if find_links(queue, second_l, path,from_links_in_title):
            result = []
            word = second_l
            c = 0
            while word != "":
                c += 1
                result.append(word)
                word = path[word]
            result = list(reversed(result))

            print("Количество переходов - " + str(len(result)),"Ссылки:")
            for i in result:
                print("https://ru.wikipedia.org/wiki/"+i)
            return
            #return result



d = find("https://ru.wikipedia.org/wiki/Философия","https://ru.wikipedia.org/wiki/Математика")