## Pre set

In order to execute directly in shell as "yd china", creat a script file `/usr/bin/yd` whith content:

    #!/bin/bash
    python ~/Dropbox/myapps/youdao-dic/youdao.py $@

And then change the execute mode of `/usr/bin/yd`:

    $ sudo chmod +x /usr/bin/yd

## Usage

Simple definition:

    yd word

Specific definition:

    yd word -s
