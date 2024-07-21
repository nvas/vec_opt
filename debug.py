#!/usr/bin/python3

#====================================================
# for debugging: print debug message, and optionally launch interactive shell
import code
import inspect
#====================================================

def debug(msg='', shell=0):

  callerframerecord = inspect.stack()[1] # 0...this line, 1...line at caller
  lsep = '\n' if shell else ''
  shell = shell or msg=='' # without parameters --> shell=True
  frame = callerframerecord[0]
  info = inspect.getframeinfo(frame)
  loc = lsep+info.filename+":"+str(info.lineno)+' ('+info.function+")" # file, line#, func
  #loc = ''+str(info.lineno) # only line#
  print(f'{loc} Debug:{msg}{lsep}')
  if shell != 0:
    code.interact(local={**frame.f_locals,**globals()}) # [CTL+D] to continue
#====================================================
