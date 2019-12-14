#!/usr/bin/python3

import os, time
from random import randint

cmds = ['figlet -ctf digital', 'figlet -ctf small', 'cowsay', 'figlet -ctf digital', 'figlet -ctf lean', 'cowthink']
args = ['Class of 2019', 'About Time', '4.5 Years!!!', 'I ate ramen', 'Now what?', 'Cs get degrees', 'Can you decode my message?']

while True:
	cmd = cmds[randint(0, len(cmds)-1)]
	arg = args[randint(0, len(args)-1)]
	os.system('clear')
	os.system('clear')
	os.system(f"{cmd} {arg} | lolcat -p {randint(0, 999)}")
		
	time.sleep(10)