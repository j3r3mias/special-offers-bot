#!/usr/bin/python
# -*- coding: utf-8 -*-

import pickle, random, requests, telepot, time
import os.path
from TOKEN import *
from bs4 import *

config = {"botKey":KEY,
        "idChat":ID,
        "url":"http://www.hardmob.com.br/promocoes/"}

bot = telepot.Bot(config['botKey'])
chat = config['idChat']

def loadDatabase():
    global database
    try:
        with open(databaseFile) as f:
            database = pickle.load(f)
    except:
        database = []

def saveData():
    global databaseFile
    global database
    with open(databaseFile, 'wb') as f:
        pickle.dump(database, f)

def loadUA():
    uas = []
    with open("user-agents.txt", 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[0:-1-0])
    random.shuffle(uas)
    return uas

def checkUpdates():
    ua = random.choice(loadUA())
    req = requests.get(config['url'], headers={'User-Agent': ua})
    soup = BeautifulSoup(req.content, 'html.parser')

    promotions = soup.findAll('a', {'class':'title'})

    for p in promotions:
        msg = p.string.encode('UTF-8').upper()
        if msg in database:
            None
        else:
            database.append(msg)
            link = p['href'].encode('UTF-8')
            bot.sendMessage(chat, msg)
            bot.sendMessage(chat, link)
            saveData()
    
if __name__ == '__main__':
    global databaseFile
    global database
    databaseFile = '.database.dat'
    loadDatabase()
    while True:
        checkUpdates()
        time.sleep(60)  # Sleep in seconds
