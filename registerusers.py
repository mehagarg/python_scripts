import re,glob,csv
fcsv = csv.writer(open('registeruser.csv','a')) 
fcsv.writerow([str('date_time'),str('ip_sliced'),str('userid'),'result','sId','userSessionId','time','deviceID','screenHeight','screenWidth','clientDevice','clientOS','clientOSVersion','clientVersion','deviceType','countryCode','domain','userHash','filename'])
flst = glob.glob('./*')
for fx in flst:
    print 'Current File : ', fx
    f =open(fx,'r')
    lns=f.readlines()
    for s in lns:
        m = re.search('(method=)(\S+)',s)
        if m:
            if m.group(2) == 'registerUser':
                result = re.search('(result=)(\S+)',s)
                if result.group(2) == 'SUCCESS':
                    
                    date_time = re.search('\S+\s\S+',s)
                    if date_time is None:
                        date_time_value = 'missing value'
                    else:
                        date_time_value = date_time.group()

                    ip = re.search('(from=)(\S+)',s)
                    if ip is None:
                        ip_slice = 'missing value'
                    else:
                        ip_slice=ip.group(2)

                    userId = re.search('(userId=)(\S+)',s)
                    if userId is None:
                        userId_value = 'missing value'
                    else:
                        userId_value=userId.group(2)

                    sId = re.search('(sId=)(\S+)',s)
                    if sId is None:
                        sId_value = 'missing value'
                    else:
                        sId_value =sId.group(2)

                    userSessionId = re.search('(userSessionId=)(\S+)',s)
                    if userSessionId is None:
                        userSessionId_value = 'missing value'
                    else:
                        userSessionId_value=userSessionId.group(2)

                    time = re.search('(time=)(\S+)',s)
                    if time is None:
                        time_value = ''
                    else:
                        time_value=time.group(2)

                    deviceID = re.search('(deviceID=)(\S+)',s)
                    if deviceID is None:
                        deviceID_value = 'missing value'
                    else:
                        deviceID_value=deviceID.group(2)

                    screenHeight = re.search('(screenHeight=)(\S+)',s)  
                    if screenHeight is None:
                        screenHeight_value = 'missing value'
                    else:
                        screenHeight_value=screenHeight.group(2)

                    screenWidth = re.search('(screenWidth=)(\S+)',s)
                    if screenWidth is None:
                        screenWidth_value = 'missing value'
                    else:
                        screenWidth_value=screenWidth.group(2)

                    clientDevice = re.search('(clientDevice=)(\S+)',s)
                    if clientDevice is None:
                        clientDevice_value = 'missing value'
                    else:
                        clientDevice_value=clientDevice.group(2)

                    clientOS = re.search('(clientOS=)(\S+)',s)
                    if clientOS is None:
                        clientOS_value = 'missing value'
                    else:
                        clientOS_value=userId.group(2)

                    clientOSVersion = re.search('(clientOSVersion=)(\S+)',s)
                    if clientOSVersion is None:
                        clientOSVersion_value = 'missing value'
                    else:
                        clientOSVersion_value=clientOSVersion.group(2)

                    clientVersion = re.search('(clientVersion=)(\S+)',s)
                    if clientVersion is None:
                        clientVersion_value = 'missing value'
                    else:
                        clientVersion_value=clientVersion.group(2)

                    deviceType = re.search('(deviceType=)(\S+)',s)
                    if deviceType is None:
                        deviceType_value = 'missing value'
                    else:
                        deviceType_value=deviceType.group(2)

                    countryCode = re.search('(countryCode=)(\S+)',s)
                    if countryCode is None:
                        countryCode_value = 'missing value'
                    else:
                        countryCode_value=countryCode.group(2)

                    domain = re.search('(domain=)(\S+)',s)
                    if domain is None:
                        domain_value = 'missing value'
                    else:
                        domain_value=domain.group(2)

                    userHash = re.search('(userHash=)(\S+)',s)
                    if userHash is None:
                        userHash_value = 'missing value'
                    else:
                        userHash_value=userHash.group(2)

                    fcsv.writerow([date_time_value, ip_slice[:-1], userId_value,result.group(2),sId_value,userSessionId_value,time_value,deviceID_value,screenHeight_value,screenWidth_value,clientDevice_value, clientOS_value, clientOSVersion_value, clientVersion_value, deviceType_value, countryCode_value, domain_value, userHash_value, fx])
    f.close() 
