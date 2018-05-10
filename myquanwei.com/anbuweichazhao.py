#coding=utf-8
import urllib2,sys,time,datetime,os,requests,urllib,re


links2={}
read_file=open("zhengzhuang.txt","a")
readall_file=open("zhengzhuangdetial.txt","a")
webdata={}
firstURL="http://weixin.myquanwei.com/wx/sympOne/1"
readed_file = open("zhengzhuang.txt","r")
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
                data=catalogPageTxt.split("<div class=\"zz_box\">")[1]
                links=data.split("onclick=\"turnHref(\'")
    
                for j in range(1,len(links)):
                        print "j"
                        print j                         
                        data2=links[j].split(")\"")[0]
                        name=links[j].split(">")[1].split("</span")[0]
                        linkaddr="http://weixin.myquanwei.com/wx/sympOnes/"+data2.replace("\',","?sex=")
                        print linkaddr
                        links2[linkaddr]=name
                for link2 in links2.keys():
                        try:
                                cateLogpage2=urllib2.urlopen(link2)        
                        except Exception,e:
                                print 'openERR:'
                                print str(e)
                                pass                                    
                        else:
                                if cateLogpage2:
                                        catalogPage2Txt=cateLogpage2.read()
                                        data3=catalogPage2Txt

                                        links3=data3.split("<li onclick=\"javascript:location.href=\'")
                                        for k in range(1,len(links3)):
                                                link3="http://weixin.myquanwei.com/"+links3[k].split("\'")[0]
                                                name2=links3[k].split("</li>")[0].split(">")[1]
                                                webdata[link3]=link3+" "+link2.split("sex=")[1].replace("1","男").replace("2","女").replace("3","孩")+"->"+links2[link2]+"->>"+name2
                                                read_file.write(webdata[link3]+"\n")
                                                read_file.flush()

                                            
                        
                        pass
        pass
print ""
print "detial start:"
print ""



readall_file.write("性别,部位,病名,地址,简介,病因,症状特点,对症处理,预防护理,饮食宜忌,可能疾病\n".decode('utf-8').encode(sys.getfilesystemencoding()))
readall_file.flush()

print len(webdata.keys())


for weblink in webdata.keys():
        print weblink
        try:   
                #weblink="http://weixin.myquanwei.com/newwx/diseaseDetail/15831?pgcProgramId=gp201301000019"
                detialPage=urllib2.urlopen(weblink)     
                #detialPage=urllib2.urlopen(testurl)          
        except Exception,e:
                print 'openERR:'
                print str(e)
                pass                                    
        else:
                if detialPage:
                        detialPageTxt=detialPage.read()
                        #http://weixin.myquanwei.com/wx/fourPill/101908 中成药->中成药->>祛风剂--[华康]风湿关节炎片
                       
                        #print linedata.decode('utf-8').encode(sys.getfilesystemencoding())
                        xingbie=webdata[weblink].split(" ")[1].split("->")[0]
                        buwei=webdata[weblink].split("->")[1].split("->>")[0]
                        bingming=webdata[weblink].split("->>")[1]
                        dizhi=weblink

                        bref=""
                        if("<div class=\"pro_detail zz_detail  pro_tit disease\">" in detialPageTxt):
                                brief=re.sub(r'\s', '', hr.sub('',(detialPageTxt.split("<div class=\"pro_detail zz_detail  pro_tit disease\">")[1].split("</div>")[0]))).replace(",","，") .strip("\n")
                        
                         
                        bingyin=""
                        zhengzhuangtedian=""
                        duizhengchuli=""
                        yufanghuli=""
                        yinshijinji=""
                        kenengjibing=""
                         
                        #病因,症状特点,对症处理,预防护理,饮食宜忌,可能疾病
                        if("病因</h3>"in detialPageTxt):
                                bingyin=re.sub(r'\s', '', hr.sub('',detialPageTxt.split("病因</h3>")[1].split("</div>")[0])).replace(",","，").strip("\n")
                        if("症状特点</h3>"in detialPageTxt):
                                zhengzhuangtedian=re.sub(r'\s', '', hr.sub('',detialPageTxt.split("症状特点</h3>")[1].split("</div>")[0])).replace(",","，").strip("\n")
                        if("对症处理</h3>"in detialPageTxt):
                                duizhengchuli=re.sub(r'\s', '', hr.sub('',detialPageTxt.split("对症处理</h3>")[1].split("</div>")[0])).replace(",","，").strip("\n")
                        if("预防护理</h3>"in detialPageTxt):
                                yufanghuli=re.sub(r'\s', '', hr.sub('',detialPageTxt.split("预防护理</h3>")[1].split("</div>")[0])).replace(",","，").strip("\n")
                        if("饮食宜忌</h3>"in detialPageTxt):
                                yinshijinji=re.sub(r'\s', '', hr.sub('',detialPageTxt.split("饮食宜忌</h3>")[1].split("</div>")[0])).replace(",","，").strip("\n")
                        
                        link4=weblink.replace("sympThree","sympFour")
                        try:   
                                 
                                detial2Page=urllib2.urlopen(link4)     
                                
                        except Exception,e:
                                print 'openERR:'
                                print str(e)
                                                                     
                        else:
                                if detial2Page:
                                        detial2PageTxt=detial2Page.read()
                                        if("onclick=\"toDiseaseIndex(\'" in detial2PageTxt):
                                                jibings=detial2PageTxt.split("<dl onclick=\"toDiseaseIndex(\'")
                                                for l in range(1,len(jibings)):
                                                        jibingname=re.sub(r'\s', '', hr.sub('',jibings[l].split("<h3>")[1].split("</h3>")[0]))
                                                        jibingdetialinfo=re.sub(r'\s', '', hr.sub('',jibings[l].split("</h3>")[1].split("</dl>")[0]))
                                                        kenengjibing+=jibingname+":"+jibingdetialinfo+"。"
                                                
                                        else:
                                                kenengjibing=detial2PageTxt.split("<div class=\"wjl\">")[1].split("</div>")[0]
                                        kenengjibing=kenengjibing.replace("。。","。").replace(",","，").strip("\n")
                             

                        
 
                        #print  (fenlei1+","+fenlei2+","+dizhi+","+title+","+brief+","+bingyin+","+bingyinDetial+","+jibingtedian+","+jibingtedianDetial+","+yihunxiaojibing+","+yihunxiaojibingDetial+","+helishenghuoxiguan+","+helishenghuoxiguanDetial+zufangyuanze+"\n").decode('utf-8').encode(sys.getfilesystemencoding())
                        #APP_KEY =raw_input("input the APP_KEY(check at http://open.weibo.com/apps/   you can change this code yourself): ")
                        readall_file.write((xingbie+","+buwei+","+bingming+","+dizhi+","+brief+","+bingyin+","+zhengzhuangtedian+","+duizhengchuli+","+yufanghuli+","+yinshijinji+","+kenengjibing+"\n").decode('utf-8').encode(sys.getfilesystemencoding()))
                        readall_file.flush()
                        
        pass

readall_file.close()
