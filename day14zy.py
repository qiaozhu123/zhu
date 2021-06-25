import threading
import time
bread=0
class cook(threading.Thread):
    username=""
    def run(self) -> None:
        global bread
        while True:
            if bread<500:
                bread+=1
                print(self.username,"做了一个面包","现有面包",bread)
                time.sleep(3)
            elif bread == 500:
                print(self.username,"休息3秒")
                time.sleep(3)
class buyer(threading.Thread):
    username=""
    money=1000
    def run(self) -> None:
        global bread
        while True:
            if bread>0:
                if self.money>=2:
                    bread-=1
                    self.money-=2
                    print(self.username,"买了一个面包")
                    time.sleep(10)
                else:
                    break
            else:
                print("没面包了，等两秒吧")
                time.sleep(2)
c1=cook()
c2=cook()
c3=cook()
p1 = buyer()
p2 = buyer()
p3 = buyer()
p4 = buyer()
p5 = buyer()
p1.username = "顾客一"
p2.username = "顾客二"
p3.username = "顾客三"
p4.username = "顾客四"
p5.username = "顾客五"
c1.username="厨师一"
c2.username="厨师二"
c3.username="厨师三"
c1.start()
c2.start()
c3.start()
p1.start()
p2.start()
p3.start()
p4.start()
p5.start()