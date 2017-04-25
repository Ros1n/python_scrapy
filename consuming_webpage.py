from html.parser import HTMLParser
from collections import defaultdict

class myHTMLParse(HTMLParser):
    def __init__(self):
        super().__init__() #not get what this used for, if lost may have trouble with rawdata feed
        self.h3 = False
        self.li = False
        self.span1 = False
        self.span2 = False
        self.p = False
        self.time = False
        self.a = False
        self.event_collections = {}
        self.count = 0


    def handle_sth(self, tag, attrs=None): #this method cannot been used in both start and end, will cause problem with 'site'
        #if not attrs:
        #    attrs['a'] = 'b'
        if tag == 'li':
            self.li = not self.li
        elif tag == 'h3':
            if attrs:
                for k, v in attrs:
                    if k == 'class' and v == 'event-title':
                        self.h3 = not self.h3
        elif tag == 'a':
            self.a = not self.a
        elif tag == 'p':
            self.p = not self.p
        elif tag == 'time':
            self.time = not self.time
        elif tag == 'span':
            if attrs:
                for k, v in attrs:
                    if k == 'class' and v == 'say-no-more':
                        self.span1 = not self.span1
                    elif k == 'class' and v == 'event-location':
                        self.span2 = not self.span2


    def handle_starttag(self, tag, attrs):
        #self.handle_sth(tag, attrs)
        if tag == 'li':
            self.li = True
        elif tag == 'h3':
            for k, v in attrs:
                if k == 'class' and v == 'event-title':
                    self.h3 = True
        elif tag == 'a':
            self.a = True
        elif tag == 'p':
            self.p = True
        elif tag == 'time':
            self.time = True
        elif tag == 'span':
            for k, v in attrs:
                if k == 'class' and v == 'say-no-more':
                    self.span1 = True
                elif k == 'class' and v == 'event-location':
                    self.span2 = True

    def handle_data(self, data): #consuming JSON value data
        if self.li:
            if self.h3 and self.a:
                self.count += 1
                self.event_collections[self.count] = {}  #defaultdict(list)
                self.event_collections[self.count]['name'] = data
            elif self.p:
                if self.time:
                    if not self.span1:
                        self.event_collections[self.count]['time'] = data
                    else:
                        self.event_collections[self.count]['time'] += (',' + data)
                else:
                    if self.span2:
                        self.event_collections[self.count]['site'] = data

    def handle_endtag(self, tag):
        #self.handle_sth(tag)
        if tag == 'a':
            self.a = False
        elif tag == 'h3':
            self.h3 = False
        elif tag == 'span':
            self.span1 = False
            self.span2 = False
        elif tag == 'time':
            self.time = False
        elif tag == 'p':
            self.p = False
        elif tag == 'li':
            self.li = False

#class myHTMLParse close here

parser = myHTMLParse()

def parse_python_event(html_data):
    global parser
    parser = myHTMLParse()
    parser.feed(html_data)
    return parser.event_collections

if __name__ == '__main__':
    html_data = ''
    with open('Our Events _ Python.org.html', 'r', encoding='utf-8') as page:
        for line in page:
            html_data += line
    event = parse_python_event(html_data)
    print('conference: %s' % event)
    for i in range(1, parser.count+1):
        print(event[i]['name'], '\n', event[i]['time'], '\t', event[i]['site'])