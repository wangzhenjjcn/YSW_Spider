#coding=utf-8
import urllib2,sys,time,datetime,os,requests,urllib,re


 

read_file=open("diseaseBaike.txt","a")
readall_file=open("diseaseBaikedetial.txt","a")
webdata={}
firstURL="http://weixin.myquanwei.com/newwx/diseaseBaike"
readed_file = open("diseaseBaike.txt","r")
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
                data=catalogPageTxt.split("<div class=\"wrap_box\">")[1].split("<li onclick=\"scrollTo(\'Z\');\">Z</li>")[0]
                links=data.split("<li onclick=\"toDiseaseDetail(\'")
                for j in range(1,len(links)):
                        print "j"
                        print j
                        name=links[j].split("</li>")[0].split(">")[1]
                        print "name:"
                        print name.decode('utf-8').encode(sys.getfilesystemencoding())
                        link="http://weixin.myquanwei.com/newwx/diseaseDetail/"+links[j].split("\')")[0].replace("\',\'","?pgcProgramId=")
                        print link
                        webdata[link]=name
                        read_file.write(link+" "+name+"\n")
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
                #weblink="http://weixin.myquanwei.com/newwx/diseaseDetail/15831?pgcProgramId=gp201301000019"
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
                        fenlei1=""
                        fenlei2=""
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
                                bingyin=re.sub(r'\s', '', hr.sub('',detialPageTxt.split("病因</h3>")[1].split("</div>")[0]))
                        if("疾病特点</h3>"in detialPageTxt):
                                jibingtedian=re.sub(r'\s', '', hr.sub('',detialPageTxt.split("疾病特点</h3>")[1].split("</div>")[0]))
                        if("易混淆疾病</h3>"in detialPageTxt):
                                yihunxiaojibing=re.sub(r'\s', '', hr.sub('',detialPageTxt.split("易混淆疾病</h3>")[1].split("</div>")[0]))
                        if("治疗原则</h3>"in detialPageTxt):
                                zhiliaoyuanze=re.sub(r'\s', '', hr.sub('',detialPageTxt.split("治疗原则</h3>")[1].split("</div>")[0]))
                        if("合理生活习惯</h3>"in detialPageTxt):
                                helishenghuoxiguan=re.sub(r'\s', '', hr.sub('',detialPageTxt.split("合理生活习惯</h3>")[1].split("</div>")[0]))
                        
                        
                        if("组方"in detialPageTxt and "<div class=\"zl\">"in detialPageTxt):
                                zufang=detialPageTxt.split("<div class=\"zl\">")
                                for i in range(1,len(zufang)):
                                        zufangi=zufang[i].split("</div>")[0].replace(",","，").replace("</h4>",":").replace("</p>","。").replace("</a>","、").replace("<h4>","·")
                                        zufangyuanze+=re.sub(r'\s', '', hr.sub('',zufangi))
                        #print zufangyuanze.decode('utf-8').encode(sys.getfilesystemencoding())
                        
                        
                   
                        #print  (fenlei1+","+fenlei2+","+dizhi+","+title+","+brief+","+bingyin+","+bingyinDetial+","+jibingtedian+","+jibingtedianDetial+","+yihunxiaojibing+","+yihunxiaojibingDetial+","+helishenghuoxiguan+","+helishenghuoxiguanDetial+zufangyuanze+"\n").decode('utf-8').encode(sys.getfilesystemencoding())
                        #APP_KEY =raw_input("input the APP_KEY(check at http://open.weibo.com/apps/   you can change this code yourself): ")
                        readall_file.write((fenlei1.replace(",","，") .strip("\n")+","+fenlei2.replace(",","，") .strip("\n")+","+dizhi.replace(",","，") .strip("\n")+","+title.replace(",","，") .strip("\n")+","+brief.replace(",","，") .strip("\n")+","+bingyin.replace(",","，") .strip("\n")+","+bingyinDetial.replace(",","，") .strip("\n")+","+jibingtedian.replace(",","，") .strip("\n")+","+jibingtedianDetial.replace(",","，") .strip("\n")+","+yihunxiaojibing.replace(",","，") .strip("\n")+","+yihunxiaojibingDetial.replace(",","，") .strip("\n")+","+helishenghuoxiguan.replace(",","，") .strip("\n")+","+helishenghuoxiguanDetial+zufangyuanze.replace(",","，") .strip("\n")+"\n").strip("？").decode('utf-8').encode(sys.getfilesystemencoding()))
                        readall_file.flush()
                        
        pass

readall_file.close()