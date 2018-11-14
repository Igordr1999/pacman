import pygame


class Music(object):
    sounds_path = "../resrc/sounds/"
    pygame.mixer.init()
    sounds = {
        'bg': [1, "bg.wav"],
        'am': [2, "angry_mode.wav"],
        'go': [3, "gameover.wav"],
        'en': [4, "energizer.wav"],
        'se': [5, "seed_eaten.wav"]}

    for s in sounds:
        sounds[s][1] = pygame.mixer.Sound(sounds_path + sounds[s][1])

    @staticmethod
    def play(title, volume=1):
        # type: (str, float) -> None
        """title:
        'bg': background
        'go': gameover
        'an': anrgy mode
        'en': energiser
        'se': seed eaten
        """
        sound = Music.sounds.get(title, ())
        pygame.mixer.Channel(sound[0]).play(sound[1], 0)
        sound[1].set_volume(volume)

    @staticmethod
    def stop(title):
        sound = Music.sounds.get(title, ())
        pygame.mixer.Channel(sound[0]).stop()
