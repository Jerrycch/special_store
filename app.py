# import streamlit as st
# import requests




# def getAllBookstore():
# 	url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M' # 在這裡輸入目標 url
# 	headers = {"accept": "application/json"}
# 	response = requests.get(url, headers=headers)
# 	res=response.json() # 將 response 轉換成 json 格式
# 	return res # 回傳值




	
# def getCountyOption(items):
# 	optionList=[]# 創建一個空的 List 並命名為 optionList
# 	for item in items:
# 		name=item['cityname'][0:3]# 把 cityname 欄位中的縣市名稱擷取出來 並指定給變數 name
# 		# hint: 想辦法處理 item['cityName'] 的內容
# 		# 如果 name 不在 optionList 之中，便把它放入 optionList
# 		if name not in optionList:
# 			optionList.append(name)# hint: 使用 if-else 來進行判斷 / 用 append 把東西放入 optionList
# 	return optionList


# def getDistrictOption(items, target):
# 	optionList = []
# 	for item in items:
# 		name = item['cityName']
# 		if target not in name: continue# 如果 name 裡面不包含我們選取的縣市名稱(target) 則略過該次迭代
# 		# hint: 使用 if-else 判斷式並且用 continue 跳過
# 		name.strip()
# 		district = name[5:]
# 		if len(district) == 0: continue
# 		if district not in optionList: optionList.append(district)# 如果 district 不在 optionList 裡面，將 district 放入 optionList
# 		# hint: 使用 if-else 判斷式並使用 append 將內容放入 optionList
# 	return optionList




# def getSpecificBookstore(items, county,districts):
# 	specificBookstoreList = []
# 	for item in items:
# 		name = item['cityName']
# 		if county not in name: continue # 如果 name 不是我們選取的 county 則跳過
# 		for district in districts:
# 			if district not in name: continue
# 			specificBookstoreList.append(item)  # hint: 用 if-else 判斷並用 continue 跳過
# 	return specificBookstoreList

# def app():
#     bookstoreList = getAllBookstore()

#     countyOption = getCountyOption(bookstoreList)

#     st.header('特色書店地圖')
#     st.metric('Total bookstore', len(bookstoreList))
#     county = st.selectbox('請選擇縣市', countyOption)
#     districtOption = getDistrictOption(bookstoreList, county)
#     district = st.multiselect('請選擇區域', districtOption)

#     specificBookstore = getSpecificBookstore(bookstoreList, county, district)
#     num = len(specificBookstore)
#     st.write(f'總共有{num}項結果', num)


import streamlit as st
import requests

def getAllBookstore() -> list:
    url = "https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    res = response.json()
    return res

def getCountyOption(items):
    optionList = []
    for item in items:
        name = item['cityName'][0:3]
        if name not in optionList:
            optionList.append(name)
    return optionList

def getDistrictOption(items, target):
    optionList = []
    for item in items:
        name = item['cityName']
        if target not in name: continue
        name.strip()
        district = name[5:]
        if len(district) == 0: continue
        if district not in optionList:
            optionList.append(district)
    return optionList

def getSpecificBookstore(items, county, districts):
    specificBookstoreList = []
    for item in items:
        name = item['cityName']
        if county not in name: continue
        for district in districts:
            if district not in name: continue
            specificBookstoreList.append(item)
    return specificBookstoreList

def getBookstoreInfo(items):
    expanderList = []
    for item in items:
        expander = st.expander(item['name'])
        expander.image(item['representImage'])
        expander.metric('hitRate', item['hitRate'])
        expander.subheader('Introduction')
        expander.write(item['intro'])
        expander.subheader('Address')
        expander.write(item['address'])
        expander.subheader('Open Time')
        expander.write(item['openTime'])
        expander.subheader('Email')
        expander.write(item['email'])
        expanderList.append(expander)
    return expanderList

def app():
    bookstoreList = getAllBookstore()

    countyOption = getCountyOption(bookstoreList)

    st.header('特色書店地圖')
    st.metric('Total bookstore', len(bookstoreList))
    county = st.selectbox('請選擇縣市', countyOption)
    districtOption = getDistrictOption(bookstoreList, county)
    district = st.multiselect('請選擇區域', districtOption)

    specificBookstore = getSpecificBookstore(bookstoreList, county, district)
    num = len(specificBookstore)
    st.write(f'總共有{num}項結果', num)

    specificBookstore.sort(key = lambda item: item['hitRate'], reverse=True)
    bookstoreInfo = getBookstoreInfo(specificBookstore)

if __name__ == '__main__':
    app()












if __name__ == '__main__':
    app()
