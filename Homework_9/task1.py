import time


class TrafficLight:
    __color = {'red': 7, 'yellow': 2, 'green': 3}


    def running(self):

        print('now red')
        time.sleep(self.__color['red'])
        print('now yellow')
        time.sleep(self.__color['yellow'])
        print('now green')
        time.sleep(self.__color['green'])


trafficlight = TrafficLight()
trafficlight.running()
