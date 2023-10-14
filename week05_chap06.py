while True:
    menu = input("1) 온도변환(화씨->섭씨)   2) 종료 : ")
    if menu == '1':
        fahrenheit = input("화씨 온도 입력 : ")
        # (100°F − 32) × 5/9 = 37.778°C
        celsius = (float(fahrenheit) - 32) * 5 / 9
        print(f"화씨 {fahrenheit}도는 섭씨 {celsius}도 입니다.")
    elif menu == '2':
        break
    else:
        print("메뉴에서 골라주세요.")

