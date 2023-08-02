from gtts import gTTS
import playsound

밥 = ["볶음밥","돼지국밥","콩나물국밥","장어덮밥","스테이크덮밥", "비빔밥","카레"]
빵 = ["핫도그", "빠네스프","햄버거","샌드위치","페스츄리"]
면 = ["라면","짬뽕","칼국수","비빔면","짜장면","스파게티","까르보나라"]
고기 = ["돈까스","치킨","규카츠","탕수육","멘보샤","닭껍질튀김","닭똥집","닭도리탕","갈비찜","김치찌개","된장찌개","소고기구이","돼지고기구이","닭고기구이","함박스테이크","제육볶음","불고기","육회"]
분식 = ["오징어튀김","새우튀김","튀김만두","오뎅탕","떡볶이"]

튀김 = ["볶음밥","핫도그","규카츠","돈까스","치킨","탕수육","멘보샤","닭껍질튀김","닭똥집","오징어튀김","새우튀김","튀김만두"]
국물 = ["돼지국밥","콩나물국밥","빠네스프","라면","짬뽕","칼국수","닭도리탕","갈비찜","김치찌개","된장찌개","오뎅탕","떡볶이"]
구이 = ["장어덮밥","스테이크덮밥","햄버거","샌드위치","소고기구이","돼지고기구이","닭고기구이","함박스테이크","제육볶음","불고기"]
비빔 = ["비빔밥","카레","페스츄리","짜장면","비빔면","스파게티","까르보나라","육회"]

매운맛 = ["비빔밥","짬뽕","비빔면","떡볶이"]
중간맛 = ["카레","핫도그","햄버거","라면","닭도리탕","김치찌개","제육볶음"]
순한맛 = ["볶음밥","돼지국밥","콩나물국밥","장어덮밥","스테이크덮밥","빠네스프","샌드위치","페스츄리","칼국수","짜장면","스파게티","까르보나라","돈까스","규카츠","치킨","탕수육","멘보샤","닭껍질튀김","갈비찜","된장찌개","소고기구이","돼지고기구이","닭고기구이","함박스테이크","육회","오징어튀김","새우튀김","튀김만두","오뎅탕","닭똥집","불고기"]

def TTS(contents, file_name):

    print(contents)
    tts = gTTS(text=contents, lang='ko')
    tts.save(file_name + ".mp3")
    playsound.playsound(file_name + ".mp3")

def wrong_input():

    text = "잘못된 입력입니다."
    TTS(text, "Wrong input")
    exit()

def no_menu():

    text = "선택하신 조건과 일치하는 메뉴가 없습니다."
    TTS(text, "no_menu"); exit()

def recommend_menu(menu_list):

    global text
    text = "추천하는 메뉴는"
    for i in menu_list : text += (' ' + i)
    text += "입니다."

text = "원하시는 메뉴의 카테고리를 선택해 주세요."
TTS(text, "category")

a,b = input().split(' ')

if a =='밥': a = 밥
elif a =='빵': a = 빵
elif a =='면': a = 면
elif a =='고기': a = 고기
elif a =='분식': a = 분식
elif a =='튀김': a = 튀김
elif a =='국물': a = 국물
elif a =='구이': a = 구이
elif a =='비빔': a = 비빔
else: wrong_input()

if b =='밥': b = 밥
elif b =='빵': b = 빵
elif b =='면': b = 면
elif b =='고기': b = 고기
elif b =='분식': b = 분식
elif b =='튀김': b = 튀김
elif b =='국물': b = 국물
elif b =='구이': b = 구이
elif b =='비빔': b = 비빔
else: wrong_input()

recommend_menu0 = set(a) & set(b)

if recommend_menu0 != set(): 
    recommend_menu(recommend_menu0)
    TTS(text, "recommend_menu0")
else: no_menu()

text = "맵기정도를 선택해 주세요."; TTS(text, "spicy")

spicy = input()

if spicy == '매운맛': spicy = 매운맛
elif spicy == '중간맛': spicy = 중간맛
elif spicy == '순한맛': spicy = 순한맛
else: wrong_input()

recommend_menu1 = set(recommend_menu0) & set(spicy)

if recommend_menu1 != set():
    recommend_menu(recommend_menu1)
    TTS(text, "recommend_menu1")
else: no_menu()