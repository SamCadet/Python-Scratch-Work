# import webbrowser
import requests
import bs4

# webbrowser.open('http://nba.com')

# res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
# print(type(res))
# print(res.status_code == requests.codes.ok)
# len(res.text)
# print(res.text[:250])

# res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
# res.raise_for_status()


# res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
# try:
#    res.raise_for_status()
# except Exception as exc:
#    print('There was a problem: %s' % (exc))

# res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
# res.raise_for_status()
# play_file = open('Romeo_and_Juliet.txt', 'wb')
# for chunk in res.iter_content(100000):
#     print(play_file.write(chunk))
#
# play_file.close()

# res = requests.get('http://nostarch.com')
# res.raise_for_status()
#
# no_starch_soup = bs4.BeautifulSoup(res.text, 'html5lib')
# print(type(no_starch_soup))
#
# example_file = open('example.html')
# example_soup = bs4.BeautifulSoup(example_file, 'html5lib')
# print(type(example_soup))

example_file = open('example.html')
# example_soup = bs4.BeautifulSoup(example_file.read(), 'html5lib')
# elems = example_soup.select('#author')
# print(type(elems))
# print(len(elems))
# print(type(elems[0]))
# print(elems[0].get_text())
# print(str(elems[0]))
# print(elems[0].attrs)
#
# p_elems = example_soup.select('p')
# print(str(p_elems[0]))
# print(p_elems[0].get_text())
# print(str(p_elems[1]))
# print(p_elems[1].get_text())
# print(str(p_elems[2]))
# print(p_elems[2].get_text())

# soup = bs4.BeautifulSoup(open('example.html'), 'html5lib')
# span_elem = soup.select('span')[0]
# print(str(span_elem))
# print(span_elem.get('id'))
# print(span_elem.get('some_nonexistent_addr') == None)
# print(span_elem.attrs)

soup = bs4.BeautifulSoup(open('example.html'), "html5lib")
span_elem = soup.select('span')[0]
print(str(span_elem))

print(span_elem.get('id'))

print(span_elem.get('some_nonexistent_addr') == None)

print(span_elem.attrs)
