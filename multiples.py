# This function will print multiples of three as Three', multiples of five as Five and multiples of three and five as ThreeFive
def multiples(num):
    response = str(num)
    if num % 3 == 0:
        response = 'Three'

    elif num % 5==0:
        response ='Five'

    elif num%3==0 and num%5==0 :
        response ='ThreeFive'
    return response

if __name__ == "__main__":
    print("\n".join(multiples(num) for num in range(1,101)))