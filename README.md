VKMusic
========

Inspired by and main code from [VKPorter](https://github.com/amka/VKPorter)

Edid for audio download by me [korzhyk](https://github.com/korzhyk).

Extremely small tool to export audios from [vk.com](https://vk.com).


## Prerequisites

Before you can start using VKMusic you have to install some python libraries if you don't have it.

### Requests

[https://github.com/kennethreitz/requests](https://github.com/kennethreitz/requests)

    $ pip install requests

or, with [easy_install](http://pypi.python.org/pypi/setuptools):

    $ easy_install requests

### VK_API
[https://github.com/python273/vk_api](https://github.com/python273/vk_api)

    $ pip install vk_api

## Usage

Synopsis:

    $ vkmusic.py [-h] [-v] [-o OUTPUT] [-p PASSWORD] username

See also `vkmusic --help`.

### Examples

    $ vkmusic.py -p RawPa$$word username
    
all audios will be exported to `./Music`.

    $ vkmusic.py -o ~/Music username
    
audios will be exported to `~/Music`.

    $ vkmusic.py -s username

audios will be exported to artist name folders ex. `Adele - Let The Sky Fall.mp3` will be saved to `./Music/Adele/Let The Sky Fall.mp3`

### Screenshot
![VKMusic](terminal.png)
