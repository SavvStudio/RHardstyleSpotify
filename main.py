import loop
import clearandpopulate_playlist

def main():
    loop.run_function_every_monday(clearandpopulate_playlist.run_playlist_creation)

main()