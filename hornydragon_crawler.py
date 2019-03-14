from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import os


def urls(urlss):
    url = urlss
    response = urlopen(url)
    html = BeautifulSoup(response)

    hdjpg = html.find_all("img", border="0")

    name = url.split("/")

    dir = 'hornydragon/'

    if not os.path.exists(dir):
                os.mkdir(dir)

    dir = 'hornydragon/' + name[3] + name[4] + '_' + name[5].split('.')[0] + '/'

    if not os.path.exists(dir):
                os.mkdir(dir)

    for j in hdjpg[8:]:
        print(j['src'])
        # print(j['src'].split("/")[-2] + '_' + j['src'].split("/")[-1])
        fname = dir + j['src'].split("/")[-2] + '_' + j['src'].split("/")[-1]
        print(fname)
        urlretrieve(j['src'], fname)

