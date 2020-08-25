# Bulk Download of photos from PLEX playlist

import os
from plexapi.server import PlexServer
from plexapi import utils

baseurl = 'http://localhost:32400'
token = 'PLACE TOKEN HERE'
plex = PlexServer(baseurl, token)

playlists = [pl for pl in plex.playlists() if pl.isPhoto]
playlist = utils.choose('Choose Playlist', playlists,
                        lambda pl: '%s' % pl.title)

for photo in playlist.items():
    photomediapart = photo.media[0].parts[0]

    if photo.year == 2018 or photo.year == 2019:
        print('Downlod File: %s' % photomediapart.file)
        url = plex.url('%s?download=1' % photomediapart.key)
        utils.download(url, token, os.path.basename(photomediapart.file), '%s' % photo.year)
    else:
        print('Skip File: %s | %s' % (photomediapart.file, photo.year))
