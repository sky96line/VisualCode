import thread
import time


def outMsg(threadName):
  fr = open('data', 'r')
  data = fr.read()
  data = data.split('\n')
  print(data[-1].split(': ')[1])


def inMsg(threadName):
  user = 'BotTwo'
  msg = raw_input('Enter message : ')
  fw = open('data', 'a+')
  fw.write('\n')
  fw.write(user + ' : ' + msg)
  fw.close()


while True:
  try:
    thread.start_new_thread(outMsg, ("Display",))
    thread.start_new_thread(inMsg, ("Input",))
  except:
    print "Error: unable to start thread"
  time.sleep(1)
