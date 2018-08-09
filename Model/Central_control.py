# -*- coding: utf-8 -*-
import example
from print_API import printAPI

def start():
    Test_Data = {"Hello":True}
    if example.Test(Test_Data).get("World") != True:
        printAPI("ERROR to example")
    printAPI("ALL OK")