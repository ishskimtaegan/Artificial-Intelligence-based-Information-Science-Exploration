while True:
    menu = input("1) 온도변환(화씨->섭씨)   2) 절대값   3) 종료 : ")
    if menu == '1':
        fahrenheit = input("화씨 온도 입력 : ")
        # (100°F − 32) × 5/9 = 37.778°C
        celsius = (float(fahrenheit) - 32) * 5 / 9
        print(f"화씨 {fahrenheit}도는 섭씨 {celsius}도 입니다.")
    elif menu == '2':
        number = int(input("정수 입력 : "))
        if number > 0:
            continue
        print(f"음수 {number}의 절대값은 {abs(number)}입니다")
    elif menu == '3':
        break
    else:
        print("메뉴에서 골라주세요.")
