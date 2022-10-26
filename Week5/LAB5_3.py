def exchange(m, c) :
    if country_list.count(c) == 1 :
        #index 함수 이용
        idx = country_list.index(c)
        print("%d 원은 %.2f %s 입니다."% (m, m/rate[idx], unit[idx]))
    else :
        print("해당 국가 정보가 없습니다.")

country_list = ['미국', '중국', '유럽', '일본', '영국']
unit = ['달러', '위안', '유로', '엔', '파운드']
rate = [1270.50, 189.44, 1345.21, 975.36, 1571.67]

money1 = int(input("환전 금액(원)을 입력하세요: "))
country = input("국가를 입력하세요: ")
exchange(money1, country)