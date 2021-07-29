import re


def build_re_character_class(chars):
    return r'[' + re.sub(r'([\]\\\^\-])', r'\\\1', chars) + r']'


def strip(s, chars=None):
    if chars is None:
        char_cls = r'\s'
    else:
        char_cls = build_re_character_class(chars)
    return re.sub(r'^' + char_cls + r'*(.*?)' + char_cls + r'*$', r'\1', s)

# https://www.reddit.com/r/inventwithpython/comments/3cghi7/automate_the_boring_stuff_chapter_7_practice/csvbhqm/
