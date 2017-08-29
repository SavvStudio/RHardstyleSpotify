import configparser

def get_configuration():
    config = configparser.ConfigParser()
    config.read("RHardstyleSpotifyAccess.ini")
    access = config["RHARDSTYLESPOTIFY_ACCESS"]
    return access