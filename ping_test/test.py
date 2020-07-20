import re
from subprocess import Popen, PIPE
from threading import Thread


class Pinger(object):
    def __init__(self, hosts):
        for host in hosts:
            pa = PingAgent(host)
            pa.start()

class PingAgent(Thread):
    def __init__(self, host):
        Thread.__init__(self)        
        self.host = host

    def run(self):
        #p = Popen('ping -n 1 ' + self.host, shell=True, stdout=PIPE)
        p = Popen('ping -c 1 ' + self.host, shell=True, stdout=PIPE)
        #m = re.search(b'Average = (.*)ms', p.stdout.read())
        m = re.search(b'avg = (.*)ms', p.stdout.read())
        #m = re.search(b'bytes from= (.*)ms', p.stdout.read())
        if m: print ('Round Trip Time: %s ms -' % m.group(1), self.host)
        else: print ('Error: Invalid Response -', self.host)


if __name__ == '__main__':
    hosts = [
        #'www.pylot.org',
        #'www.goldb.org',
        #'www.google.com',
        #'www.yahoo.com',
        #'www.techcrunch.com',
        #'www.this_one_wont_work.com'
        '10.88.179.248',
        '10.88.179.249',
        '10.88.179.250',
        '10.88.179.251',
        '10.88.179.252',
        '10.88.179.253',
        '10.88.179.254',
        '10.88.179.255',
        '10.88.179.256',
        '10.88.179.257',
        '10.88.179.258',
        '10.88.179.259',
        '10.88.179.260',
       ]
    Pinger(hosts)
