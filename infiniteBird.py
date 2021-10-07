import pygame
import time
import random 
from pydub import AudioSegment
import glob

audioVol=0.3
audioPath="./audio/birds"
musicPath="./audio/music"
audioFiles = sorted(glob.glob(audioPath+"/*mp3_*.wav"))
musicFiles = sorted(glob.glob(musicPath+"/*.wav"))
randomMax=3
randomLoopsMax=3
bandfilterRange=3000
lowPassFilterFreqHz=bandfilterRange-1000
highPassFilterFreqHz=bandfilterRange+1000

pygame.mixer.init()
pygame.init()

pygame.mixer.set_num_channels(len(audioFiles) +1)
mixerList=[]
for audioFile in audioFiles:
    print("Loading: " + audioFile)
    sound=pygame.mixer.Sound(AudioSegment.from_wav(audioFile).low_pass_filter(lowPassFilterFreqHz).high_pass_filter(highPassFilterFreqHz).raw_data)
    sound.set_volume(audioVol)
    mixerList.append(sound)

mcnt=1
for musicFile in musicFiles:
    print("queueing music file: " + musicFile)
    if mcnt == 1:
      pygame.mixer.music.load(musicFile)
    else:
      pygame.mixer.music.queue(musicFile)
      mcnt += 1

i = 1
while True:
  print("sound played: " + str(i) + " - total samples loaded: " + str(len(mixerList)))
  rnd = random.choice(mixerList)
  rnd.play(loops = random.randint(0,randomLoopsMax)) 
  time.sleep (random.randint(0,randomMax))
  if not pygame.mixer.music.get_busy():
    pygame.mixer.music.play(loops=-1)
  i += 1
