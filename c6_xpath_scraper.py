from lxml.html import fromstring
from advanced_link_crawler import download

url = 'http://example.webscraping.com/places/default/view/Singapore-203'
html = download(url)

tree = fromstring(html)
area = tree.xpath('//tr[@id="places_area__row"]/td[@class="w2p_fw"]/text()')[0]
print(area)
