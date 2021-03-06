import  urllib.request as remote
from time import gmtime, strftime
import os

# creates forder with data
if not os.path.isdir("data1"):
    os.makedirs("data1")

for i in range(1,28):
    # gets file from remote server
    url = "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID=" + str(i) + "&year1=1981&year2=2017&type=Mean"
    vhi_url = remote.urlopen(url)
    data = vhi_url.read().splitlines(True)
    region = (data[0].split())[6].decode("utf-8")
    # erases comma
    region = region[:-1]
    if region == "Kie":
        region = "KievCity"
    # writes filename
    out = open('data1/vhi_id_' + str(i) + '_' + region + strftime('_%Y-%m-%d_%H:%M', gmtime()) + '.csv','w')

    # writes data
    data = data [1:-1]
    out.write("year,week,SMN,SMT,VCI,TCI,VHI\n")
    for item in data:
        string = item.decode("utf-8").split(',')
        tmp = string[0].split()
        string = tmp + string[1:]
        j = 0
        for word in string:
            if j != len(string) - 1:
                word += ','
            string[j] = word
            j += 1
        out.write(''.join(string))
    out.close()
    print("VHI #" + str(i) + " is downloaded...")
