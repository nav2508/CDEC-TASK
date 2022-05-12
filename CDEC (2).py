#!/usr/bin/env python
# coding: utf-8

# In[1]:


from decimal import *
import datetime
from datetime import date
import re

type=["","","",""]

pattern = re.compile(r"[0]")
pattern1 = re.compile(r"[1]")
pattern2 = re.compile(r"fal")
pattern3 = re.compile(r"tru")

def dataconversionfunction1(datatype,value):
    
    
    
    if datatype == "boolean":
       
        
        
        match1 = pattern.search(value)
        if match1!=None:
            
            return False
        
        
        match2 = pattern1.search(value)
        if match2!=None:
            
            return True
        
        
        match3 = pattern2.search(value)
        if match3 != None:
        
            return False
        
        
        match4 = pattern3.search(value)
        if match4!= None:
        
            return True
        else:
            value = None
        
        return value

           
    if datatype == "decimal" or  datatype == "distance" or datatype == "percentile" or datatype == "currency" :
        locales=["$","Pu","kr","£","€","Rs","₦","Php","￥","₹"]
        if(re.search('\d*\.?\d+',value)):
            res = ""
            for i in value:
                if(i.isdigit() == False and i != "."):
                    res += "0"
                else:
                    res+=i
            lst = res.split(".")
            finalres = ""
            c = 0
            for i in lst:
                if(int(i) != 0 and c != len(lst)-1):
                    finalres+=i
                    finalres+="."
                elif (int(i) != 0 and c == len(lst)-1):
                    finalres+=i
                c = c+1

            finalres = float(finalres)
            
        if datatype == "currency":
            finalres = str(finalres)
            for i in locales:
                if(value.find(i) != -1):
                    finalres+=i
                    break



        return (finalres)
    if datatype == "number":
        if(re.search('\d*\.?\d+',value)):
            res = ""
            for i in value:
                if(i.isdigit() == False):
                    res += "0"
                else:
                    res+=i
        return int(res)
                

                
            
    if datatype == "email":
        
        value1 = ""
        r = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Z|a-z]{2,3}'
       
        if(re.search(r,value)):
            
            
            matched_value = re.search(r,value)
            
            length = matched_value.span()
            
            
            value1 = value[int(length[0]):int(length[1])] 
            while(value1[0] in "+-%_."):
                value1 = value1[1:len(value1)]
           
            pass
        else:
            value1 = None
        return value1



           
    if datatype == "hyperlink":
        regex = ("[a-zA-Z0-9@:%._\\+~#?&//=]" +"{2,256}\\.[a-z]" +"{2,6}\\b([-a-zA-Z0-9@:%" +"._\\+~#?&//=]*)")

        p = re.compile(regex)
        if(re.search(p, value) == 0):
            value = None

        return value


        
    if datatype == "password" or datatype == "richtext" or datatype == "text":
        value = str(value)

        return value
    
    if datatype == "date":
        string = value
        if("/" in string):
            lst = string.split("/")
            n = len(lst)
            res = ""
        if n == 3:
            if(lst[1].isdigit() == False):
                res+=lst[0]
                res+="-"
                res+="01-"
                res+=lst[2]
                print(res)
            else:
                count = 0
                for i in lst:
                    count = count+1
                    if(count != 3):
                        res+=i
                        res+="-"
                    else:
                        res+=i
                print(res)
        elif n == 2:
            res+="01-"
            count = 0
            for i in lst:
                count =  count+1
                if(count != 2):
                    res+=i
                    res+="-"
                else:
                    res+=i
            print(res)
        else:
            res ="01-01-"
            res+=string
            print(res)
    
                
    if datatype == "daterange":
        
        from datetime import datetime
        import dateutil.parser as dparser
        t = dparser.parse(value,fuzzy=True, fuzzy_with_tokens = True)
        res =""
        now = t[0] # current date and time
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")
        time = now.strftime("%H:%M:%S")
        res+=year
        res+="-"
        res+=month
        res+="-"
        res+=day
        res+="T"
        res+=time
        res+=".000Z"
        print(res)
    
    if datatype == "mobileno":
        import sys, os, re
        import glob          
        import errno 
        reg_ex = "(?:(?:\+|0{0,2})91(\s*[\\-]\s*)?|[0]?)?[6789]\d{2}\s*\d{3}\s*\d{4}"    
        count = 0
        for i in value:
            if i.isdigit() == True:
                count+=1
        if count == 10:
            match = re.search(reg_ex,value)
            print(match)
        elif count == 12:
            if "+" in value:
                match = re.search(reg_ex,value)
                print(match)
    
    
    

        
        
            
            


# In[ ]:




