
from gtts import gTTS
from pygame import mixer
import pygame

f=open('songs.txt','r')
content=f.read().split('||')
j=0
song_listen=[]
for i in content:
    song_listen.append(content[j].split(':'))
    j+=1

print("Press 0 to exit")
while True:

    song="Enter the song you want to listen"
    speech = gTTS(song)
    speech.save('test.mp3')
    
    mixer.init()
    mixer.music.load('test.mp3')
    mixer.music.play()
    p=input()
    p='\n'+p
    j=0
    song_lyrics=""
    for i in song_listen:
        if i[0]==p:
            song_lyrics=gTTS(i[1])
            break
    #mixer.music.unload()
    song_lyrics.save('lyrics.mp3')
    mixer.music.load('lyrics.mp3')
    mixer.music.play()
    while mixer.music.get_busy():
        pygame.time.Clock().tick(30000)

