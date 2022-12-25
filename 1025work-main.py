# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 19:11:30 2022

@author: mitch
"""

import mylccdb
from datetime import datetime

def addEmployee(name,sex,tel):
    now = datetime.now()
    today = datetime.strftime(now,'%Y-%m-%d')
    sql = "insert into employee(name,sex,tel,assume) values('{}','{}','{}','{}')".format(name,sex,tel,today)
    
    cursor = mylccdb.conn.cursor()
    cursor.execute(sql)
    mylccdb.conn.commit()
    

def addWorks(employeeid,items,info):
    sql = "insert into works(items,info,employeeid) values('{}','{}','{}')".format(items,info,employeeid)
    
    cursor = mylccdb.conn.cursor()
    cursor.execute(sql)
    mylccdb.conn.commit()   
    
def allEmplyee():
    sql = "select id,name from employee"
    cursor = mylccdb.conn.cursor()
    cursor.execute(sql)
    mylccdb.conn.commit()       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def updateEmplyee(employeeid,tel,sex):
    sql = "update employee set tel='{}',sex='{}' where id='{}'".format(tel,sex,employeeid)
    cursor = mylccdb.conn.cursor()
    cursor.execute(sql)
    mylccdb.conn.commit()   
    
def queryEmplyeeworks(employeeid):
    sql = "select employee.name,works.*from employee inner join works on employee.id = works.employeeid where employee.id ='{}'".format(employeeid)
    
    cursor = mylccdb.conn.cursor()
    cursor.execute(sql)
    mylccdb.conn.commit()   
    
    result = cursor.fetchall()
    
    for row in result:
        print("員工:",row[0])
        print("工作項目:",row[2])
        print("工作內容:",row[3])
        
if __name__ == "__main__":
    item = input("員工系統:a -> 新增員工 w-> 新增員工工作 q->查詢 u->修改 e->員工工作內容 x->離開:")
    
    
    if item =="x":
        break
    elif item == "a":
        name = input("新增員工姓名:")
        sex = input("性別(F/M):")
        tel = input("電話:")
        addEmpyloee(name,sex,tel)
        allEmplyee()
    elif item == "w":
        allEmplyee()
        
        empId = input("請輸入員工編號:")
        item = input("請輸入員工作事項:")
        info = input("請輸入內容:")
        addWorks(empId,item,info)
        
    elif item == "q":
        eid = input("請輸入員工編號:")
        queryEmpyloee(eid)
        
    elif item == "u":
        allEmplyee()
        
        eid = input("請輸入員工編號:")
        tel = input("請輸入修改的電話:")
        sex = input("請輸入修改的性別(F/M):")
        update
    
    
    
    
    
    
    
    
    
    
    
    
    
    
