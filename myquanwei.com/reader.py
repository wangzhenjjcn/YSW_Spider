#coding=utf-8
import urllib2,sys,time,datetime,os,requests,urllib,re


 

read_file=open("readed.txt","a")
readall_file=open("readeddetial.txt","a")
webdata={}
firstURL="http://weixin.myquanwei.com/wx/onePill"
readed_file = open("readed.txt","r")
for lines in readed_file:
        data = lines.strip("\n").split(" ")[0]
        webdata[data]=lines
     
hdr = {
        'Host':"weixin.myquanwei.com",
       'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36",
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'gzip, deflate, br',
       'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
       'Connection': 'keep-alive',
       'cookie':"huaweielbsession=f67b5926a5b4f89e69c69caa1abc9931; __jsluid=67afc29719df7db3211ded2f8039a7ce; UM_distinctid=16308260a0b657-0f261135daea6-39614101-1fa400-16308260a0d4ab; ASP.NET_SessionId=pcmoudz4fg2yvi0vmcdbppgu; subcatalogflag_ssl=1; hotkeywords=%E6%8B%9C%E9%98%BF%E5%8F%B8%E5%8C%B9%E7%81%B5%23%231%23%23med%23%23%24%23%23medicine-584398.html%23%23%24%40%40%E8%A1%A5%E8%A1%80%23%231%23%23wwwsearch%23%23%24%23%23search.html%23%23keyword%3D%25e8%25a1%25a5%25e8%25a1%2580%40%40999%23%230%23%23other_https%3A%2F%2Fwww.yaofangwang.com%2Fsearch%2F13791.html%40%40%E7%89%87%E4%BB%94%E7%99%80%23%231%23%23other_https%3A%2F%2Fwww.yaofangwang.com%2Fsearch%2F39735.html%40%40%E5%A6%88%E5%AF%8C%E9%9A%86%23%230%23%23wwwsearch%23%23%24%23%23search.html%23%23keyword%3D%25e5%25a6%2588%25e5%25af%258c%25e9%259a%2586%40%40%E9%98%BF%E8%83%B6%23%231%23%23other_https%3A%2F%2Fwww.yaofangwang.com%2Fsearch%2F11442.html%40%40%E9%87%91%E6%88%88%23%230%23%23other_https%3A%2F%2Fwww.yaofangwang.com%2Fsearch%2F30642.html%40%40%E6%B1%A4%E8%87%A3%E5%80%8D%E5%81%A5%23%230%23%23other_https%3A%2F%2Fwww.yaofangwang.com%2Fsearch%2F50493.html; Hm_lvt_e5f454eb1aa8e839f8845470af4667eb=1524850101; cartcount=0; historysearch=; CNZZDATA1261831897=1577417923-1524847327-null%7C1524852728; Hm_lpvt_e5f454eb1aa8e839f8845470af4667eb=1524852782; topnavflag_ssl=1"
       }

hr = re.compile(r'<[^>]+>',re.S)
























try:   
        cateLogpage=urllib2.urlopen(firstURL)        
except Exception,e:
        print 'openERR:'
        print str(e)
        pass                                    
else:
        if cateLogpage:
                catalogPageTxt=cateLogpage.read()
                data=catalogPageTxt
                links=data.split("<dl onclick=\"gotoNext(\'")
                cateLogpageLinks={}
                cateLogpageLinks3={}
                detialPageLinks={}
                for i in range(1,len(links)):
                        link="http://weixin.myquanwei.com/wx/twoPill/"+links[i].split("\')")[0]
                        name=links[i].split("<dd>")[1].split("</dd>")[0]
                        cateLogpageLinks[link]=name;
                print cateLogpageLinks
                for cateLogpageLink in cateLogpageLinks.keys():
                        try:
                                cateLogpage2=urllib2.urlopen(cateLogpageLink)        
                        except Exception,e:
                                print 'openERR:'
                                print str(e)
                                pass                                    
                        else:
                                if cateLogpage2:
                                        print cateLogpageLink
                                        catalogPage2Txt=cateLogpage2.read()
                                        data2=catalogPage2Txt.split("<div class=\"twoPill\">")[1].split("</div>")[0]
                                        links2=data2.split("<dl>")
                                        for j in range(1,len(links2)):
                                                print "j"
                                                print j
                                                name2=links2[j].split("<span>")[0].split(">")[1]
                                                print "name2:"
                                                print name2.decode('utf-8').encode(sys.getfilesystemencoding())
                                                data3=links2[j].split("<dd")[1].split("</dd>")[0].split("<p onclick=\"toNext(\'")
                                                
                                                for k in range(1,len(data3)):
                                                        if(">" in data3[k]):
                                                                print "k"
                                                                print k
                                                                name3=data3[k].split(">")[1].split("</p")[0]
                                                                print name3.decode('utf-8').encode(sys.getfilesystemencoding())
                                                                link3="http://weixin.myquanwei.com/wx/threePill/"+data3[k].split("\')")[0]
                                                                print link3
                                                                cateLogpageLinks3[link3]=cateLogpageLinks[cateLogpageLink]+"->"+name2+"->>"+name3
                                                                print (cateLogpageLinks[cateLogpageLink]+"->"+name2+"->>"+name3).decode('utf-8').encode(sys.getfilesystemencoding())
                        pass
                print ""
                print "ListPage start:"
                print ""
                for cateLogpageLink3 in cateLogpageLinks3.keys():
                        try:
                                listPage=urllib2.urlopen(cateLogpageLink3)        
                        except Exception,e:
                                print 'openERR:'
                                print str(e)
                                pass                                    
                        else:
                                if listPage:
                                        print cateLogpageLink3
                                        print cateLogpageLinks3[cateLogpageLink3].decode('utf-8').encode(sys.getfilesystemencoding())
                                        listPageTxt=listPage.read()
                                        listPageTxt=listPageTxt.split("<div id=\"classifyProduct\">")[1]
                                        hasNextPage=listPageTxt.split("value=\"")[1].split("\" id=\"hasNextPage\"")[0]
                                        parentId=listPageTxt.split("id=\"hasNextPage\"")[1].split("value=\"")[1].split("\" id=\"parentId\"")[0]
                                        currPage=listPageTxt.split("id=\"parentId\"")[1].split("value=\"")[1].split("\" id=\"currPage\"")[0].strip(",").strip(",".decode('utf-8').encode(sys.getfilesystemencoding()))
                                        totalPages=listPageTxt.split("id=\"currPage\"")[1].split("value=\"")[1].split("\" id=\"totalPages\"")[0].strip(",").strip(",".decode('utf-8').encode(sys.getfilesystemencoding()))
                                        print ""
                                        print hasNextPage
                                        print parentId
                                        print currPage
                                        print totalPages
                                        print ""
                                        data4=listPageTxt.split("<div class=\"sp_list\"  onclick=\"toProductDetail(\'")
                                        print len(data4)
                                        for o in range(1,len(data4)):
                                                print "o:"
                                                print o
                                                name4=data4[o].split("<p class=\"sp_tit\">")[1].split("</p>")[0]
                                                print "name4:"
                                                print name4.decode('utf-8').encode(sys.getfilesystemencoding())
                                                link4="http://weixin.myquanwei.com/wx/fourPill/"+data4[o].split("\')")[0]
                                                detialPageLinks[link4]=name4
                                                webdata[link4]=link4+" "+cateLogpageLinks3[cateLogpageLink3]+"--"+name4+"\n"
                                                read_file.write(link4+" "+cateLogpageLinks3[cateLogpageLink3]+"--"+name4+"\n")
                                                read_file.flush()
                                        if(hasNextPage=="Y"):   
                                                print  "++++++++++++++++totalPages:"+totalPages                                  
                                                for x in range(int(currPage),999999):
                                                        postData = {'hasNextPage':'Y','currPage':x,'parentId':parentId,'url':'/wx/threePill'}
                                                        postData_urlencode = urllib.urlencode(postData)
                                                        requrl = "http://weixin.myquanwei.com/wx/threePill"
                                                        req = urllib2.Request(url = requrl,data =postData_urlencode)
                                                        res_data = urllib2.urlopen(req)
                                                        res = res_data.read()
                                                        data5=res.split("<div class=\\\"sp_list\\\"  onclick=\\\"toProductDetail(\'")
                                                        currPage2=res.split("currPage\":")[1].split(",")[0]
                                                        hasNextPage2=res.split("\"hasNextPage\":\"")[1].split("\"")[0]
                                                        print "currPage2:"+ currPage2+"   hasNextPage2:"+hasNextPage2+" totalPage:"+totalPages
                                                        print len(data5)
                                                        for q in range(1,len(data5)):
                                                                print "o:"+bytes(o) +"q:"+bytes(q)  
                                                        
                                                                name5=data5[q].split("<p class=\\\"sp_tit\\\">")[1].split("</p>")[0]
                                                                print "name5:"
                                                                print name5.decode('utf-8').encode(sys.getfilesystemencoding())
                                                                link5="http://weixin.myquanwei.com/wx/fourPill/"+data5[q].split("\')")[0]
                                                                detialPageLinks[link5]=name5
                                                                webdata[link5]=link5+" "+cateLogpageLinks3[cateLogpageLink3]+"--"+name5+"\n"
                                                                read_file.write(link5+" "+cateLogpageLinks3[cateLogpageLink3]+"--"+name5+"\n")
                                                                read_file.flush()
                                                        if(hasNextPage2!="Y"):
                                                                break
                                                                 
                
        pass




read_file.close()





readall_file.write("类别1,类别2,类别3,地址,名称,类型,型号,生产厂家,功能主治,用法用量,不良反应,使用禁忌提示,使用注意,孕妇及哺乳妇女使用注意,儿童使用注意,老年人使用注意,药物相互作用,用药小知识,适用范围,使用方法\n".decode('utf-8').encode(sys.getfilesystemencoding()))
readall_file.flush()

for weblink in webdata.keys():
        print weblink
        try:   
                #testurl="http://weixin.myquanwei.com/wx/fourPill/146293"
                detialPage=urllib2.urlopen(weblink)     
                #detialPage=urllib2.urlopen(testurl)          
        except Exception,e:
                print 'openERR:'
                print str(e)
                pass                                    
        else:
                if detialPage:
                        linedata=webdata[weblink]
                        #http://weixin.myquanwei.com/wx/fourPill/101908 中成药->中成药->>祛风剂--[华康]风湿关节炎片
                        fenlei1=linedata.strip("\n").split(" ")[1].split("->")[0]
                        fenlei2=linedata.strip("\n").split("->")[1].split("->>")[0]
                        fenlei3=linedata.strip("\n").split("->>")[1].split("--")[0]
                        dizhi=linedata.strip("\n").split(" ")[0]
                        detialPageTxt=detialPage.read()
                        title=re.sub(r'\s', '', hr.sub('',(detialPageTxt.split("<h3>")[1].split("</h3>")[0])))
                        title=re.sub(r'\s', '', hr.sub('',title)) .replace(",","，") .strip("\n")
                        form1=detialPageTxt.split("<div class=\"pro_tit\">")[1].split("</ul>")[0]
                        form1List=form1.split("<li>")      
                        leibie=re.sub(r'\s', '', hr.sub('',form1List[1])) 
                        leibie=re.sub(r'\s', '', hr.sub('',leibie)) .replace(",","，") .strip("\n")
                        guige=form1List[2].split("<")[0].strip("/n").strip(" ")
                        guige=re.sub(r'\s', '', hr.sub('',guige)) .replace(",","，") .strip("\n")
                        changjia=form1List[3].split("<")[0].strip("/n").strip(" ")
                        changjia=re.sub(r'\s', '', hr.sub('',changjia)) .replace(",","，") .strip("\n")
                        gongenngzhuzhi=""
                        yongfayongliang=""
                        buliangfanying=""
                        shiyongjinjitishi=""
                        shiyongzhuyi=""
                        yunfujiburufunvshiyongzhuyi=""
                        ertongshiyongzhuyi=""
                        laonianrenshiyongzhuyi=""
                        yaowuxianghuzuoyong=""
                        yongyaoxiaozhishi=""
                        shiyongfanwei=""
                        shiyongfangfa=""
 
                        if("功能主治</h3>"in detialPageTxt):
                                gongenngzhuzhi=re.sub(r'\s', '', hr.sub('',detialPageTxt.split("功能主治</h3>")[1].split("</div>")[0])).replace(",","，") .strip("\n")
                        if("适应症</h3>"in detialPageTxt):
                                gongenngzhuzhi=re.sub(r'\s', '', hr.sub('',detialPageTxt.split("适应症</h3>")[1].split("</div>")[0])).replace(",","，") .strip("\n")
                                #print  gongenngzhuzhi.decode('utf-8').encode(sys.getfilesystemencoding())
                        if("用法用量</h3>"in detialPageTxt):
                                yongfayongliang=re.sub(r'\s', '', hr.sub('',detialPageTxt.split("用法用量</h3>")[1].split("</div>")[0])) .replace(",","，").strip("\n")
                                #print yongfayongliang.decode('utf-8').encode(sys.getfilesystemencoding())
                        if("不良反应</h3>"in detialPageTxt):
                                buliangfanying=re.sub(r'\s', '', hr.sub('',detialPageTxt.split("不良反应</h3>")[1].split("</div>")[0])) .replace(",","，").strip("\n")
                                #print buliangfanying.decode('utf-8').encode(sys.getfilesystemencoding())
                        if("使用禁忌提示</h3>"in detialPageTxt):
                                shiyongjinjitishi=re.sub(r'\s', '', hr.sub('',detialPageTxt.split("使用禁忌提示</h3>")[1].split("</div>")[0])) .replace(",","，").strip("\n")
                                #print shiyongjinjitishi.decode('utf-8').encode(sys.getfilesystemencoding())
                        if("使用注意</h3>"in detialPageTxt):
                                shiyongzhuyi=re.sub(r'\s', '', hr.sub('',detialPageTxt.split("使用注意</h3>")[1].split("</div>")[0])) .replace(",","，").strip("\n")
                                #print shiyongzhuyi.decode('utf-8').encode(sys.getfilesystemencoding())
                        if("孕妇及哺乳妇女使用注意</h3>"in detialPageTxt):
                                yunfujiburufunvshiyongzhuyi=re.sub(r'\s', '', hr.sub('',detialPageTxt.split("孕妇及哺乳妇女使用注意</h3>")[1].split("</div>")[0])) .replace(",","，").strip("\n")
                                #print yunfujiburufunvshiyongzhuyi.decode('utf-8').encode(sys.getfilesystemencoding())
                        if("儿童使用注意</h3>"in detialPageTxt):
                                ertongshiyongzhuyi=re.sub(r'\s', '', hr.sub('',detialPageTxt.split("儿童使用注意</h3>")[1].split("</div>")[0])) .replace(",","，").strip("\n")
                                #print ertongshiyongzhuyi.decode('utf-8').encode(sys.getfilesystemencoding())
                        if("老年人使用注意</h3>"in detialPageTxt):
                                laonianrenshiyongzhuyi=re.sub(r'\s', '', hr.sub('',detialPageTxt.split("老年人使用注意</h3>")[1].split("</div>")[0])) .replace(",","，").strip("\n")
                                #print laonianrenshiyongzhuyi.decode('utf-8').encode(sys.getfilesystemencoding())
                        if("药物相互作用</h3>"in detialPageTxt):
                                yaowuxianghuzuoyong=re.sub(r'\s', '', hr.sub('',detialPageTxt.split("药物相互作用</h3>")[1].split("</div>")[0])) .replace(",","，").strip("\n")
                                #print yaowuxianghuzuoyong.decode('utf-8').encode(sys.getfilesystemencoding())
                        if("用药小知识</h3>"in detialPageTxt):
                                yongyaoxiaozhishi=re.sub(r'\s', '', hr.sub('',detialPageTxt.split("用药小知识</h3>")[1].split("</div>")[0])) .replace(",","，").strip("\n")
                                #print yongyaoxiaozhishi.decode('utf-8').encode(sys.getfilesystemencoding())
                        if("适用范围</h3>"in detialPageTxt):
                                shiyongfanwei=re.sub(r'\s', '', hr.sub('',detialPageTxt.split("适用范围</h3>")[1].split("</div>")[0])) .replace(",","，").strip("\n")
                                #print shiyongfanwei.decode('utf-8').encode(sys.getfilesystemencoding())
                        if("使用方法</h3>"in detialPageTxt):
                                shiyongfangfa=re.sub(r'\s', '', hr.sub('',detialPageTxt.split("使用方法</h3>")[1].split("</div>")[0])) .replace(",","，").strip("\n")
                                #print shiyongfangfa.decode('utf-8').encode(sys.getfilesystemencoding())
                        print title.decode('utf-8').encode(sys.getfilesystemencoding())
                        readall_file.write((fenlei1+","+fenlei2+","+fenlei3+","+dizhi+","+title+","+leibie+","+guige+","+changjia+","+gongenngzhuzhi+","+yongfayongliang+","+buliangfanying+","+shiyongjinjitishi+","+shiyongzhuyi+","+yunfujiburufunvshiyongzhuyi+","+ertongshiyongzhuyi+","+laonianrenshiyongzhuyi+","+yaowuxianghuzuoyong+","+yongyaoxiaozhishi+","+shiyongfanwei+","+shiyongfangfa+"\n").decode('utf-8').encode(sys.getfilesystemencoding()))
                        readall_file.flush()
                        #CALL_BACK =raw_input("input the CALL_BACK address (if dont know,you can use this :https://api.weibo.com/oauth2/default.html) : ")
        pass

readall_file.close()