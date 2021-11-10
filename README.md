
# infiniteBird
a python script that will randomly play bird sounds filtered at 3kHz infinitely.
samples were sourced from https://experiments.withgoogle.com/bird-sounds

the reason for creating this project was to experiment with bird sounds and their effect on plants/people.

https://www.forbes.com/sites/grrlscientist/2021/04/15/more-birds-make-you-as-happy-as-more-money/
https://www.hempbasics.com/hhusb/hh5elc.htm - specifically section 5 part 8

clone the repo,  in a terminal or via ssh
 `sudo apt install git libsdl2-mixer-2.0-0 -y `
at least on rasp pi B you have to default the jack output via terminal:

    `raspi-config` -> `System Options` -> `S2 Audio` -> `1 Force audio out through HDMI or 3.5mm jack`

rasp pi 4 should be like:

    `raspi-config` -> `Advanced Options` -> `A4 Audio Force audio out through HDMI or 3.5mm jack`. Select `1 Headphones`. 
 then run:
`cd /usr/local/`
`git clone https://github.com/proper1grows/infiniteBird.git`
`cd infiniteBird`
`pip3 install -r requirements.txt`
`python3 infiniteBird.py `
control + c to kill the noise.
[Video of the software in action on a rasp pi b](https://imgur.com/a/fn6BB2R)


