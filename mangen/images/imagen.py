#! /usr/bin/env python3
#coding: utf-8

from zencad import *
import os

import zencad.visual

#lazy.diag = True

wsize = (300, 200)

if not os.path.exists("generic"):
    os.makedirs("generic")

def doscreen(model, path, size):
	print("screen (path:{0}, size:{1})".format(path, size))
	screen(model, "generic/"+path, size)

#prim3d
doscreen(model=box(10,20,30), path="box.png", size=wsize)

doscreen(model=sphere(r=10), path="sphere0.png", size=wsize)
doscreen(model=sphere(r=10, yaw=deg(120)), path="sphere1.png", size=wsize)
doscreen(model=sphere(r=10, pitch=(deg(20), deg(60))), path="sphere2.png", size=wsize)
doscreen(model=sphere(r=10, yaw=deg(120), pitch=(deg(20), deg(60))), path="sphere3.png", size=wsize)

doscreen(model=cylinder(r=10, h=20), path="cylinder0.png", size=wsize)
doscreen(model=cylinder(r=10, h=20, yaw=deg(45)), path="cylinder1.png", size=wsize)

doscreen(model=cone(r1=20, r2=10, h=20), path="cone0.png", size=wsize)
doscreen(model=cone(r1=20, r2=10, h=20, yaw=deg(45)), path="cone1.png", size=wsize)
doscreen(model=cone(r1=0, r2=20, h=20), path="cone2.png", size=wsize)
doscreen(model=cone(r1=20, r2=0, h=20), path="cone3.png", size=wsize)

doscreen(model=torus(r1=20, r2=5), path="torus0.png", size=wsize)
doscreen(model=torus(r1=20, r2=5, yaw=deg(120)), path="torus1.png", size=wsize)
doscreen(model=torus(r1=20, r2=5, pitch=(deg(-20), deg(120))), path="torus2.png", size=wsize)
doscreen(model=torus(r1=20, r2=5, pitch=(deg(-20), deg(120)), yaw=deg(120)), path="torus3.png", size=wsize)
doscreen(model=torus(r1=20, r2=5, pitch=(deg(-140), deg(140)), yaw=deg(120)), path="torus4.png", size=wsize)
doscreen(model=torus(r1=20, r2=5, pitch=(deg(-20), deg(190)), yaw=deg(120)), path="torus5.png", size=wsize)

doscreen(model=sphere(r=10) - halfspace().rotateX(deg(150)), path="halfspace0.png", size=wsize)
doscreen(model=sphere(r=10) ^ halfspace().rotateX(deg(150)), path="halfspace1.png", size=wsize)

#prim2d
doscreen(model=rectangle(10, 20), path="rectangle0.png", size=wsize)
doscreen(model=rectangle(10, 20, wire=True), path="rectangle1.png", size=wsize)
doscreen(model=rectangle(20), path="rectangle2.png", size=wsize)
doscreen(model=rectangle(20, wire=True), path="rectangle3.png", size=wsize)

doscreen(model=circle(r=20), path="circle0.png", size=wsize)
doscreen(model=circle(r=20, wire=True), path="circle1.png", size=wsize)
doscreen(model=circle(r=20, angle=(deg(45), deg(90))), path="circle2.png", size=wsize)
doscreen(model=circle(r=20, angle=(deg(45), deg(90)), wire=True), path="circle3.png", size=wsize)

doscreen(model=ellipse(r1=40, r2=20), path="ellipse0.png", size=wsize)
doscreen(model=ellipse(r1=40, r2=20, wire=True), path="ellipse1.png", size=wsize)
doscreen(model=ellipse(r1=40, r2=20, angle=(deg(45), deg(90))), path="ellipse2.png", size=wsize)
doscreen(model=ellipse(r1=40, r2=20, angle=(deg(45), deg(90)), wire=True), path="ellipse3.png", size=wsize)

doscreen(model=polygon(pnts=[(0,0), (0,40), (20,10), (10,0)]), path="polygon0.png", size=wsize)
doscreen(model=polygon(pnts=[(0,0), (0,40), (20,10), (10,0)], wire=True), path="polygon1.png", size=wsize)

doscreen(model=ngon(r=20, n=3), path="ngon0.png", size=wsize)
doscreen(model=ngon(r=20, n=3, wire=True), path="ngon1.png", size=wsize)
doscreen(model=ngon(r=20, n=5), path="ngon2.png", size=wsize)
doscreen(model=ngon(r=20, n=5, wire=True), path="ngon3.png", size=wsize)
doscreen(model=ngon(r=20, n=8), path="ngon4.png", size=wsize)
doscreen(model=ngon(r=20, n=8, wire=True), path="ngon5.png", size=wsize)

doscreen(model=textshape(text="TextShape", fontpath="../../zencad/examples/fonts/testfont.ttf", size=100), path="textshape0.png", size=wsize)
doscreen(model=textshape(text="TextShape", fontpath="../../zencad/examples/fonts/mandarinc.ttf", size=100), path="textshape1.png", size=wsize)

doscreen(model=segment((10,10,10),(20,10,10)), path="segment0.png", size=wsize)

doscreen(model=polysegment([(0,0,0),(0,10,10),(0,10,20),(0,-10,20),(0,-10,10)]), path="polysegment0.png", size=wsize)
doscreen(model=polysegment([(0,0,0),(0,10,10),(0,10,20),(0,-10,20),(0,-10,10)], closed=True), path="polysegment1.png", size=wsize)
