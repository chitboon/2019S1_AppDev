try:
    count = int(input('How many number you want to capture?'))

    numList = []


    for i in range(count):
        msg = 'Enter number #' + str(i+1)
        num = int(input(msg))
        numList.append(num)

    print('The lowest number in the list:', min(numList))
    print('The highest number in the list:', max(numList))
    print('The total of the number in the list:', sum(numList))

    print('The average of the number in the list:', sum(numList)/len(numList))
except ValueError:
   print('Invalid integer')
except ZeroDivisionError:
   print('Zero Division Error')
except:
   print('An unknown error occured')
finally:
   print('End of Program')
