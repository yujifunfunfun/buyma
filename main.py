import eel
from edit_date import *


@eel.expose
def edit_date(input_month,input_day):
    main(input_month,input_day)

eel.init("web")
eel.start("main.html",size=(600, 800))