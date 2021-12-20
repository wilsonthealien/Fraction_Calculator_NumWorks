from math import *
from kandinsky import *
from ion import *
from time import *
backcolor=(0,0,100)
num=1
denom=1
fill_rect(0,0,322,222,backcolor)
fill_rect(0,84,322,3,"grey")
fill_rect(0,110,322,3,"grey")
while 1:
  draw_string("(Use Arrow keys",5,150,(0,0,0),(255,204,153))
  draw_string("To change values.)",5,172,(0,0,0),(51,204,204))
  draw_string("To Reset, BackSpace",5,194,(0,0,0),(153,204,0))
  fract=num/denom
  draw_string("Numerator   :  "+str(num),10,25,"cyan",(0,0,0))
  draw_string("Denominator :  "+str(denom),10,45,"pink",(0,0,0))
 
  draw_string("= "+str(fract),25,90,"white",(0,0,0))
  if keydown(KEY_UP):
    fill_rect(0,0,322,222,backcolor)
    fill_rect(0,84,322,3,"grey")
    fill_rect(0,110,322,3,"grey")
    sleep(0.2)
    num+=1
  if keydown(KEY_DOWN):
    fill_rect(0,0,322,222,backcolor)
    fill_rect(0,84,322,3,"grey")
    fill_rect(0,110,322,3,"grey")
    sleep(0.2)
    num-=1
  if keydown(KEY_RIGHT):
    fill_rect(0,0,322,222,backcolor)
    fill_rect(0,84,322,3,"grey")
    fill_rect(0,110,322,3,"grey")
    sleep(0.2)
    denom+=1
  if keydown(KEY_LEFT):
    fill_rect(0,0,322,222,backcolor)
    fill_rect(0,84,322,3,"grey")
    fill_rect(0,110,322,3,"grey")
    sleep(0.2)
    denom-=1
  if keydown(KEY_BACKSPACE):
    sleep(0.2)
    num=1
    denom=1
   
    fill_rect(0,0,322,222,backcolor)
    fill_rect(0,84,322,3,"grey")
    fill_rect(0,110,322,3,"grey")
 
  if denom<1:
    denom=1
  if num>denom:
    draw_string("Mix Number",215,2,(0,0,100),(153,204,255))
  if num==denom:
    draw_string("Equal 1",215,2,(0,0,100),(153,204,255))
  if num<denom:
    draw_string("Fraction",215,2,(0,0,100),(153,204,255))
 
 
 
