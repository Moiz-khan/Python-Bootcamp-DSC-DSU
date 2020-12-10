
import time

def print_lyrics(song):
    song_list = song.split(',')
    
    for lyrics in song_list:
        time.sleep(1)
        print(lyrics)    

#song contain 10 lyrics of song
song = "One thing I don't know why,It doesn't even matter how hard you try,Keep that in mind, I designed this rhyme,To explain in due time,All I know,Time is a valuable thing,Watch it fly by as the pendulum swings,Watch it count down to the end of the day,The clock ticks life away"

print_lyrics(song)