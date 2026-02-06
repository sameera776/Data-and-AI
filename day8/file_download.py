import threading
import urllib.request
def download_file():
    # url='http://localhost:8000/jk.txt'
    url='https://files.eric.ed.gov/fulltext/EJ1172284.pdf'
    filename='downloaded_test.pdf'
    print("start download of file")
    # time.sleep(2)
    urllib.request.urlretrieve(url,'filename')
    print("Download completed")

t=threading.Thread(target=download_file)
t.start()
print("Main thread continues execution")