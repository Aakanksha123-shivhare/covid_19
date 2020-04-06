# Do all the imports
import banner as banner
import requests
import bs4
import tkinter as tk
import plyer
import time
import datetime
import threading


def get_html_data(url):
    data = requests.get(url)
    return data


def get_corona_detail_of_india():
    url = "https://www.mohfw.gov.in/"
    html_data = get_html_data(url)
#    print(html_data.text)
    bs = bs4.BeautifulSoup(html_data.text,"html.parser")
#    print(bs.prettify())
    info_div = bs.find("div",class_ = "information_row").find_all("div",class_ = "iblock" )
   # print(info_div)
 #   print(info_div.prettify())
  #  print(len(info_div))
    all_details = ""
    for block in info_div:
   #     print(block)
   #     print()
        count = block.find("span",class_ = "icount").get_text()
        text = block.find("div",class_ = "info_label").get_text()
        all_details = all_details + text + " : " + count + "\n"
    return all_details
#print(get_corona_detail_of_india())


##function use to reload the data from website
def refresh():
    newdata = get_corona_detail_of_india()
    print("Refreshing..")
    mainLable['text'] = newdata

## function for notifying....
# def notify_me():
#     while True:
#         plyer.notification.notify(
#         title="covid 19 cases of INDIA",
#         message=get_corona_detail_of_india(),
#         timeout=10,
#         #app_icon="icon.ico"
#      )
#         time.sleep(30)



##creating gul::::
root = tk.Tk()
root.geometry("900x800")
root.iconbitmap("icon.ico")               ##doubt
root.title("CORONA DATA TRACKER - INDIA")
root.configure(background="white")

f = ("poppins",25,"bold")
#
# banner = tk.PhotoImage(file="covid.png")
# bannerLable = tk.Label(root,image=banner)
# bannerLable.pack()

mainLable = tk.Label(root,text=get_corona_detail_of_india(),font=f)
mainLable.pack()
reBtn = tk.Button(root,text="REFRESH",font=f,relief="solid",command=refresh)
reBtn.pack()
##create a new thread
# th1 = threading.Thread(target=notify_me())
# th1.setDaemon(True)
# th1.start

root.mainloop()




