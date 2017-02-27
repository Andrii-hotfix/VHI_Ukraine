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
    out.write("provinceID = " + str(i) + "\n")
    out.write("year,week,SMN,SMT,VCI,TCI,VHI\n")
    for item in data:
        out.write(item.decode("utf-8"))
    out.close()
    print("VHI #" + str(i) + " is downloaded...")
