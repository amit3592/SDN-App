#Homework 2
#Application to display Switch DPID MAC address and IP of all ports of switch and then display any of per switch stats if required
import requests
import httplib
import json 


m = requests.get('http://10.0.0.175:8080/wm/device/') #get info of all devices tracked by controller
a = 'http://10.0.0.175:8080/wm/core/switch/' #former part to second API for per switch stats
info = json.loads(m.content) #saving device info in info





y = info['devices']#storing info of array devices to y 
i=0
for i in range(0,3): #loop to display all 3 port info

	print ('Switch DPID'+ y[i]['attachmentPoint'][0]['switch'] +'port:'+y[i]['attachmentPoint'][0]['port'] +'\n' ' mac ' + y[i]['mac'][0])

	print ('IP:' +y[i]['ipv6'][0]+ ' VLAN: '+y[i]['vlan'][0]+'\n')
	i= i+1
b = info['devices'][0]['attachmentPoint'][0]['switch'] #storing switch DPID after parsing it

l=0
while (l is 0): #asking user if he wants to see per switch stats of our switch 
	t=raw_input('Do u want to see any of these per switch stats : ''\n'+'aggregate, desc, flow, group, group-desc, group-features, meter, meter-config, meter-features, port, port-desc, queue, table, features[Y/N]? ' )



	if (t=='y' or t=='Y'): #checking user input
		j=raw_input('enter the exact parameter as above you want to see next: ')
		c = '/'+j+'/json'
		n = a+b+c
		k = requests.get(n)
		z = json.loads(k.content)
		print j+'for switch' + b +'is''\n'
		print z
	p=raw_input('Do you want another parameter?[Y/N]? ')#loop to endlessly prompt for another parameter till the user does not deny
	if (p=='y' or p=='Y'):
		l=0
	else:
		l=1
		print('Thanks for using my application')

	



