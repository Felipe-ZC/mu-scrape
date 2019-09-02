# mu-scrape

#### Avoid getting banned

From the scrapy docs:

>Some websites implement certain measures to prevent bots from crawling them,
with varying degrees of sophistication. Getting around those measures can be
difficult and tricky, and may sometimes require special infrastructure. 
>
> Here are some tips to keep in mind when dealing with these kinds of sites:
>    * rotate your user agent from a pool of well-known ones from browsers (google around to get a list of them)
>    * disable cookies (see COOKIES_ENABLED) as some sites may use cookies to spot bot behaviour
>    * use download delays (2 or higher). See DOWNLOAD_DELAY setting.
>    * if possible, use Google cache to fetch pages, instead of hitting the sites directly
>    * use a pool of rotating IPs. For example, the free Tor project or paid services like ProxyMesh. An open source alternative is scrapoxy, a super proxy that you can attach your own proxies to.
>    * use a highly distributed downloader that circumvents bans internally, so you can just focus on parsing clean pages. One example of such downloaders is Crawlera

