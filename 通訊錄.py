import re
flag = 1
contact =  {}

def check_phoneNumber(phone):
	m = re.findall(r'^09\d{2}-\d{6}$',phone)
	if m ==[]:
		print("電話格式為 : 09xx-xxxxxx\n")
		return True
	else:
		return False

def add_contact():
	global contact
	phone = ''
	check = True
	print("\n")
	name = input("請輸入姓名 : ")
	while (len(name) ==0):
		
		name = input("請輸入姓名 : ")
	#print(name)
	print("\n")
	while check:
		phone  = input("請輸入電話 : ")
		check = check_phoneNumber(phone)
	contact[name] = phone
	#print(contact)
	print("新增成功\n")

def search(arg):
	global contact
	print("\n")
	if len(contact)==0:
		print("目前沒有資料\n")
	if arg:
		for key,value in contact.items():
			print("%s %s\n" % (key,value))	
	else:
		name = input("請輸入人名 : ")
		if name in contact:
			print("%s %s\n" % (name,contact[name]))
		else:
			
			print("\n" + '查無此人' + "\n")
			
def delete():
	print("\n")
	name = input("請輸入姓名 : ")
	if name in contact:
		del contact[name]
		print("\n刪除成功\n")
	else:
		print("\n" + '查無此人' + "\n")

def clear():
	contact.clear()
	print("\n聯絡人都已刪除成功\n")

# 把旗標設為0 , 使其離開while
def setFlag():
	global flag 
	print("\nExit\n")
	flag  = 0 

# switch case 
def switch(user_input):
	try:
		{
			'1' : lambda : add_contact(),
			'2' : lambda : search(1),
			'3' : lambda : search(0),
			'4' : lambda : delete(),
			'5' : lambda : clear(),
			'0' : lambda : setFlag()
	}[user_input]()
	except Exception:
		pass

# 正規化檢查
def check_input(user_input):
	m = re.match(r'[0-5]',user_input)
	if (m == None ):
		print("\n請輸入0~5的數字\n")
		return False
	
	else:
		return True
	
def printInfo():
	while flag:
		print("1)新增聯絡人")
		print("2)查詢聯絡人 (全部)")
		print("3)查詢聯絡人 (部分)")
		print("4)刪除聯絡人")
		print("5)清除聯絡人")
		print("0)離開")
		print("\n")
		user_input = input("請輸入")
		check = check_input(user_input)
		if(check):
			switch(user_input)

if __name__ == "__main__":
	printInfo()

