from gtts import gTTS #모듈 불러오기
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

def TTS(contents, file_name): #tts를 생성하고 출력하는 함수 argument로 텍스트와 파일명을 전달받는다.

    print(contents)
    tts = gTTS(text=contents, lang='ko')
    tts.save(file_name + ".mp3")
    playsound.playsound(file_name + ".mp3")

def wrong_input():

    text = "잘못된 입력입니다." 
    TTS(text, "Wrong input") #위에서 만든 TTS 함수를 활용하여 "잘못된 입력입니다." 라는 문자열이 출력되고 tts로 변환되에 음성으로 출력되고 "Wrong input" 라는 파일명으로 저장된뒤 프로그램이 종료된다.
    exit()

def no_menu(): #선택한 카테고리의 교집합이 존재하지 않을시 실행

    text = "선택하신 조건과 일치하는 메뉴가 없습니다." 
    TTS(text, "no_menu"); exit() #위에서 만든 TTS함수를 활용하여 "선택하신 조건과 일치하는 메뉴가 없습니다." 라는 문자열이 출력되고 tts로 변환되어 출력된뒤 "no_menu" 라는 파일명으로 저장된뒤 프로그램이 종료된다.

def recommend_menu(menu_list):

    global text
    text = "추천하는 메뉴는"
    for i in menu_list : text += (' ' + i) #전달받은 리스트 형태의 자료의 0번째 값 부터 마지막 값 까지 순차적으로 i 라는 변수에 대입되어 text 변수에 더해진다.
    text += "입니다."
    
text = "원하시는 메뉴의 카테고리를 선택해 주세요."
TTS(text, "category") #TTS 함수에 argument로 text, "category" 를 전달

a,b = input().split(' ') #a,b 라는 변수에 사용자가 입력한값을 ' ' 를 기준으로 나누어 저장

if a =='밥': a = 밥 #입력된 값에 따라 맞는 변수를 다시 a 라는 변수에 저장
elif a =='빵': a = 빵
elif a =='면': a = 면
elif a =='고기': a = 고기
elif a =='분식': a = 분식
elif a =='튀김': a = 튀김
elif a =='국물': a = 국물
elif a =='구이': a = 구이
elif a =='비빔': a = 비빔
else: wrong_input() #잘못된 입력

if b =='밥': b = 밥 #입력된 값에 따라 맞는 변수를 다시 b 라는 변수에 저장
elif b =='빵': b = 빵
elif b =='면': b = 면
elif b =='고기': b = 고기
elif b =='분식': b = 분식
elif b =='튀김': b = 튀김
elif b =='국물': b = 국물
elif b =='구이': b = 구이
elif b =='비빔': b = 비빔
else: wrong_input() #잘못된 입력

recommend_menu0 = set(a) & set(b) #a,b 라는 이름의 리스트의 교집합을 recommend_menu0 이라는 변수에 저장

if recommend_menu0 != set(): #recommend_menu0 이 빈 리스트가 아닌 경우 참
    recommend_menu(recommend_menu0) #recommend_menu 라는 함수에 argument로 recommend_menu0 라는 변수를 전달
    TTS(text, "recommend_menu0") #TTS 함수에 argument로 text, recommend_menu0 라는 변수를 전달
else: no_menu() #no_menu 함수를 호출한다

text = "맵기정도를 선택해 주세요."; TTS(text, "spicy") #TTS 함수에 argument로 text, "spicy" 를 전달

spicy = input() #spicy 값을 입력받는다

if spicy == '매운맛': spicy = 매운맛 #입력된 값에 따라 맞는 변수를 다시 spicy 라는 변수에 저장
elif spicy == '중간맛': spicy = 중간맛
elif spicy == '순한맛': spicy = 순한맛
else: wrong_input() #잘못된 값을 입력하였을경우 wrong_input 함수를 호출한다.

recommend_menu1 = set(recommend_menu0) & set(spicy) #recommend_menu0 과 spicy 라는 리스트들의 교집합을 recommend_menu1이라는 리스트 자료형을 가진 변수에 저장한다.

if recommend_menu1 != set(): #recommend_menu1 이 빈 리스트가 아닌 경우 참
    recommend_menu(recommend_menu1) #recommend_menu 라는 함수에 argument로 recommend_menu1 라는 변수를 전달
    TTS(text, "recommend_menu1") #TTS 함수에 argument로 text, recommend_menu1 라는 변수를 전달
else: no_menu() #no_menu 함수를 호출한다