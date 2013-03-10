VKMusic
========

Inspired by and main code from [VKPorter](https://github.com/amka/VKPorter)

Edit for audio download by me [korzhyk](https://github.com/korzhyk).

Extremely small tool to export audios from [vk.com](https://vk.com).

Home page [VKMusic](http://korzhyk.github.com/VKMusic)

## Installation

    $ easy_install VKMusic

    $ pip install VKMusic

## Usage

Synopsis:

    $ vkmusic [-h] [-v] [-o OUTPUT] [-p PASSWORD] username

See also `vkmusic --help`.

### Examples

    $ vkmusic -p RawPa$$word username
    
all audios will be exported to `./Music`.

    $ vkmusic -o ~/Music username
    
audios will be exported to `~/Music`.

    $ vkmusic -s username

audios will be exported to artist name folders ex. `Adele - Let The Sky Fall.mp3` will be saved to `./Music/Adele/Let The Sky Fall.mp3`

### Screenshot
[![VKMusic](http://korzhyk.github.com/VKMusic/images/terminal.png)](http://korzhyk.github.com/VKMusic/images/terminal.png)
