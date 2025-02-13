def determine_winner(user_input, ai_chice):
    
    if user_input == ai_chice:
        return "비겼습니다!"
    elif (user_input == 0 and ai_chice == 2) or (user_input == 1 and ai_chice == 0) or (user_input == 2 and ai_chice == 1):
        return "사용자가 이겼습니다!"
    else:
        return "AI가 이겼습니다!"