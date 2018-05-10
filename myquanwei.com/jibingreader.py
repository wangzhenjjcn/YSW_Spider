#coding=utf-8
import urllib2,sys,time,datetime,os,requests,urllib,re


 

read_file=open("readedDisease.txt","a")
readall_file=open("readedDiseasedetial.txt","a")
webdata={}
firstURL="http://weixin.myquanwei.com/newwx/commonDisease"
readed_file = open("readedDisease.txt","r")
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
                data=catalogPageTxt.split("<div class=\"twoPill\"")[1].split("</div>")[0]
                links=data.split("<dl>")
                for j in range(1,len(links)):
                        print "j"
                        print j
                        name=links[j].split("</dt>")[0].split("<dt>")[1]
                        print "name:"
                        print name.decode('utf-8').encode(sys.getfilesystemencoding())
                        data2=links[j].split("<dd")[1].split("</dd>")[0].split("<p onclick=\"toDiseaseIndex(\'")
                        for k in range(1,len(data2)):
                                if(">" in data2[k]):
                                        print "k"
                                        print k
                                        name2=data2[k].split(">")[1].split("</p")[0]
                                        print name2.decode('utf-8').encode(sys.getfilesystemencoding())
                                        link2="http://weixin.myquanwei.com/newwx/diseaseDetail/"+data2[k].split("\',")[0]
                                        print link2
                                        webdata[link2]=name+"->"+name2
                                        print (name+"->"+name2).decode('utf-8').encode(sys.getfilesystemencoding())
                                        read_file.write(link2+" "+name+"->"+name2+"\n")
                                        read_file.flush()
        pass
print ""
print "detial start:"
print ""



readall_file.write("类别1,类别2,地址,名称,简介,病因,病因详情,疾病特点,疾病特点详情,易混淆疾病,易混淆疾病详情,治疗原则,治疗原则详情,合理生活习惯,合理生活习惯详情,组方原则\n".decode('utf-8').encode(sys.getfilesystemencoding()))
readall_file.flush()

print len(webdata.keys())


for weblink in webdata.keys():
        print weblink
        try:   
                #testurl="http://weixin.myquanwei.com/newwx/diseaseDetail/0101"
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
                        dizhi=weblink
                        #print linedata.decode('utf-8').encode(sys.getfilesystemencoding())
                        fenlei1=linedata.strip("\n").split("->")[0]
                        fenlei2=linedata.strip("\n").split("->")[1]
                        detialPageTxt=detialPage.read()
                        title=re.sub(r'\s', '', hr.sub('',(detialPageTxt.split("<h3>")[1].split("</h3>")[0]))).replace(",","，") .strip("\n")
                        brief=re.sub(r'\s', '', hr.sub('',(detialPageTxt.split("</h3>")[1].split("</p>")[0]))).replace(",","，") .strip("\n")
                        #print title.decode('utf-8').encode(sys.getfilesystemencoding())
                        #print brief.decode('utf-8').encode(sys.getfilesystemencoding())
                       
                        bingyin=""
                        bingyinDetial=""
                        jibingtedian=""
                        jibingtedianDetial=""
                        yihunxiaojibing=""
                        yihunxiaojibingDetial=""
                        zhiliaoyuanze=""
                        zhiliaoyuanzeDetial=""
                        helishenghuoxiguan=""
                        helishenghuoxiguanDetial=""
                        zufangyuanze=""
                         
                        if("病因</h3>"in detialPageTxt):
                                #bingyin=detialPageTxt.split("病因</h3>")[1].split("</div>")[0].split("id=\"")[1].split("\">")[0]
                                bingyinid=detialPageTxt.split("病因</h3>")[1].split("</div>")[0].split("id=\"")[1].split("\">")[0]
                                try:   
                                        bingyinurl="http://weixin.myquanwei.com/newwx/diseaseSkip/"+weblink.split("diseaseDetail/")[1]+"/"+bingyinid
                                        #print bingyinurl
                                        bingyinDetialPage=urllib2.urlopen(bingyinurl)          
                                except Exception,e:
                                        print 'openERR:'
                                        print str(e)
                                                                             
                                else:
                                        if bingyinDetialPage:
                                                
                                                bingyinDetialPageTxt=bingyinDetialPage.read()
                                                if("</p>" in bingyinDetialPageTxt):
                                                        bingyin=re.sub(r'\s', '', hr.sub('',bingyinDetialPageTxt.split("<p>")[1].split("</p>")[0])).replace(",","，") .strip("\n")
                                                        #print bingyin.decode('utf-8').encode(sys.getfilesystemencoding())
                                                        bingyinDetial=re.sub(r'\s', '', hr.sub('',bingyinDetialPageTxt.split("</p>")[1].split("</p>")[0])).replace(",","，") .strip("\n")
                                                        #print bingyinDetial.decode('utf-8').encode(sys.getfilesystemencoding())
                                                else:
                                                        bingyin=re.sub(r'\s', '', hr.sub('',bingyinDetialPageTxt))
                                                        bingyinDetial=re.sub(r'\s', '', hr.sub('',bingyinDetialPageTxt))
                                                


                               
                        if("疾病特点</h3>"in detialPageTxt):
                                jibingtedianid=detialPageTxt.split("疾病特点</h3>")[1].split("</div>")[0].split("id=\"")[1].split("\">")[0]
                                try:   
                                        jibingtedianurl="http://weixin.myquanwei.com/newwx/diseaseSkip/"+weblink.split("diseaseDetail/")[1]+"/"+jibingtedianid
                                        #print jibingtedianurl
                                        jibingtedianDetialPage=urllib2.urlopen(jibingtedianurl)          
                                except Exception,e:
                                        print 'openERR:'
                                        print str(e)
                                                                             
                                else:
                                        if jibingtedianDetialPage:
                                                jibingtedianDetialPageTxt=jibingtedianDetialPage.read()
                                                if("</p>" in jibingtedianDetialPageTxt):
                                                        jibingtedian=re.sub(r'\s', '', hr.sub('',jibingtedianDetialPageTxt.split("<p>")[1].split("</p>")[0])).replace(",","，") .strip("\n")
                                                        #print jibingtedian.decode('utf-8').encode(sys.getfilesystemencoding())
                                                        jibingtedianDetial=re.sub(r'\s', '', hr.sub('',jibingtedianDetialPageTxt.split("</p>")[1].split("</p>")[0])).replace(",","，") .strip("\n")
                                                        #print jibingtedianDetial.decode('utf-8').encode(sys.getfilesystemencoding())
                                                else:
                                                        jibingtedian=re.sub(r'\s', '', hr.sub('',jibingtedianDetialPageTxt))
                                                        jibingtedianDetial=re.sub(r'\s', '', hr.sub('',jibingtedianDetialPageTxt))
                        
                        if("易混淆疾病</h3>"in detialPageTxt):
                                yihunxiaojibingid=detialPageTxt.split("易混淆疾病</h3>")[1].split("</div>")[0].split("id=\"")[1].split("\">")[0]
                                try:   
                                        yihunxiaojibingurl="http://weixin.myquanwei.com/newwx/diseaseSkip/"+weblink.split("diseaseDetail/")[1]+"/"+yihunxiaojibingid
                                        #print yihunxiaojibingurl
                                        yihunxiaojibingDetialPage=urllib2.urlopen(yihunxiaojibingurl)          
                                except Exception,e:
                                        print 'openERR:'
                                        print str(e)
                                                                             
                                else:
                                        if yihunxiaojibingDetialPage:
                                                yihunxiaojibingDetialPageTxt=yihunxiaojibingDetialPage.read()
                                                if("</p>" in yihunxiaojibingDetialPageTxt):
                                                        yihunxiaojibing=re.sub(r'\s', '', hr.sub('',yihunxiaojibingDetialPageTxt.split("<p>")[1].split("</p>")[0])).replace(",","，") .strip("\n")
                                                        #print yihunxiaojibing.decode('utf-8').encode(sys.getfilesystemencoding())
                                                        yihunxiaojibingDetial=re.sub(r'\s', '', hr.sub('',yihunxiaojibingDetialPageTxt.split("</div>")[0].replace(",","，").replace("</h4>",">>").replace("</p>","。").replace("</a>","、").replace("<span>","·"))).replace(",","，") .strip("\n")
                                                        #print yihunxiaojibingDetial.decode('utf-8').encode(sys.getfilesystemencoding())
                                                else:
                                                        yihunxiaojibing=re.sub(r'\s', '', hr.sub('',yihunxiaojibingDetialPageTxt))
                                                        yihunxiaojibingDetial=re.sub(r'\s', '', hr.sub('',yihunxiaojibingDetialPageTxt))
                        if("治疗原则</h3>"in detialPageTxt):
                                zhiliaoyuanzeid=detialPageTxt.split("治疗原则</h3>")[1].split("</div>")[0].split("id=\"")[1].split("\">")[0]
                                try:   
                                        zhiliaoyuanzeurl="http://weixin.myquanwei.com/newwx/diseaseSkip/"+weblink.split("diseaseDetail/")[1]+"/"+zhiliaoyuanzeid
                                        #print zhiliaoyuanzeurl
                                        zhiliaoyuanzeDetialPage=urllib2.urlopen(zhiliaoyuanzeurl)          
                                except Exception,e:
                                        print 'openERR:'
                                        print str(e)
                                                                             
                                else:
                                        if zhiliaoyuanzeDetialPage:
                                                zhiliaoyuanzeDetialPageTxt=zhiliaoyuanzeDetialPage.read()
                                                if("</p>" in zhiliaoyuanzeDetialPageTxt):
                                                        zhiliaoyuanze=re.sub(r'\s', '', hr.sub('',zhiliaoyuanzeDetialPageTxt.split("<p>")[1].split("</p>")[0])).replace(",","，") .strip("\n")
                                                        #print zhiliaoyuanze.decode('utf-8').encode(sys.getfilesystemencoding())
                                                        zhiliaoyuanzeDetial=re.sub(r'\s', '', hr.sub('',zhiliaoyuanzeDetialPageTxt.split("</p>")[1].split("</p>")[0])).replace(",","，") .strip("\n")
                                                        #print zhiliaoyuanzeDetial.decode('utf-8').encode(sys.getfilesystemencoding())
                                                else:
                                                        zhiliaoyuanze=re.sub(r'\s', '', hr.sub('',zhiliaoyuanzeDetialPageTxt))
                                                        zhiliaoyuanzeDetial=re.sub(r'\s', '', hr.sub('',zhiliaoyuanzeDetialPageTxt))
                        if("合理生活习惯</h3>"in detialPageTxt):
                                helishenghuoxiguanid=detialPageTxt.split("合理生活习惯</h3>")[1].split("</div>")[0].split("id=\"")[1].split("\">")[0]
                                try:   
                                        helishenghuoxiguanurl="http://weixin.myquanwei.com/newwx/diseaseSkip/"+weblink.split("diseaseDetail/")[1]+"/"+helishenghuoxiguanid
                                        print helishenghuoxiguanurl
                                        helishenghuoxiguanDetialPage=urllib2.urlopen(helishenghuoxiguanurl)          
                                except Exception,e:
                                        print 'openERR:'
                                        print str(e)
                                                                             
                                else:
                                        if helishenghuoxiguanDetialPage:
                                                helishenghuoxiguanDetialPageTxt=helishenghuoxiguanDetialPage.read()
                                                if("</p>" in helishenghuoxiguanDetialPageTxt):
                                                        helishenghuoxiguan=re.sub(r'\s', '', hr.sub('',helishenghuoxiguanDetialPageTxt.split("<p>")[1].split("</p>")[0])).replace(",","，") .strip("\n")
                                                        #print helishenghuoxiguan.decode('utf-8').encode(sys.getfilesystemencoding())
                                                        helishenghuoxiguanDetial=re.sub(r'\s', '', hr.sub('',helishenghuoxiguanDetialPageTxt.split("</p>")[1].split("</p>")[0])).replace(",","，") .strip("\n")
                                                        #print helishenghuoxiguanDetial.decode('utf-8').encode(sys.getfilesystemencoding())
                                                else:
                                                        helishenghuoxiguan=re.sub(r'\s', '', hr.sub('',helishenghuoxiguanDetialPageTxt))
                                                        helishenghuoxiguanDetial=re.sub(r'\s', '', hr.sub('',helishenghuoxiguanDetialPageTxt))
                        
                        
                        zufang=detialPageTxt.split("<div class=\"zl\">")
                        for i in range(1,len(zufang)):
                                zufangi=zufang[i].split("</div>")[0].replace(",","，").replace("</h4>",":").replace("</p>","。").replace("</a>","、").replace("<h4>","·")
                                zufangyuanze+=re.sub(r'\s', '', hr.sub('',zufangi))
                        #print zufangyuanze.decode('utf-8').encode(sys.getfilesystemencoding())
                        
                        
                   
                        #print  (fenlei1+","+fenlei2+","+dizhi+","+title+","+brief+","+bingyin+","+bingyinDetial+","+jibingtedian+","+jibingtedianDetial+","+yihunxiaojibing+","+yihunxiaojibingDetial+","+helishenghuoxiguan+","+helishenghuoxiguanDetial+zufangyuanze+"\n").decode('utf-8').encode(sys.getfilesystemencoding())
                        readall_file.write((fenlei1.replace(",","，") .strip("\n")+","+fenlei2.replace(",","，") .strip("\n")+","+dizhi.replace(",","，") .strip("\n")+","+title.replace(",","，") .strip("\n")+","+brief.replace(",","，") .strip("\n")+","+bingyin.replace(",","，") .strip("\n")+","+bingyinDetial.replace(",","，") .strip("\n")+","+jibingtedian.replace(",","，") .strip("\n")+","+jibingtedianDetial.replace(",","，") .strip("\n")+","+yihunxiaojibing.replace(",","，") .strip("\n")+","+yihunxiaojibingDetial.replace(",","，") .strip("\n")+","+helishenghuoxiguan.replace(",","，") .strip("\n")+","+helishenghuoxiguanDetial+zufangyuanze.replace(",","，") .strip("\n")+"\n").strip("？").decode('utf-8').encode(sys.getfilesystemencoding()))
                        readall_file.flush()
                        
        pass

readall_file.close()