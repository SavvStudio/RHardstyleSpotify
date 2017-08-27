import configparser

def get_configuration():
    config = configparser.ConfigParser()
    config.read("C:\\Users\\Savvas\\RHardstyleSpotifyAccess.ini")
    access = config["RHARDSTYLESPOTIFY_ACCESS"]
    return access