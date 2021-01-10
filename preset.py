class Preset:
    """Preset represents a customization preset."""

    def __init__(self, name, bpmtarget, bpmmin=0.0, bpmmax=2000.0, acmin=0.0, acmax=1.0, dancemin=0.0, dancemax=1.0,
                 energymin=0.0, energymax=1.0, valenmin=0.0, valenmax=1.0):

        """
        :param name: Preset name
        :param bpmtarget: Tempo target value (Tracks with the attribute values nearest
            to the target values will be preferred.)
        :param bpmmin: Tempo lower limit
        :param bpmmax: Tempo upper limit
        :param acmin: Acousticness lower limit
        :param acmax: Acousticness upper limit
        :param dancemin: Danceability lower limit
        :param dancemax: Danceability upper limit
        :param energymin: Energy lower limit
        :param energymax: Energy upper limit
        :param valenmin: Valence (musical positiveness) lower limit
        :param valenmax: Valence (musical positiveness) upper limit
        """

        self.name = name
        self.bpmtarget = bpmtarget
        self.bpmmin = bpmmin
        self.bpmmax = bpmmax
        self.acmin = acmin
        self.acmax = acmax
        self.dancemin = dancemin
        self.dancemax = dancemax
        self.energymin = energymin
        self.energymax = energymax
        self.valenmin = valenmin
        self.valenmax = valenmax

    def __str__(self):
        return f"Preset: {self.name}"

######################

#JOGGING PRESET
jogging = Preset('Jogging', 120, bpmmin=115, bpmmax=130, dancemin=0.6, energymin=0.6)

#RUNNING PRESET
running = Preset('Running', 140, bpmmin=135, bpmmax=150, dancemin=0.6, energymin=0.7)

#SPRINTING PRESET
sprinting = Preset('Sprinting', 160, bpmmin=150, dancemin=0.6, energymin=0.75, valenmax=0.55)

#CHILL ACOUSTIC PRESET
chill_acoustic = Preset('Chill Acoustic', 180, acmin=0.65, valenmin=0.45)

#RELAX PRESET
relax = Preset('Relax', 60, bpmmin=50, bpmmax=80, energymax=0.4)

#DEEP RELAX PRESET
deep_relax = Preset('Deep Relax', 60, bpmmin=50, bpmmax=65, energymax=0.3)

#GOOD MOOD
good_mood = Preset('Good Mood', 120, dancemin=0.6, energymin=0.6, valenmin=0.6)

presets = [jogging, running, sprinting, chill_acoustic, relax, deep_relax, good_mood]

def presets_list():
    index=0
    for preset in presets:
        index+=1
        print(f'{index} - {preset.__str__()}')
    #index+=1
    #print(f'{index} - Custom (Advanced)')
