import os
import requests
from urllib.parse import urlparse
# import pefile
print("########################################################")
print("####New Update Launcher####")
print("########################################################")
dir = '%s\\beamin_launcher.exe'% os.path.expanduser("~")
# def get_version_file ():
#     try :
#         pe = pefile.PE(dir)
#         ProductVersionLS = pe.VS_FIXEDFILEINFO[0].ProductVersionLS
#         ProductVersionMS = pe.VS_FIXEDFILEINFO[0].ProductVersionMS
#         ProductVersion = (ProductVersionMS >> 16, ProductVersionMS & 0xFFFF, ProductVersionLS >> 16)
#         pe.close()
#         return 'v%s.%s.%s' % ProductVersion
#     except:
#         return 'v1.0.0 '
def get_version_file ():
    try:
        f = open("/Users/hoon/Documents/version", 'r')
    except:
        f = open("C:/version",'r')
    for line in f:
        line = line.strip()
    f.close()
    return line
def get_version_git():
    r = requests.head("https://github.com/kimmoney/gongzone_beamin_releases/releases/latest")
    print(r.headers)
    ver = r.headers['location'][-6:]
    return ver
def update_version(version):
    try:
        f = open("/Users/hoon/Documents/version", 'w')
    except:
        f = open("C:/version",'w')
    f.write(version)
    f.close()

print(dir)
ver_file = get_version_file()
ver_git  = get_version_git()
print("file:",ver_file)
print("git:",ver_git)

if ver_file == ver_git :
    print("open")
    pass
else:
    try:os.remove(dir)
    except:pass
    print("Installing new version")
    url = "https://github.com/kimmoney/gongzone_beamin_releases/releases/download/{}/beamin_gongzone.exe".format(ver_git)
    file = requests.get(url,stream = True)
    print(url)
    parsed_file = urlparse(url)
    file_name = os.path.basename(parsed_file.path)
    file = requests.get(url)    
    update_version(ver_git)
    open(dir, 'wb').write(file.content)
print('Finish')
commend = "start "+ dir
os.system(commend)