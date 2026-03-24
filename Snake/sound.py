import winsound

# Sonido al comer
def sound_eat():
    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS | winsound.SND_ASYNC)

# Sonido al morir
def sound_die():
    winsound.PlaySound("SystemHand", winsound.SND_ALIAS | winsound.SND_ASYNC)