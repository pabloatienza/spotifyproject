class Track:
    """Track represents a piece of music."""

    def __init__(self, name, id, artist, tempo, acoustic, dance, energy, valence):
        """
        :param name (str): Track name
        :param id (int): Spotify track id
        :param artist (str): Artist who created the track
        """
        self.name = name
        self.id = id
        self.artist = artist
        self.tempo = tempo
        self.acoustic = acoustic
        self.dance = dance
        self.energy = energy
        self.valence = valence

    def create_spotify_uri(self):
        return f"spotify:track:{self.id}"

    def __str__(self):
        return self.name + " by " + self.artist + f' ({round(self.tempo)} bpm)'

class Track2:

    def __init__(self, name, id, artist):
        """
        :param name:
        :param id:
        :param artist:
        """
        self.name = name
        self.id = id
        self.artist = artist

    def create_spotify_uri(self):
        return f"spotify:track:{self.id}"

    def __str__(self):
        return self.name + " by " + self.artist