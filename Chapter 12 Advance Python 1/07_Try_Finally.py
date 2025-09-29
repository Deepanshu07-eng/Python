def main():
    try:
        a = int(input("Enter Number: "))
        print(a)
        return

    except Exception as e:
        print(e)

    finally:
        print("Its finally")


main()