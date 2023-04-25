from pytube import YouTube
import urllib.request
import speedtest
import qrcode

def spdtest():
    wifi  = speedtest.Speedtest()
    print("Wifi Download Speed is ", wifi.download())
    print("Wifi Upload Speed is ", wifi.upload())

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")

    print("Download is completed successfully")


def menu():
    print("1. Download a YouTube Video\n2. Check your network\n3. Do a speedtest\n4. URL to QR Converter\n5. Exit")

def qrc():
    input_URL=input("Enter Site URL: ")
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )

    qr.add_data(input_URL)
    qr.make(fit=True)
    img = qr.make_image(fill_color="red", back_color="white")
    img.save("url_qrcode.png")

    print(qr.data_list)


def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False


menu()

def main():
    ch=int(input("Enter your choice: "))

    if ch==1:
        link=input("Enter YouTube URL:")
        Download(link)

    elif ch==2:
        # test
        print( "connected" if connect() else "no internet!")

    elif ch==3:
        spdtest()

    elif ch==4:
        qrc()

    elif ch==5:
        print("Exiting.....Done")

    else:
        print("Invalid Input. Try again")
        menu()
        main()
main()