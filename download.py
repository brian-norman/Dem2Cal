import urllib2

def main():
    download_file("http://schools.cbe.ab.ca/b860/pdfs/demands12.pdf")

def download_file(download_url):
    response = urllib2.urlopen(download_url)
    file = open("demands.pdf", 'w')
    file.write(response.read())
    file.close()
    print("Completed")

if __name__ == "__main__":
    main()