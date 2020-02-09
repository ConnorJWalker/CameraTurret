import sys
import application

if len(sys.argv) == 1:
    print("No arguments entered, rendering prevented")
    app = application.Application(False)
    app.start()
else:
    if sys.argv[1] == "-r":
        print("Starting detector with renderer")
        app = application.Application(True)
        app.start()
    else:
        print("starting detector without render")
        app = application.Application(False)
        app.start()
    