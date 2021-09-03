import eel
from edit_date2 import *


@eel.expose
def edit_date2(input_month,input_day):
    main2(input_month,input_day)

eel.init("web")
eel.start("main2.html",size=(600, 800))

