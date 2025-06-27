def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return


    except Exception as e:
        print(e)

    finally:
        print("i am inside of Finally.")  #finally can be useed in any cases but mostly used for 'def functions' with try & except


main()

