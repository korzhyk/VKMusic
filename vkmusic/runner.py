#!/usr/bin/env python

"""
    :mod:`vkmusic`
    ~~~~~~~~~~~~~~~

    A micro tool for export audio from `vk.com <https://vk.com>`_.
     It's based on `VK_API <https://github.com/python273/vk_api>`_
     by Kirill Python <mikeking568@gmail.com>,
     `Requests <python-requests.org>`_.

    :copyright: (c) 2013 by Andrii Korzh.
    :license: BSD, see LICENSE for more details.
"""

__author__ = 'Andrii Korzh <Andrii.Korzh@gmail.com>'
__date__ = '10.03.13'
__version__ = '0.0.3'

import argparse
import datetime
from getpass import getpass
import os
import time
import sys
import requests
from vk_api import VkApi

def connect(login, password):
    """Initialize connection with `vk.com <https://vk.com>`_ and try to authorize user with given credentials.

    :param login: user login e. g. email, phone number
    :type login: str
    :param password: user password
    :type password: str

    :return: :mod:`vk_api.vk_api.VkApi` connection
    :rtype: :mod:`VkApi`
    """
    return VkApi(login, password)


def get_albums(connection):
    """Get albums list for currently authorized user.

    :param connection: :class:`vk_api.vk_api.VkApi` connection
    :type connection: :class:`vk_api.vk_api.VkApi`

    :return: list of audio albums or ``None``
    :rtype: list
    """
    try:
        return connection.method('audio.getAlbums')
    except Exception as e:
        print(e)
        return None


def get_audios(connection):
    """Get audios list for selected album.

    :param connection: :class:`vk_api.vk_api.VkApi` connection
    :type connection: :class:`vk_api.vk_api.VkApi`

    :return: list of photo albums or ``None``
    :rtype: list
    """
    try:
        return connection.method('audio.get')
    except Exception as e:
        print(e)
        return None


def download(audio, output, title):
    """Download audio

    :param audio: hash
    :param output: string 
    """
    if not os.path.exists(output):
        os.makedirs(output)
    r = requests.get(audio['url'])
    with open(os.path.join(output, '%s.mp3' % title), 'wb') as f:
        for buf in r.iter_content(1024):
            if buf:
                f.write(buf)

def get_title(audio):
    return "%s - %s" % (audio['artist'], audio['title'])

def main():
    parser = argparse.ArgumentParser(description='', version='%(prog)s ' + __version__)
    parser.add_argument('-o', '--output', help='output path to store photos',
                        default='~/Music')
    parser.add_argument('username', help='vk.com username')
    parser.add_argument('-p','--password', help='vk.com password')
    parser.add_argument('-s','--sort', help='sort by artist folder', action='store_true')

    args = parser.parse_args()

    # expand user path if necessary
    if args.output.startswith('~'):
        args.output = os.path.expanduser(args.output)

    start_time = datetime.datetime.now()
    try:
        password = args.password or getpass("Password: ")

        # Initialize vk.com connection
        connection = connect(args.username, password)

        # Request list of audios
        audios = get_audios(connection)
        if len(audios) > 0:
            print("Found %s audio%s:\n" % (len(audios), 's' if len(audios) > 1 else ''))
            print('%3s. %-80s %s' % ('No', 'Title', 'Duration'))
            ix = 0
            for audio in audios:
                ix += 1
                print('%3d. %-80s %s' % (ix, get_title(audio), datetime.timedelta(seconds=audio['duration'])))
            print("\r")

            # Sleep to prevent max request count
            time.sleep(1)

            processed = 1

            prev_s_len = 0  # A length of the previous output line.
            for audio in audios:
                percent = round(float(processed) / float(len(audios)) * 100, 2)
                output_s = "\rExporting %-75s %s of %s (%d%%)" % (get_title(audio), processed, len(audios), percent)
                # Pad with spaces to clear the previous line's tail.
                # It's ok to multiply by negative here.
                output_s += ' '*(prev_s_len - len(output_s))
                sys.stdout.write(output_s)
                prev_s_len = len(output_s)
                sys.stdout.flush()

                output = os.path.join(args.output, audio['artist'] if args.sort else '')

                download(audio, output, audio['title'] if args.sort else get_title(audio))
                processed += 1
        else:
            print("\nNo audios found! Exiting...")
            sys.exit(0)

    except Exception as e:
        print(e)
        sys.exit(1)

    except KeyboardInterrupt:
        print('\nVKMusic exporting stopped by keyboard')
        sys.exit(0)

    finally:
        print("\nDone in %s" % (datetime.datetime.now() - start_time))

if __name__ == '__main__':
    main()