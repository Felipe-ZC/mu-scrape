# mu-scrape

Scrapes news articles from music blogs and other music related websites.
Finds a current list of artists from select record labels.  

# Setup

## Scrapy

[Install scrapy](http://doc.scrapy.org/en/latest/intro/install.html#using-a-virtual-environment-recommended) inside a virtual environment. 
[Avoid getting banned](https://docs.scrapy.org/en/latest/topics/practices.html#avoiding-getting-banned) while using Scrapy!

## Tor 

Install [Tor](https://www.torproject.org/docs/tor-doc-unix.html.en) 

Create a hashed password to enable authentication on Tor's ControlPort:

```
tor --hash-password mypassword
```

Update torrc:

```
HashedControlPassword hashedPassword 
```

Use one of the following to restart tor and apply changes:

```
// 1 
/etc/init.d/tor restart

// 2
sudo systemctl restart tor.service 

// 3 (Restarts all instances)
sudo systemctl restart tor-master.service 
```

## Privoxy

Install [Privoxy](https://www.privoxy.org/) 

Edit Privoxy's config file located at /etc/privoxy/config
and enable socks5 forwarding. This tells Privoxy to route 
traffic through Tor:

```
forward-socks5 / localhost:9050 .
```

## (Optional) Test Tor/Privoxy setup

Install stem:

```
pip install stem
```

Stem is a libary that acts as an interface to the Tor service.
Run the following script, which makes an HTTP request to a server
and returns the IP address of the requester:

```
import stem
import stem.connection

import time
from urllib import request as urlrequest

from stem import Signal
from stem.control import Controller

# initialize some HTTP headers
# for later usage in URL requests
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent}
proxy_host = '127.0.0.1:8118'

# request a URL 
def makeReq(url):
    # communicate with TOR via a local proxy (privoxy)
    req = urlrequest.Request(url); 
    req.set_proxy(proxy_host, 'http');
    
    return urlrequest.urlopen(req).read() 

def renew_connection():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password = 'dopeorder45')
        controller.signal(Signal.NEWNYM)
        controller.close()

for i in range(0,10):
    renew_connection()
    print(makeReq('http://icanhazip.com/'))
    time.sleep(10);
```

Each response SHOULD contain a new IP addresss. 
Try increasing the number of seconds in time.sleep() 
if too many responses contain the same IP address.  

## Configure Scrapy to use Privoxy


## scrapy-splash install docs

[Splash](https://splash.readthedocs.io/en/latest/index.html) is a JS rendering engine, includes an HTTP API.
[scrapy-splash](https://github.com/scrapy-plugins/scrapy-splash) is a scrapy plugin that provides integration with Splash.

## Splash HTTP proxy setup 

## TODO

- Create requirments file for venv python dependencies!
- Change name of proxy middleware...

- WIP:
	- Full news articles
	- More artist names
 
- Pitchfork Spider breaks after 145 pages... (503 Error)
- Refactor README
- Containerzie this application
	- Tor
	- Privoxy
	- Splash
	- Scrapy
	- Python 3.7

## Current concerns

1) How can we ensure that our spiders are parsing each webpage correctly?
2) How do you we track changes in the webpages we scrape?
3) How do we stay annonymous?
	- Use Privoxy to route scrapy HTTP traffic through the Tor network.
	- HTTP traffic from scrapy is routed through Privoxy, which forwards this stream to Tor.
	- Setup Tor locally & Privoxy locally [Use this link for help!](https://dm295.blogspot.com/2016/02/tor-ip-changing-and-web-scraping.html)
	- By setting our locally configured Privoxy server as an HTTP proxy for our scrapy spiders, we can scrape anonymously.
 
4) Where should we store the data gathered from scraping?
	- MongoDB (Atlas) 
