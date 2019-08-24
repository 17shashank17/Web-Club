from gtts import gTTS

speech=gTTS('Hello! Which song you want to listen?')
speech.save('test.mp3')

f=open('songs.txt','r')
content=f.read().split('||')
j=0
song=[]
for i in content:
    song.append(content[j].split(':'))
    j+=1
print(song)