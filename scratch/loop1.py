import tkinter.filedialog


def while_version(L):
    i = 0
    total = 0

    while i < len(L) and L[i] % 2 != 0:
        total = total + L[i]
        i = i + 1

    return total

def for_version(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0 and not found_even:
            total = total + num
        else:
            found_even = True
 
    return total

for_version([1,3,5,9,45,2,3,6])


def cap_song_repetition(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.
    '''
    while playlist.count(song) > 3:
        playlist.remove(playlist.index(song))

# NOK
  #  while playlist.count(song) >= 3:
   #     playlist.remove(song)

# OK
#    while playlist.count(song) > 3:
#        playlist.remove(song)

# OK
 #   while playlist.count(song) > 3:
  #      playlist.pop(playlist.index(song))


def increment_items(L, increment):
    i = 0
    while i < len(L):
        L[i] = L[i] + increment
        print (L[i],' ', increment)
        i = i + 1


def count_matches(s1, s2):
    ''' (str, str) -> int
    Return the number of positions in s1 that contain the
    same character at the corresponding position of s2.
    Precondition: len(s1) == len(s2)
    '''
    num_matches = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            num_matches = num_matches + 1

    return num_matches

def mystery(lst):
    for sublist in lst:
        total = 0
        for num in sublist:
            total = total + num
            
    return total


def merge(L):
    merged = []
    for i in range(0, len(L), 3):
        merged.append(L[i] + L[i + 1] + L[i + 2])
    return merged






