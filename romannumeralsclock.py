# -*- coding: utf-8 -*-

import os
import datetime
import time


##############################
# Bines Römische Zahlen Uhr
# Author: Simon Schmid
# Datum: 19.01.2019
##############################


class RomanNumeralsClock:

    def __init__(self, clearscreeneverycycle=False):
        self.__clearscreeneverycycle = clearscreeneverycycle

        os.system("cls")
        os.system("title Bines Römische Zahlen Uhr")

    def show_time(self):
        """
        main function running in loop and showing the new time every minute
        """

        # run in infinite loop
        while True:

            # get time
            dtime = datetime.datetime.now()
            if 'old_min' not in locals():
                old_min = None

            # calculate and print every second
            if dtime.minute != old_min:

                # calculate display and print to display
                if self.__clearscreeneverycycle:
                    os.system("cls")

                print("")
                print("---------- Neue Zeit ----------")
                print("")

                print("{0:^31}".format(self.__convert_arabic_to_roman(dtime.hour) + " : " + self.__convert_arabic_to_roman(dtime.minute)))

                time.sleep(58)  # todo kann man schöner lösen

            old_min = dtime.minute

    def __convert_roman_to_arab(self, romanstr):
        """
        converts a random roman number into a arabic number
        """

        arabic_number = 0
        roman_to_arab = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        # convert
        old_value = None
        for digit in range(len(romanstr)):

            # save value in old_value to skip same ones
            if old_value != romanstr[digit]:
                old_value = romanstr[digit]
            else:
                continue

            # check if subtraktion
            if digit < len(romanstr) - 1:
                if roman_to_arab.get(romanstr[digit]) < roman_to_arab.get(romanstr[digit + 1]):
                    if not (romanstr[digit] == 'I' or romanstr[digit] == 'X' or romanstr[digit] == 'C'):
                        print('Eigentlich duerfen nur I, X und C als Subtraktion genutzt werden. Genutzt wurde aber {}'.format(romanstr[digit]))
                    arabic_number = arabic_number - roman_to_arab.get(romanstr[digit])
                    continue

            # count how many times same value
            num_same_value = 0
            if digit <= len(romanstr):
                for counter in range(len(romanstr) - digit):
                    if romanstr[digit + counter] == romanstr[digit]:
                        num_same_value += 1
                        if num_same_value > 3:
                            print('Normalerweise duerfen nur maximal 3 gleiche Zahlen hintereinander stehen! Hier sind es ingesamt {} mal das Zeichen "{}"'.format(num_same_value, romanstr[digit]))
                    else:
                        break

            # add up values
            arabic_number = arabic_number + num_same_value * roman_to_arab.get(romanstr[digit])

        return arabic_number

    def __convert_arabic_to_roman(self, arabic_num):
        """
        converts a random arabic number into a roman number
        """

        # check input
        if arabic_num < 0:
            print("Negative Zahlen koennen nicht dargestellt werden!")
        if arabic_num > 3999:
            print("Zahlen ueber 3999 koennen nicht korrekt dargestellt werden!")

        # dictionary used to interpret the roman signs
        arab_to_roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        roman_list = []
        roman_str = ""

        # convert
        for digit in range(len(str(arabic_num))):

            # skip an zero
            if str(arabic_num)[digit] == 0:
                continue

            # get potency of number
            potency = len(str(arabic_num)) - digit - 1  # for example 2000 has potency of 3
            current_digit = int(str(arabic_num)[digit])

            # 1, 2, 3
            if 1 <= current_digit <= 3:
                for counter in range(current_digit):
                    roman_list.append(arab_to_roman.get(10**potency))

            # 4
            if current_digit == 4:
                roman_list.append(arab_to_roman.get(10**potency))
                roman_list.append(arab_to_roman.get(5 * 10**potency))

            # 5
            if current_digit == 5:
                roman_list.append(arab_to_roman.get(5 * 10**potency))

            # 6, 7, 8
            if 6 <= current_digit <= 8:
                roman_list.append(arab_to_roman.get(5 * 10**potency))
                for counter in range(current_digit - 5):
                    roman_list.append(arab_to_roman.get(10**potency))

            # 9
            if current_digit == 9:
                roman_list.append(arab_to_roman.get(10**potency))
                roman_list.append(arab_to_roman.get(10**(potency + 1)))

        # convert list into string for output
        num_elements = len(roman_list)
        for counter in range(num_elements):
            roman_str = roman_str + roman_list[counter]

        return str(roman_str)


# start clock
if __name__ == '__main__':
    clock = RomanNumeralsClock(clearscreeneverycycle=False)
    clock.show_time()
