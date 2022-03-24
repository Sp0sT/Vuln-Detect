#!/usr/bin/python
#pip install requests

import requests
import sys
import pickle
import urllib3
from time import sleep



words = (""" \x1b[34m

                  __      __    _         _____       _            _
                  \ \    / /   | |       |  __ \     | |          | |
                   \ \  / /   _| |_ __   | |  | | ___| |_ ___  ___| |_
                    \ \/ / | | | | '_ \  | |  | |/ _ \ __/ _ \/ __| __|
                     \  /| |_| | | | | | | |__| |  __/ ||  __/ (__| |_
                      \/  \__,_|_|_| |_| |_____/ \___|\__\___|\___|\__|             by sp0st






                             #############################################################
                             ###################################################   #######
                             ###############################################   /~\   #####
                             ############################################   _- `~~~', ####
                             ##########################################  _-~       )  ####
                             #######################################  _-~          |  ####
                             ####################################  _-~            ;  #####
                             ##########################  __---___-~              |   #####
                             #######################   _~   ,,                  ;  `,,  ##
                             #####################  _-~    ;'                  |  ,'  ; ##
                             ###################  _~      '                    `~'   ; ###
                             ############   __---;                                 ,' ####
                             ########   __~~  ___                                ,' ######
                             #####  _-~~   -~~ _                               ,' ########
                             ##### `-_         _                              ; ##########
                             #######  ~~----~~~   ;                          ; ###########
                             #########  /          ;                        ; ############
                             #######  /             ;                      ; #############
                             #####  /                `                    ; ##############
                             ###  /                                      ; ###############
                             #                                            ################

                                                                                                    \x1b[34m""")
for char in words:
    sleep(0.0001)
    sys.stdout.write(char)

def main():
        n = input("\n1- XSS detect\n2- SQLi detect\n\nselect a mode : ")

        if n == 1:
            requests()
        elif n == 2:
            sql_injection()

def requests():
        print("_______________XSS_detect_______________")
        url = raw_input("\nEnter url : ")
        r = requests.post(url, data={'=':'<script>alert("find")</script>'})
        print(r.status_code)
        if r.status_code == 200:
            print("XSS was detected")
        elif r.status_code == 405:
            print("XSS not found")


def sql_injection():
    print("_______________SQLi_detect_______________")
    a = input("1- Low_methode\n2- Hight_methode\n\nselect a mode : ")
    if a == 1:
        Low_methode()
    elif a == 2:
        Hight_methode()


def Low_methode():
    print("Low_methode sql injection\n\nIn_Build")

def Hight_methode():
    print("Hight_methode sql injection\n\nIn_Build")




if __name__ == "__main__":
    main()
