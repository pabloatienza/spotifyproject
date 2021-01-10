import secretCredentials
#import TokenLogin
#import logintest
#import Login2
import preset

#token = secretCredentials.GetAccessToken()

#print(token)

#logintest.callback()

import os

from spotifyclient import SpotifyClient


def main():
    #token = secretCredentials.GetAccessToken()

    #spotify_client = SpotifyClient(secretCredentials.GetAccessToken(),
    #                               os.getenv("SPOTIFY_USER_ID"))

    spotify_client = SpotifyClient(os.getenv("SPOTIFY_AUTHORIZATION_TOKEN"),
                                   os.getenv("SPOTIFY_USER_ID"))

    # get tracks to choose seeds
    option2 = 0
    while option2 != 1 and option2 != 2 and option2 != 3 and option2 != 4:
        option2 = int(input('Choose option to get list of tracks:\n1. Recently Played\n2. Top Tracks (Recent)\n'\
                            '3. Top Tracks (Medium Term)\n4. Top Tracks (All Time)\n\nSelect: '))

    if option2 == 1:
        # get last played tracks
        num_tracks_to_visualise = int(input("How many tracks would you like to visualise? "))
        last_played_tracks = spotify_client.get_last_played_tracks(num_tracks_to_visualise)

        print(f"\nHere are the last {num_tracks_to_visualise} tracks you listened to on Spotify:")
        for index, track in enumerate(last_played_tracks):
            print(f"{index+1}- {track}")

        # choose which tracks to use as a seed to generate a playlist
        indexes = input("\nEnter a list of up to 5 tracks you'd like to use as seeds."
                        "Use indexes separated by a space: ")
        indexes = indexes.split()
        seed_tracks = [last_played_tracks[int(index)-1] for index in indexes]

    else:
        num_tracks_to_visualise = int(input("How many tracks would you like to visualise? "))
        if option2 == 2:
            top_played_tracks = spotify_client.get_top_tracks_short(num_tracks_to_visualise)
        elif option2 == 3:
            top_played_tracks = spotify_client.get_top_tracks_medium(num_tracks_to_visualise)
        else:
            top_played_tracks = spotify_client.get_top_tracks_long(num_tracks_to_visualise)

        print(f"\nHere are the top {num_tracks_to_visualise} tracks you listened to on Spotify:")
        for index, track in enumerate(top_played_tracks):
            print(f"{index + 1}- {track}")

        # choose which tracks to use as a seed to generate a playlist
        indexes = input("\nEnter a list of up to 5 tracks you'd like to use as seeds."
                        "Use indexes separated by a space: ")
        indexes = indexes.split()
        seed_tracks = [top_played_tracks[int(index) - 1] for index in indexes]

    #customize!!
    yesno = ''
    while yesno != 'n' and yesno != 'y':
        yesno = str(input('\nWould you like to filter the recommendations? (Y/N): '))
        yesno = yesno.lower()
        #if yesno == 'y' or yesno == 'n': break

    if yesno == 'n':
        # get recommended tracks based off seed tracks
        recommended_tracks = spotify_client.get_track_recommendations(seed_tracks)
        print("\nHere are the recommended tracks which will be included in your new playlist:")
        for index, track in enumerate(recommended_tracks):
            print(f"{index+1}- {track}")

        # get playlist name from user and create playlist
        playlist_name = input("\nWhat's the playlist name? ")
        playlist = spotify_client.create_playlist(playlist_name)
        print(f"\nPlaylist '{playlist.name}' was created successfully.")

        # playlist cover
        #option3 = ''
        #while option3 != 'y' and option3 != 'n':
        #    option3 = str(input('\nWould you like a custom playlist cover? (Y/N): '))
        #    option3 = option3.lower()
        #if option3 == 'y':
        #    spotify_client.playlist_cover(playlist)

        # populate playlist with recommended tracks
        spotify_client.populate_playlist(playlist, recommended_tracks)
        print(f"\nRecommended tracks successfully uploaded to playlist '{playlist.name}'.")

    elif yesno == 'y':
        option1 = 0
        while option1 != 1 and option1 != 2:
            option1 = int(input('\n1. Presets\n2. Custom (Advanced)\n\nSelect number: '))
            #if option1 == 1 or option1 == 2: break

        if option1 == 1:
            presetselect = spotify_client.choose_presets()

            recommended_tracks2 = spotify_client.get_track_recommendations_presets(seed_tracks, preset=presetselect)
            print("\nHere are the recommended tracks which will be included in your new playlist:")
            for index, track in enumerate(recommended_tracks2):
                print(f"{index + 1}- {track}")

            # get playlist name from user and create playlist
            playlist_name = input("\nWhat's the playlist name? ")
            playlist = spotify_client.create_playlist(playlist_name)
            print(f"\nPlaylist '{playlist.name}' was created successfully.")

            # playlist cover
            # option3 = ''
            # while option3 != 'y' and option3 != 'n':
            #    option3 = str(input('\nWould you like a custom playlist cover? (Y/N): '))
            #    option3 = option3.lower()
            # if option3 == 'y':
            #    spotify_client.playlist_cover(playlist)

            # populate playlist with recommended tracks
            spotify_client.populate_playlist(playlist, recommended_tracks2)
            print(f"\nRecommended tracks successfully uploaded to playlist '{playlist.name}'.")

        elif option1 == 2:
            print('\nEnter Values:')
            bpmtarget = int(input('\nBpm Target: '))
            bpmmin = int(input('Bpm Minimum: '))
            bpmmax = int(input('Bpm Maximum: '))
            acmin = float(input('Acousticness Min. (0-1): '))
            acmax = float(input('Acousticness Max. (0-1): '))
            dancemin = float(input('Danceability Min. (0-1): '))
            dancemax = float(input('Danceability Max. (0-1): '))
            energymin = float(input('Energy Min. (0-1): '))
            energymax = float(input('Energy Max. (0-1): '))
            valenmin = float(input('Valence Min. (0-1): '))
            valenmax = float(input('Valence Max. (0-1): '))

            recommendedtracks3=spotify_client.get_track_recommendations_custom(seed_tracks, bpmtarget=bpmtarget,
                                                                               bpmmin=bpmmin, bpmmax=bpmmax,
                                                                               acmin=acmin, acmax=acmax,
                                                                               dancemin=dancemin, dancemax=dancemax,
                                                                               energymin=energymin, energymax=energymax,
                                                                               valenmin=valenmin, valenmax=valenmax)
            print("\nHere are the recommended tracks which will be included in your new playlist:")
            for index, track in enumerate(recommendedtracks3):
                print(f"{index + 1}- {track}")

            # get playlist name from user and create playlist
            playlist_name = input("\nWhat's the playlist name? ")
            playlist = spotify_client.create_playlist(playlist_name)
            print(f"\nPlaylist '{playlist.name}' was created successfully.")

            # playlist cover
            # option3 = ''
            # while option3 != 'y' and option3 != 'n':
            #    option3 = str(input('\nWould you like a custom playlist cover? (Y/N): '))
            #    option3 = option3.lower()
            # if option3 == 'y':
            #    spotify_client.playlist_cover(playlist)

            # populate playlist with recommended tracks
            spotify_client.populate_playlist(playlist, recommendedtracks3)
            print(f"\nRecommended tracks successfully uploaded to playlist '{playlist.name}'.")



if __name__ == "__main__":
    main()