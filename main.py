import loop
import clearandpopulate_playlist

def main():
    print("======== /R/HARDSTYLE SPOTIFY PLAYLIST CREATOR ========")
    loop.run_function_every_monday(clearandpopulate_playlist.run_playlist_creation)

main()