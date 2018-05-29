# -*- coding: utf-8 -*-
PLUGIN_NAME = 'Tagger script functions is_lossless() and is_lossy()'
PLUGIN_AUTHOR = 'Philipp Wolfer'
PLUGIN_DESCRIPTION = 'Tagger script functions to detect if a file is lossless or lossy'
PLUGIN_VERSION = "0.1"
PLUGIN_API_VERSIONS = ["1.3.0"]
PLUGIN_LICENSE = "GPL-2.0"
PLUGIN_LICENSE_URL = "https://www.gnu.org/licenses/gpl-2.0.html"

from picard.script import register_script_function

LOSSLESS_EXTENSIONS = ['flac', 'oggflac', 'ape', 'ofr', 'tak', 'wv', 'tta', 'wav']

def is_lossless(parser):
    """
    Returns true, if the file processed is a lossless audio format.
    Note: This depends mainly on the file extension and does not look inside the
    file to detect the codec.
    """
    if parser.context['~extension'] in LOSSLESS_EXTENSIONS:
        return "1"
    elif parser.context['~extension'] == 'm4a':
        # Mutagen < 1.26 fails to detect the bitrate for Apple Lossless Audio Codec.
        if not parser.context['~bitrate'] or parser.context['~bitrate'] > 1000:
            return "1"
        else:
            return ""
    else:
        return ""

def is_lossy(parser):
    """Returns true, if the file processed is a lossy audio format."""
    if is_lossless(parser) == "1":
        return ""
    else:
        return "1"

register_script_function(is_lossless)
register_script_function(is_lossy)
