from html.parser import HTMLParser

class ListItemParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.items = []
        self._capture = False

    def handle_starttag(self, tag, attrs):
        if tag == "li":
            self._capture = True

    def handle_endtag(self, tag):
        if tag == "li":
            self._capture = False

    def handle_data(self, data):
        if self._capture:
            text = data.strip()
            if text:
                self.items.append(text)


def extract_data_from_soup(html: str):
    """Extract list item text from HTML string."""
    parser = ListItemParser()
    parser.feed(html)
    return parser.items


def scrape_data_directly(html: str):
    """Parse HTML and return list item text."""
    return extract_data_from_soup(html)
