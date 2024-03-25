import requests

def readFile():
    file = open('list.txt', 'r')
    linhas = file.readlines()
    findUrlget(linhas)


def findUrlget(linhas):
    for url in linhas:
        r = requests.get(url)
        print(r.url,'-', r.status_code, end='\n')


readFile()
