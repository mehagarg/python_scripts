# make sure you import BeautifulSoup in Python
# run from the location your html file is
# output can be done via >>
# 
from BeautifulSoup import BeautifulSoup as BS
soup = BS(open('PlayStoreDevices.txt'))

def getProductDictionariesList(productItem):
    productList = []
    productItems = productItem.findAll(name='li')
    for product in productItems:
        productDic = {}
    
        for attr in product.attrs:
            if 'data-device-id' in attr:
                productDic['data-device-id'] = str(attr[1])
            
        spanList = product.findAll(name='span', recursive=False)
        for span in spanList:
            ariaFlag = True
            ariaChecked = None
            ariaDisabled = None
        
            for eachAttr in span.attrs:
                if 'data-device-name' in eachAttr:
                    ariaFlag = False
                    try:
                        productDic['data-device-name'] = str(span.text)
                    except:
                        productDic['data-device-name'] = span.text
                
                if 'data-product' in eachAttr:
                    ariaFlag = False
                    try:
                        productDic['data-product'] = str(span.text)
                    except:
                        productDic['data-product'] = span.text
                
                if 'aria-checked' in eachAttr:
                    if str(eachAttr[1]) == 'false':
                        ariaChecked = False
                    elif str(eachAttr[1]) == 'true':
                        ariaChecked = True    
                    
                if 'aria-disabled' in eachAttr:
                    if str(eachAttr[1]) == 'false':
                        ariaDisabled = False
                    elif str(eachAttr[1]) == 'true':
                        ariaDisabled = True
                        
            if ariaFlag:
                productDic['aria-checked'] = ariaChecked
                productDic['aria-disabled'] = ariaDisabled
            
        #print "Current Product Dictionary = "
        #print productDic
        productList.append(productDic)
    
    return productList
        
ol = soup.findAll(name='ol')

manufacturerList = []
megaManufacturerDic = {}

for item in ol[0].findAll(name='li', recursive=False):
    productList = getProductDictionariesList(item)
    
    manufacturerName = str(item.h3.text)
    if not manufacturerName in manufacturerList:
        manufacturerList.append(manufacturerName)
    
    if not manufacturerName in megaManufacturerDic:
        megaManufacturerDic[manufacturerName] = productList
             
        
#print '------ Mega Dic = -----'
for key,value in megaManufacturerDic.iteritems():
    #print key + ' with %d products:\n' % len(value)
    l = [key]
    for x in value:
        print l + x.values()
        #print x
    
    #print '^'*80   

#print "List of %d Manufacturers:" % len(manufacturerList)
#for x in manufacturerList:
    #print x     