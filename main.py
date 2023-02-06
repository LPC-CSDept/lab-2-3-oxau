def main():
    ##################################################
    # Comlete your code here
    ##################################################
    val1 = int(input('First Integer: '))
    val2 = int(input('Second Integer: '))
    val3 = int(input('Third Integer: '))
    sum = int(val1 + val2 + val3)
    avg = float(sum/3)

    print ('Values: ' + '{0} {1} {2}'. format(val1, val2, val3))
    print (f'Total: \t\t{sum}')
    print (f'Average: \t{avg:.2f}')

    
    pass


if __name__ == '__main__':
    main()
