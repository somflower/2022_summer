light1 = input("1번 전지가 있습니까? (Y/N)")
light2 = input("2번 전지가 있습니까? (Y/N)")

if light1 == 'y' and light2 == 'y' :
    print("직렬연결 : 전구에 불이 켜집니다.")
    print("병렬연결 : 전구에 불이 켜집니다.")
elif light1 == 'n' and light2 == 'n' :
    print("직렬연결 : 전구에 불이 꺼집니다.")
    print("병렬연결 : 전구에 불이 꺼집니다.")
else :
    print("직렬연결 : 전구에 불이 꺼집니다.")
    print("병렬연결 : 전구에 불이 켜집니다.")