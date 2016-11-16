
def main():
    data = raw_input().split('/')
    for word in data:
        if 'www' in word:
            return
    print data

if __name__ == '__main__':
    main()
