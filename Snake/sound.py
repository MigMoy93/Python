try:
    import winsound

    # Sonido al comer
    def sound_eat():
        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS | winsound.SND_ASYNC)
            
    # Sonido al morir
    def sound_die():
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS | winsound.SND_ASYNC)

except ImportError:
    def sound_eat():  # existe pero no hace nada
        pass
    def sound_die():  
        pass
