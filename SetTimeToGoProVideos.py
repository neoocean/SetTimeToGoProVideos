# -*- coding: utf-8 -*-

import os
import fnmatch

# 'GOPR'로 시작하는 파일 이름을 던지면 연속으로 촬영된 파일을 'run' 리스트에 붙여줌.
def getFilesByNumber(n): 
	list = fnmatch.filter(os.listdir(os.getcwd()), ('GP??' + n.zfill(4) + '.MP4'))
	for f in list:
		run.append(f)

videos = fnmatch.filter(os.listdir(os.getcwd()), 'GOPR*.MP4')
videos.sort()

run = []

for f in videos:
	run.append(f)
	getFilesByNumber(f[4:8])

if len(run) > 720: 
	print '한 번에 최대 720개 까지만 처리할 수 있습니다.'

hour = 0
minute = 0

for f in run: 
	command = 'SetFile -d \'01/01/2016 ' + str(hour).zfill(2) + ':' + str(minute).zfill(2) + ':00\' ' + f
	print command
	os.system(command)

	minute = minute + 1
	if minute > 59:
		minute = 0
		hour = hour + 1
