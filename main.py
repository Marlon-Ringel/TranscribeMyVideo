from webinterface import Webinterface

def main():
    serverLink = "127.0.0.1:5000" #for development testing
    app = Webinterface(serverLink)
    app.run(debug=True)

if __name__ == "__main__":
    main()
    