class Media:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Media:", self.name)


class Audio(Media):
    def __init__(self, name, duration):
        Media.__init__(self, name)
        self.duration = duration

    def play_audio(self):
        print("Playing audio for", self.duration, "minutes")


class Video(Media):
    def __init__(self, name, quality):
        Media.__init__(self, name)
        self.quality = quality

    def play_video(self):
        print("Playing video in", self.quality, "quality")


class Multimedia(Audio, Video):
    def __init__(self, name, duration, quality):
        Audio.__init__(self, name, duration)
        Video.__init__(self, name, quality)

    def play_all(self):
        self.show()
        self.play_audio()
        self.play_video()


m = Multimedia("MovieSong", 5, "HD")
m.play_all()
