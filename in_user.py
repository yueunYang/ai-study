def user_input():
    print("가위 바위 보 게임입니다. 어떤 것을 내시겠습니까?")
    a = input()
    if a == '가위':
        return 0
    elif a == '바위':
        return 1
    elif a == '보':
        return 2
    
