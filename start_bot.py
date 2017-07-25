#!/usr/bin/python

import subprocess
import os

name = 'bot-promocoes.py'

command = 'pgrep -f ' + name
out = subprocess.Popen(command, stdout = subprocess.PIPE,
        shell = True)
(p, err) = out.communicate()

pid = p.split()

print 'Pid: ' + str(pid)

if len(pid) < 2:
    command = 'nohup python ' + name + ' &'
    os.system(command)
    print "Let's go bot!"
else:
    print "Bot still working..."

