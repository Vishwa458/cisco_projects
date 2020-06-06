from collections import defaultdict

#Routers Records
Routers = { 'router1': {'Sapid': 122344,'Loopback':'127.0.0.1','Hostname':'localhost','Mac_address':'00:0A:95:9D:68:16'},
'router1': {'Sapid': 122344,'Loopback':'127.0.0.1','Hostname':'localhost','Mac_address':'00:0A:95:9D:68:16'},
'router2': {'Sapid': 122344,'Loopback':'127.0.0.1','Hostname':'localhost','Mac_address':'00:0A:95:9D:68:16'},
'router3': {'Sapid': 122344,'Loopback':'127.0.0.1','Hostname':'localhost','Mac_address':'00:0A:95:9D:68:16'},
'router4': {'Sapid': 122344,'Loopback':'127.0.0.1','Hostname':'localhost','Mac_address':'00:0A:95:9D:68:16'},
'router5': {'Sapid': 122344,'Loopback':'127.0.0.1','Hostname':'localhost','Mac_address':'00:0A:95:9D:68:16'},
'router6': {'Sapid': 122344,'Loopback':'127.0.0.1','Hostname':'localhost','Mac_address':'00:0A:95:9D:68:16'},
'router7': {'Sapid': 122344,'Loopback':'127.0.0.1','Hostname':'localhost','Mac_address':'00:0A:95:9D:68:16'},
'router8': {'Sapid': 122344,'Loopback':'127.0.0.1','Hostname':'localhost','Mac_address':'00:0A:95:9D:68:16'},
'router9': {'Sapid': 122344,'Loopback':'127.0.0.1','Hostname':'localhost','Mac_address':'00:0A:95:9D:68:16'},
'router10': {'Sapid': 122344,'Loopback':'127.0.0.1','Hostname':'localhost','Mac_address':'00:0A:95:9D:68:16'},
'router11': {'Sapid': 122344,'Loopback':'127.0.0.1','Hostname':'localhost','Mac_address':'00:0A:95:9D:68:16'},
'router12': {'Sapid': 122344,'Loopback':'127.0.0.1','Hostname':'localhost','Mac_address':'00:0A:95:9D:68:16'},
'router13': {'Sapid': 122344,'Loopback':'127.0.0.1','Hostname':'localhost','Mac_address':'00:0A:95:9D:68:16'},
'router14': {'Sapid': 122344,'Loopback':'127.0.0.1','Hostname':'localhost','Mac_address':'00:0A:95:9D:68:16'},
'router15': {'Sapid': 122344,'Loopback':'127.0.0.1','Hostname':'localhost','Mac_address':'00:0A:95:9D:68:16'},
'router16': {'Sapid': 122344,'Loopback':'127.0.0.1','Hostname':'localhost','Mac_address':'00:0A:95:9D:68:16'},
'router17': {'Sapid': 122344,'Loopback':'127.0.0.1','Hostname':'localhost','Mac_address':'00:0A:95:9D:68:16'},
'router18': {'Sapid': 122344,'Loopback':'127.0.0.1','Hostname':'localhost','Mac_address':'00:0A:95:9D:68:16'},
'router19': {'Sapid': 122344,'Loopback':'127.0.0.1','Hostname':'localhost','Mac_address':'00:0A:95:9D:68:16'},
'router20': {'Sapid': 122344,'Loopback':'127.0.0.1','Hostname':'localhost','Mac_address':'00:0A:95:9D:68:16'},
'router21': {'Sapid': 122344,'Loopback':'127.0.0.1','Hostname':'localhost','Mac_address':'00:0A:95:9D:68:16'},
'router22': {'Sapid': 122344,'Loopback':'127.0.0.1','Hostname':'localhost','Mac_address':'00:0A:95:9D:68:16'},
'router23': {'Sapid': 122344,'Loopback':'127.0.0.1','Hostname':'localhost','Mac_address':'00:0A:95:9D:68:16'}
            }

#opt=int(input"Enter the number of records to be displayed "))
n=int(input("enter the number of records to display : "))
print("Sapid" + "\t\t" + "Loopback" + "\t\t" + "Hostaname" + "\t\t" + "Mac_address" + "\t\t")
def get_all_values(Routers):
    for key, value in Routers.items():
        if type(value) is dict:
            get_all_values(value)
        else:
            print(value, end="\t\t")

get_all_values(Routers)


