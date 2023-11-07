import requests
from PIL import Image
import string, random
import urllib
import json
import httplib2



combinations=list(map(str,input().split(' ')))

#list - создает массив
#list(map(str,input().split(' '))) - создает массив комбинаций
num=len(combinations)

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(
    pool_connections=100,
    pool_maxsize=1000)
session.mount('http://', adapter)

numman=0
numend=0
for i in range(num*3):
    f = open("num.txt", "r")
    numintxt = int(f.read())
    
    #создает массив из елемента в combinations разделяя его
    if (i%3==0 and i!=0):
        numman=numman+1
    subject=list(combinations[numman].split('-'))
    man=subject[0]
    
    #print(len(imgurl))
    if (num+i==19):
        numend=1
    else:
        numend=num+i
    rand = random.choice(string.ascii_letters)
    state= True
    if (i%2==0):
        state=False
    res = session.get("https://pixabay.com/api/?key=23542651-cf1b5845142b8014201d20cc9&q=" + man+"&image_type=photo&pretty="+str(state)+"&total=20")
    finall = res.json()
    imgurl=finall['hits']

    imgurl=imgurl[numend]['webformatURL']
    h = httplib2.Http('.cache')
    response, content = h.request(imgurl)


    fw = open("num.txt", "w")

    imglocal="image/"+str(numintxt)+".jpg"
    out = open(imglocal, 'wb')
    num2=numintxt+1
    fw.write(str(num2))
    f.close()
    fw.close()
    out.write(content)
    out.close()
    img = Image.open(imglocal)
    img.show()


#len(combinations) - считает колличество елементов
for i in range(num):
    #цикл
    subject=list(combinations[i].split('-'))
    #создает массив из елемента в combinations разделяя его
    man=subject[0]
    adjective=subject[1]
    secondqu=subject[2]
    #присвоивает словам
    for j in range(num):
        subject=list(combinations[j].split('-'))
        #изменяет содержимое массива subject
        adjective=subject[1]
        for e in range(num):
            subject=list(combinations[e].split('-'))
            secondqu=subject[2]
            #изменяет содержимое
            print(man+'-'+adjective+"-"+secondqu)
            #выводит всё в одну строку
            
           
