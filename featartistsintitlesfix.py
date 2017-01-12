PLUGIN_NAME = 'Feat. Artists in Titles (Fix)'
PLUGIN_AUTHOR = 'Lukas Lalinsky, Michael Wiencek, Bryan Toth edited by JeromyNix (NobahdiAtoll)'
PLUGIN_DESCRIPTION = 'Move "feat." from artist names to album and track titles. Match is case insensitive. (sort order tags included)'
PLUGIN_VERSION = "0.2"
PLUGIN_API_VERSIONS = ["0.9.0", "0.10", "0.15", "0.16"]

from picard.metadata import register_album_metadata_processor, register_track_metadata_processor
import re


def move_album_featartists(tagger, metadata, release):
    match = re.match(r"([\s\S]+) feat.([\s\S]+)", metadata["albumartist"], re.IGNORECASE)
    if match:
        metadata["albumartist"] = match.group(1)
        metadata["album"] += " (feat.%s)" % match.group(2)
    match = re.match(r"([\s\S]+) feat.([\s\S]+)", metadata["albumartistsort"], re.IGNORECASE)
    if match:
        metadata["albumartistsort"] = match.group(1)


def move_track_featartists(tagger, metadata, release, track):
    match = re.match(r"([\s\S]+) feat.([\s\S]+)", metadata["artist"], re.IGNORECASE)
    if match:
        metadata["artist"] = match.group(1)
        metadata["title"] += " (feat.%s)" % match.group(2)
    match = re.match(r"([\s\S]+) feat.([\s\S]+)", metadata["artistsort"], re.IGNORECASE)
    if match:
        metadata["artistsort"] = match.group(1)

register_album_metadata_processor(move_album_featartists)
register_track_metadata_processor(move_track_featartists)
