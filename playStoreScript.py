from BeautifulSoup import BeautifulSoup as BS
soup = BS(open('garmin.txt'))

manufacturerList = []

megaManufacturerDic = {}
manufacturerName = str(soup.h3.text)
if not manufacturerName in manufacturerList:
    manufacturerList.append(manufacturerName)
    
    if not manufacturerName in megaManufacturerDic:
        megaManufacturerDic[manufacturerName] = []

#dic['data-manufacturer-group'] = str(soup.h3.text)

productList = soup.ol.findAll(name='li')
for product in productList:
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
                productDic['data-device-name'] = span.text
                
            if 'data-product' in eachAttr:
                ariaFlag = False
                productDic['data-product'] = str(span.text)
                
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
            
    print "Current Product Dictionary = "
    print productDic
    
    megaManufacturerDic[manufacturerName].append(productDic)
    
print 'Mega Dic = '
print megaManufacturerDic
        