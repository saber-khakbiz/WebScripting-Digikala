
from persiantools import digits
from bs4 import BeautifulSoup
import requests
import re
import sys


#*Geneal list and Variable
N=2             #?  Number of pages {min=2,max=10}
Ram_lst=[]      #?  List ALL Memorey Ram
Ram_pr={}       #?  Propety Each Memorey Ram
brand_lst=[]    #?  List ALL Name of Memorey Ram
con=1           #?  counter for countering number Ram on Each Page



#*animate processing
print("\nProcessing, Please Wait..")
animation = ["[□□□□□□□□□]", "[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
S=len(animation)
step=S-N
sys.stdout.write("\r" + animation[0])
sys.stdout.flush()



#! Patterns for Extracting Data

pattern_Brand=r"(?:data-fa|data-en)=[\"]([\w\s\.\-ااُچ‌پی]+.)[\"]"
pattern_DDRX=r"DDR([\d])"
pattern_Freq=r"([\w]+)\s*(?:مگاهرتز|مگا هرتز|Mhz|MHz|mhz|MHZ|[sS])"
pattern_Cap=r"([\d]+)\s*(?:گیگابایت|Gb|GB|گيگابايت)"
pattern_Cost=r"([\w ,]+.) تومان"


#!<<<<<<<<<<<<<<<<<< Pull and save name of ram brands >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

link_b=f"https://www.digikala.com/search/category-ram/?has_selling_stock=1&q=ram&pageno=1&sortby=4/"
page_b=requests.get(link_b)
soup_b= BeautifulSoup(page_b.content,"html.parser")
main_b=soup_b.find(id="main")
Ram_brand_lst=main_b.find_all(class_ = "c-box c-box--brands-filter js-ab-sidebar-filter")
x=re.findall(pattern_Brand,str(Ram_brand_lst))
x.pop()
for b in zip([i for i in x if x.index(i)%2],[j for j in x if not x.index(j)%2]):
    if b == ('اچ\u200cپی', 'HP'):
        brand_lst.append(("اچ پی","HP"))
    elif b==('گیگابایت','GIGABYTE'):
        brand_lst.append(("گیل","GIGABYTE"))
    else:
        brand_lst.append(b)



#*first animate processing element
sys.stdout.write("\r" + animation[1])
sys.stdout.flush()





#!<<<<<<<<<<<<<<<<<< Pull and save Ram Propertiy DATA >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

for page in range(1,N):
    #* Request to Digikala avalible Ram  Page
    link=f"https://www.digikala.com/search/category-ram/?has_selling_stock=1&q=ram&pageno={page}&sortby=4/"
    Page=requests.get(link)
    soup= BeautifulSoup(Page.content,"html.parser")
    main=soup.find(id="main")
    Ram_propeity=main.find_all(class_ = "c-product-box__title")
    Ram_cost=main.find_all(class_ = "c-price__value-wrapper")  
    
    
    #*animate processing
    count=page+step
    sys.stdout.write("\r" + animation[count])
    sys.stdout.flush()



    for p,c in zip(Ram_propeity,Ram_cost):
        #* Text of Ram
        txt_ram=p.get_text()
        txt_cost=c.get_text().strip()
        
        #* Model of Ram's DDRX {2 or 3 or 4}
        ddrx=re.findall(pattern_DDRX,txt_ram)
        if not ddrx:
            ddrx=None
        else:
            ddrx=digits.fa_to_en(ddrx[0]).strip()

        #* Frequency of RAM [Mhz]
        freq=re.findall(pattern_Freq,txt_ram)
        if not freq:
            freq=None
        else:
            freq=digits.fa_to_en(freq[0].strip())
            freq="".join([i for i in freq if i.isdigit()])

        #* Capacity of Ram [GB]
        capacity=re.findall(pattern_Cap,txt_ram)
        if not capacity:
            capacity=None
        else:
            capacity=digits.fa_to_en(capacity[0].strip())
        
        #* Cost of Ram [Toman]
        cost=re.findall(pattern_Cost,txt_cost)
        if not cost:
            cost_en=None
        else:
            cost_fa=cost[0].replace(",","")
            cost_en=digits.fa_to_en(cost_fa).strip()

        #* brand name Ram
        Brand=''
        for name in brand_lst:
            pattern_name_brand=rf"\b{name[0]}\b"
            x=re.findall(pattern_name_brand,txt_ram)
            if len(x)>0:
                Brand=name[1]
        if len(Brand)==0:
            Brand='Miscellaneous'

        
        Ram_pr["BrandName"]=Brand
        Ram_pr["Capacity"]=capacity
        Ram_pr["DDRX"]=ddrx
        Ram_pr["frequency"]=freq
        Ram_pr["Price"]=cost_en
        Ram_lst.append(Ram_pr.copy())

        #? maximum Number of Ram in each Page is 36 {removing advertiasig Ram in page below }
        con+=1
        if con==37:
            break
