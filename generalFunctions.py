def smartInput(msg:str,datatype=str,bounds=None,validinput=None,case:str="lower"):
    while True:
        try:
            user = datatype(input(msg))
            if type(user) == str:
                if case == "upper":
                    user = user.upper()
                elif case == "lower":
                    user = user.lower()
                
            if bounds != None:
                if not bounds[0] <= user <= bounds[1]:
                    raise ValueError
            if validinput != None:
                if user not in validinput:
                    raise ValueError
            break
        except ValueError:
            continue
    return user