import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"   #spider name
    allowed_domains = ["books.toscrape.com"]   #this is the domains to scrape from  - allowed domains used bcos urls link to multiple others so we are making the spider only crawl inside 1 domain 
    start_urls = ["https://books.toscrape.com"]   #this is the first url the spider will scrape through, but you can have multiple so its 1 after the other

    def parse(self, response):  #when the response comes back then we can extract the data from it
        books = response.css("article.product_pod") #this is to get the article element with this class

        for book in books:  #defining everyrhing we want to scape with our scrapy spider
            yield{
                "name" : book.css("h3 a::text").get(),
                "price" : book.css(".product_price .price_color::text").get(),
                "url" : book.css("h3 a").attrib["href"],
            } #this is like return
            #after you define all your returns then you should exit scrapy shell

        next_page = response.css("li.next a ::attr(href)").get()  #this will access the next page & gets the ending of the url

        if next_page is not None:  #if it exists
            if "catalogue/" in next_page:  #this is a way to have every page include the catalogue word in the url as its needed else page wont scrape properly
                next_page_url = "https://books.toscrape.com/" + next_page  #this is the complete url link 
            else:
                next_page_url = "https://books.toscrape.com/catalogue/" + next_page
            yield response.follow(next_page_url, callback = self.parse)  #it will return by going to that url & the callback is the function that will get executed once we get the response back & it starts self.parse which is the function above

        #above only 
            
            
            
            
            #go to the scrapy.cfg file using cd"Insert yout Folder location here"
            #this is the root

            # then run scrapy crawl bookspider - now we get all the info 


            #Part 2 - for multiple pages

            # go back to the initial scrapy folder (cd .. to go out of a folder)

            #then scrapy shell, fetch("https://books.toscrape.com/")

            #response.css("li.next a ::attr(href))").get() this is now to get the list with next class so we can get the items on other pages

            #output is catalogue/page=2/html

            #i highlighted over the next button & saw this



    
#using scrapy shell to get the css selectors we want
#scrapy shell is an area where you can access the scrapy code very fast
#we use it so we can tell scrapy what css tags (classses & ids) to extract from

#pip install ipython is the terminal command to make the scrapy shell 
# go to scrapy.cfg & type "shell = ipython"

# this is [1]
#the available scrape commands written inside there
#fetch("https://books.toscrape.com/") was run so that we access this url   - stores it in a variable in a response variable

#this is [2]
#then type in response 
# we get a response code of 200 so its been executed successfully

#this is [3]
#response.css("article.product_pod") then type the response.css("html element.css class selector")

#OUTPUT IS ALL THE OTHER ELEMENTS WITH ARTICLE TAG & CLASS = PRODUCT_POD

#[4] - response.css("article.product_pod").get() this collects the 1st item part of article tag & class product_pod

# books = response.css("article.product_pod") this will store all the cases into the books variable

# len(books) = 20 this means that we have 20 cases of article elements with class=product_pod 

#to get the name, price & URL

# book = books[0] this will store the first book
# book.css(" h3 a::text").get()   this will open the first article with class = product_pod then it goes to the h3 tag & then to the a tag & find the text attribute & outputs that 

#In [7]: book.css(".product_price .price_color::text").get()   - this line is from article then a div block with a class called product_price then another p element with class .price color then the text to get the text 
#Out[7]: '£51.77'  #this is the result - PERFECT
#book.css(" h3 a").attrib["href"]   this goes from the article with product_pod class to the h3 elements then a element & gets the value with the attribute href
