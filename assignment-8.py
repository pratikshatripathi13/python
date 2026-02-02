class School:
    def __init__(self, name):
        self.name = name

    def show_school(self):
        print("School:", self.name)


class SportsStudent(School):
    def __init__(self, name, sport):
        School.__init__(self, name)
        self.sport = sport

    def play_sport(self):
        print("Plays", self.sport)


class MusicStudent(School):
    def __init__(self, name, instrument):
        School.__init__(self, name)
        self.instrument = instrument

    def play_music(self):
        print("Plays", self.instrument)


class AllRounder(SportsStudent, MusicStudent):
    def __init__(self, name, sport, instrument):
        SportsStudent.__init__(self, name, sport)
        MusicStudent.__init__(self, name, instrument)

    def perform(self):
        self.show_school()
        self.play_sport()
        self.play_music()


a = AllRounder("Green Valley", "Football", "Guitar")
a.perform()
