# -*- coding: utf-8 -*-

import os
import datetime
import random
import time

##############################
# Bines Rechen Uhr
# Author: Simon Schmid
# Datum: 19.01.2019
##############################


class CalculatorClock:

    def __init__(self, clearscreeneverycycle=False):
        self._possible_ops = ['plus', 'minus', 'mult', 'divide', 'modulo']
        self.__clearscreeneverycycle = clearscreeneverycycle

        os.system("cls")
        os.system("title Bines Rechen Uhr")

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

            if dtime.minute != old_min:

                if self.__clearscreeneverycycle:
                    os.system("cls")

                print("")
                print("---------- Neue Zeit ----------")  # todo remove
                print("")

                # hour
                time_input = dtime.hour
                rand_op = random.choice(self._possible_ops)
                if time_input > 10:  # having module with to large numbers is crappy
                    while rand_op == 'modulo':
                        rand_op = random.choice(self._possible_ops)
                display = "{} h".format(self.__calculate_display(rand_op, time_input))
                print("{0:^32}".format(str(self.__calculate_display(rand_op, time_input)) + " h"))

                # minute
                time_input = dtime.minute
                rand_op = random.choice(self._possible_ops)
                if time_input > 10:  # having module with to large numbers is crappy
                    while rand_op == 'modulo':
                        rand_op = random.choice(self._possible_ops)
                print("{0:^32}".format(str(self.__calculate_display(rand_op, time_input)) + " min"))

                time.sleep(58)  # todo kann man schöner lösen

            old_min = dtime.minute

    def __calculate_display(self, rand_op, curr_time):
        """
        creates display_str based on currentTime and the choosen random operator
        """

        display_str = None

        # plus
        if rand_op == 'plus':
            rand_summ = random.randint(1, curr_time)
            display_str = "{} + {}".format(rand_summ, curr_time - rand_summ)

        # minus
        if rand_op == 'minus':
            rand_min = random.randint(curr_time, 61)
            display_str = "{} - {}".format(rand_min, rand_min - curr_time)

        # multiplicate
        if rand_op == 'mult':
            rand_prod1 = random.randint(2, 10)
            rand_prod2 = random.randint(2, 10)
            if rand_prod1 * rand_prod2 == curr_time:
                display_str = "{} x {}".format(rand_prod1, rand_prod2)
            elif rand_prod1 * rand_prod2 > curr_time:
                display_str = "{} x {} - {}".format(rand_prod1, rand_prod2, rand_prod1 * rand_prod2 - curr_time)
            elif rand_prod1 * rand_prod2 < curr_time:
                display_str = "{} x {} + {}".format(rand_prod1, rand_prod2, curr_time - rand_prod1 * rand_prod2)

        # divide
        if rand_op == 'divide':
            rand_divisor = random.randint(2, 6)
            rand_dividend = random.randint(1, 4) * rand_divisor
            if rand_dividend / rand_divisor == curr_time:
                display_str = "{} / {}".format(rand_dividend, rand_divisor)
            elif rand_dividend / rand_divisor > curr_time:
                display_str = "{} / {} - {}".format(rand_dividend, rand_divisor, int(rand_dividend / rand_divisor - curr_time))
            elif rand_dividend / rand_divisor < curr_time:
                display_str = "{} / {} + {}".format(rand_dividend, rand_divisor, int(curr_time - rand_dividend / rand_divisor))

        # modulo
        if rand_op == 'modulo':
            rand_dividend = random.randint(curr_time, curr_time * 3)
            rand_divisor = random.randint(2, 5)
            while rand_divisor >= rand_dividend:
                rand_dividend = random.randint(curr_time, curr_time * 3)
                rand_divisor = random.randint(2, 5)
            if rand_dividend % rand_divisor == curr_time:
                display_str = "{} % {}".format(rand_dividend, rand_divisor)
            elif rand_dividend % rand_divisor > curr_time:
                display_str = "{} % {} - {}".format(rand_dividend, rand_divisor, int(rand_dividend % rand_divisor - curr_time))
            elif rand_dividend % rand_divisor < curr_time:
                display_str = "{} % {} + {}".format(rand_dividend, rand_divisor, int(curr_time - rand_dividend % rand_divisor))

        return display_str


# start clock
if __name__ == '__main__':
    clock = CalculatorClock(clearscreeneverycycle=False)
    clock.show_time()
