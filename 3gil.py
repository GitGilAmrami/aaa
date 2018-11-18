class weather:

    name="DAY of WEEK"

    def rain(self):
        print("It is raining")

    def snow(self):
        print("It is snowing")

    # @staticmethod
    # def temperatur():
    #     print("temperatur now is...")

def main():
    today=weather() ##instance=object
    today.name=print("MONDAY")
    print(today.name)
    today.rain()


    yestarday = weather()  ##instance=object
    yestarday.name="SUNDAY"
    print (yestarday.name)
    # yestarday.snow()
    # weather.temperatur()

if __name__ == '__main__':
    main()
    weather.temperatur()
    print(weather.name)