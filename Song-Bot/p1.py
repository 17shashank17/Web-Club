f=open('songs.txt','r')
content=f.read().split('||')
j=0
song=[]
for i in content:
    song.append(content[j].split(':'))
    j+=1
j=0
print(song)