import webbrowser
import random

with open("hentai.txt","r") as f:
    urls = f.readlines()

new=2

url= random.choice(urls)
webbrowser.open(url,new= new);
