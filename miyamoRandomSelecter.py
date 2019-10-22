import maya.cmds as mc
import random as r

obj = mc.ls(sl=True)
length = len(obj)
numberOfObj = r.randrange(1, length, 1)
sl = []
for i in range(numberOfObj):
	sl.append(obj[r.randrange(length)])

mc.select(sl)
