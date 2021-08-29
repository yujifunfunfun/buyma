import eel
from edit_date import *


@eel.expose
def edit_date(date):
    main(date)

eel.init("web")
eel.start("main.html")