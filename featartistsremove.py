PLUGIN_NAME = 'Feat. Artists Complete Removal'
PLUGIN_AUTHOR = 'JeromyNix (edited version of plugin by Lukas Lalinsky, Michael Wiencek, Bryan Toth)'
PLUGIN_DESCRIPTION = 'Complete removal of "feat." from artist names. Match is case insensitive.'
PLUGIN_VERSION = "0.1"
PLUGIN_API_VERSIONS = ["0.9.0", "0.10", "0.15", "0.16"]

from picard.metadata import register_album_metadata_processor, register_track_metadata_processor
import re


def remove_album_featartists(tagger, metadata, release):
    match = re.match(r"([\s\S]+) feat.([\s\S]+)", metadata["albumartist"], re.IGNORECASE)
    if match:
        metadata["albumartist"] = match.group(1)
    match = re.match(r"([\s\S]+) feat.([\s\S]+)", metadata["albumartistsort"], re.IGNORECASE)
    if match:
        metadata["albumartistsort"] = match.group(1)


def remove_track_featartists(tagger, metadata, release, track):
    match = re.match(r"([\s\S]+) feat.([\s\S]+)", metadata["artist"], re.IGNORECASE)
    if match:
        metadata["artist"] = match.group(1)
    match = re.match(r"([\s\S]+) feat.([\s\S]+)", metadata["artistsort"], re.IGNORECASE)
    if match:
        metadata["artistsort"] = match.group(1)

register_album_metadata_processor(remove_album_featartists)
register_track_metadata_processor(remove_track_featartists)
