import webbrowser

def search(query, cm):
    
    if "youtube" in query:
        webbrowser.open(f"http://www.youtube.com/results?search_query={cm}")
    
    elif "facebook" in query:
        webbrowser.open(f"https://www.facebook.com/search/top?q={cm}")
            
    elif "amazon" in query:
        webbrowser.open(f"https://www.amazon.com/s?k={cm}&ref=nb_sb_noss_2")

    elif "flipkart" in query:
        webbrowser.open(f"https://www.flipkart.com/search?q={cm}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

    elif "snapdeal" in query:
        webbrowser.open(f"https://www.snapdeal.com/search?keyword={cm}&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy")

    elif "ebay" in query:
        webbrowser.open(f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={cm}&_sacat=0")

    elif "yahoo" in query:
        webbrowser.open(f"https://in.search.yahoo.com/search;_ylt=AwrxiDbKPVhhYhQA_RG6HAx.;_ylc=X1MDMjExNDcyMzAwMgRfcgMyBGZyAwRmcjIDc2ItdG9wLXNlYXJjaARncHJpZANNdTQ1U0ZyeFRKRzhHdWU3cmFrU1pBBG5fcnNsdAMwBG5fc3VnZwMxMARvcmlnaW4DaW4uc2VhcmNoLnlhaG9vLmNvbQRwb3MDMARwcXN0cgMEcHFzdHJsAzAEcXN0cmwDNQRxdWVyeQNoZWxsbwR0X3N0bXADMTYzMzE3Mjk1MQ--?p={cm}&fr=sfp&iscqry=&fr2=sb-top-search")

    else:
        url = f"https://www.google.com/search?q={cm}"
        webbrowser.open(f"{url}")
