from scrapy import cmdline

# cmdline.execute("scrapy crawl quotes".split())
cmdline.execute("scrapy crawl quotes -o products.csv -t csv".split())