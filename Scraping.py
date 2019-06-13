import bs4 as bs
import urllib.request
import re
import json

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
webpage = opener.open("https://www.amazon.in/dp/B07DJHY82F/ref=gbph_img_m-5_d182_b23b14bf?smid=A23AODI1X2CEAE&pf_rd_p=a3a8dc53-aeed-4aa1-88bb-72ce9ddad182&pf_rd_s=merchandised-search-5&pf_rd_t=101&pf_rd_i=1389401031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=P3FSQH2KEB3B5QQ1NQD5")
soup=bs.BeautifulSoup(webpage,'lxml')
#print("Title:",soup.title.string)


dict={}
# for list1 in soup.find_all("div",class_="pdTab"):
#     i=i+1
#     print(list1.attrs)
#     if i==1:
#         print("Technical Details")
#         print(str(list1.text))
#     if i==2:
    
def remove(str):
    str= str.replace("\n","")
    str= str.replace("\t","")
    str = str.replace(u"\xa0", u"")
    str = str.replace('\s','')
    str = str.replace("  ","")
    return str

#Title
dict["Title"]=remove(soup.find("h1").text)
print(dict)
#description
dict["Description"]=remove(soup.find(id="productDescription").text)
print(dict)



#Large_image
span=soup.find(id="imgTagWrapperId").find("img").attrs["data-old-hires"]
url=span
dict["ImageUrl"]=url


#price
dict["Price"]=(remove(soup.find(id="priceblock_dealprice").text).replace("₹",""),remove(soup.find(id="maxBuyBackDiscountSection").text).replace("Up to","").replace(" off",""))



#details
div = soup.find_all("div",class_ = "pdTab")
details =  div[0].find_all("tr")
dict["Details"]={}
for i in details:
    dict["Details"][remove((i.contents[0].text))]= remove(i.contents[1].text)
del dict["Details"][""]


# number of review 
dict["No of reviews"]=remove(soup.find(id="acrCustomerReviewText").text.replace(" customer reviews",""))

#rating
dict["Rating"]=remove(soup.find("span",class_="arp-rating-out-of-text a-color-base").text)


#reviwes
list=[]
for i in range(10):
    url = 'https://www.amazon.in/OnePlus-Midnight-Black-128GB-Storage/product-reviews/B07DJHY82F/ref=cm_cr_getr_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber'
    url += '='+str(i+1)
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    webpage = opener.open(url)
    soup=bs.BeautifulSoup(webpage,'lxml')
    revs = soup.find_all('div' , class_ = "a-row a-spacing-small review-data")
    for rev in revs:
        list.append(remove(rev.text))      
#print(list)
dict["Reviews"]=list
print(dict)



# out = open('words.json', 'w')

# wordsJson = json.dumps(dict)

# # print(wordsJson)
# out.write((wordsJson))



##########################insert dictionary in mangodb#########
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["amamzon"]
print(myclient.list_database_names())
mycol = mydb["Product"]
print(mydb.list_collection_names())
x = mycol.insert_one(dict)
print(x.inserted_id)


