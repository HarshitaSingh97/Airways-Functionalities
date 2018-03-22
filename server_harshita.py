'''
-AIRWAYS

SRS

1.Book (online) tickets.
2.3.[categories:flights and classes]
4.Allot seats.
5.Luggage management (YES/NO) ?
6.Services : catering; magazines/newspapers ; drinks 
7.Immigration
8./*shopping*/   Assign pilots to respective flights
9.Restaurants inside the airport
10.Cancelling tickets and refunds
11.time slot allottment of runways for airplanes
12.airport ongate parking 





Concepts used: 1.Threads and system calls(select() must be studied for this.)
1 terminal as server and 2 terminals as clients.



'''


###SERVER SIDE


import random
import socket
from threading import Thread
from socketserver import ThreadingMixIn
import sys
'''available=[["Bangalore","Hubli","12-12-2017",5],["Bangalore","Hubli","15-12-2017",5],["Mumbai","Delhi","01-01-2018",5],["Mumbai","Delhi","23-12-2017",5],["Bangalore","Delhi","19-12-2017",5],["Bangalore","Delhi","31-12-2017",5]]
'''
lost=[]
found=[]
feedback=[]		
booking=[]
stars=[0,0,0,0,0]
#ind=0
#flag=0

pet_request=[]
main_enquiry=[]



MESSAGE="noexit"
#Multithreaded Python server: TCP Server Socket Thread Pool
class ClientThread(Thread):

	def __init__(self,ip,port):
		Thread.__init__(self)
		self.ip = ip
		self.port = port
		print (" [+] New server socket thread started for " + ip + ":" + str(port))

	def run(self):
		var=True
		available=[[b"Bangalore",b"Hubli",b"12-12-2017",5],[b"Bangalore",b"Hubli","15-12-2017",5],[b"Mumbai",b"Delhi",b"01-01-2018",5],[b"Mumbai",b"Delhi",b"23-12-2017",5],[b"Bangalore",b"Delhi",b"19-12-2017",5],[b"Bangalore",b"Delhi",b"31-12-2017",5]]
		
		
		flight=[[b"Bangalore",b"Hubli",b"12-12-2017"],[b"Bangalore",b"Hubli","15-12-2017"],[b"Mumbai",b"Delhi",b"01-01-2018"],[b"Mumbai",b"Delhi",b"23-12-2017"],[b"Bangalore",b"Delhi",b"19-12-2017"],[b"Bangalore",b"Delhi",b"31-12-2017"]]
		
		pets=[b"Cat",b"Dog",b"Bird"]
		
		
		
		
		while var:
			data=conn.recv(2048)
			data.decode("utf-8")
			print ("Server received data : ", data)
			if data==b'1': #book ticket
				flag=0
				MESSAGE="Enter Name, source, destination, date"				
				conn.send(bytes(MESSAGE,'utf-8'))
				data=conn.recv(2048)
				data.decode("utf-8")
				deets=data.split(b',')
				if(len(deets)==4):
					for i in available:					
						if(deets[1]==i[0] and deets[2]==i[1] and deets[3]==i[2] and i[3]!=0):
							flag=1	
							i[3]=i[3]-1
							booking.append(deets)
							MESSAGE="Booking confirmed!"
							conn.send(bytes(MESSAGE,'utf-8'))
							break
				if (len(deets)==4 and flag==0):
					MESSAGE="Booking not possible"
					conn.send(bytes(MESSAGE,'utf-8'))
						
				elif(flag==0):
					MESSAGE="Invalid Format! Resend"
					conn.send(bytes(MESSAGE,'utf-8'))
					
			elif data==b'2': #Lost and found
				flag=0
				MESSAGE="1.Report someone else's lost baggage\n2.Find your lost baggage"
				conn.send(bytes(MESSAGE,'utf-8'))
				data=conn.recv(2048)
				data.decode("utf-8")
				if data==b'1':
					MESSAGE="Enter baggage number"
					conn.send(bytes(MESSAGE,'utf-8'))
					data=conn.recv(2048)
					data.decode("utf-8")
					found.append(data)
					MESSAGE="Thank you!"
					conn.send(bytes(MESSAGE,'utf-8'))
					for j in lost:
						if(j==data):
							lost.remove(data)
							
				if data==b'2':
					MESSAGE="Enter baggage number"
					conn.send(bytes(MESSAGE,'utf-8'))
					data=conn.recv(2048)
					data.decode("utf-8")
					for i in found:
						if(i==data):
							flag=1
							MESSAGE="This baggage has been found! Please collect it at the help desk!"
							conn.send(bytes(MESSAGE,'utf-8'))
							found.remove(data)
							
					if(flag==0):
						lost.append(data)
						MESSAGE="Sorry! The baggage hasn't been found yet! Please check back later."
						conn.send(bytes(MESSAGE,'utf-8'))
					
					
					
			elif data==b'3': #Food Menu
				flag=0
				Food=[[b"1","Veg Burger","150"],[b"2","Veg Katti roll","110"],[b"3","KFC chicken Rice Bowl","250"],[b"4","Double chicken Roll","130"],[b"5","Diet coke","50"],[b"6","Veg Sandwich","90"]]
				MESSAGE="Item no. Item Price(Rs)\n1 Veg Burger 150\n2 Veg Katti roll 110\n3 KFC chicken Rice Bowl 250\n4 Double chicken Roll 130\n5 Diet coke 50\n6 Veg Sandwich 90"
				conn.send(bytes(MESSAGE,'utf-8'))
				data=conn.recv(2048)
				data.decode("utf-8")
				print(data)
				for i in Food:
					if(data==i[0]):
						flag=1
						conn.send(bytes("Enter Paytm number",'utf-8'))
						data=conn.recv(2048)
						data.decode("utf-8")
						MESSAGE=i[1]+" Ordered,"+i[2]+" Rs. deducted from your account"
						conn.send(bytes(MESSAGE,'utf-8'))
						break
				if(flag==0):
					MESSAGE="Could not process request"
					conn.send(bytes(MESSAGE,'utf-8'))
			elif data==b'4': #Changes and Cancellation
				flag=0
				MESSAGE="Enter Name, source, destination and date"				
				conn.send(bytes(MESSAGE,'utf-8'))
				data=conn.recv(2048)
				data.decode("utf-8")
				deets=data.split(b',')
				if(len(deets)==4):
					for i in booking:					
						if(deets[0]==i[0] and deets[1]==i[1] and deets[2]==i[2] and deets[3]==i[3]):
							for j in available:
								if(deets[1]==j[0] and deets[2]==j[1] and deets[3]==j[2]):
									flag=1	
									j[3]=j[3]+1
									booking.remove(deets)
									MESSAGE="Booking cancelled!"
									conn.send(bytes(MESSAGE,'utf-8'))
									break
						if(flag==1):
							break
				if (len(deets)==4 and flag==0):
					MESSAGE="Booking cannot be cancelled"
					conn.send(bytes(MESSAGE,'utf-8'))
						
				elif(flag==0):
					MESSAGE="Invalid Format! Resend"
					conn.send(bytes(MESSAGE,'utf-8'))
				
			elif data==b'5': #Feedback
				MESSAGE="Let's start with the rating (1 to 5 with 1 being the worst and 5 being the best)"				
				conn.send(bytes(MESSAGE,'utf-8'))
				data=conn.recv(2048)
				data.decode("utf-8")
				if(data==b'1'):
					stars[0]+=1
				elif(data==b'2'):
					stars[1]+=1
				elif(data==b'3'):
					stars[2]+=1
				elif(data==b'4'):
					stars[3]+=1
				elif(data==b'5'):
					stars[4]+=1
				MESSAGE="Please enter your valuable feedback"				
				conn.send(bytes(MESSAGE,'utf-8'))
				data=conn.recv(2048)
				data.decode("utf-8")
				feedback.append(data)
				MESSAGE="Thank you for your valuable feedback!"				
				conn.send(bytes(MESSAGE,'utf-8'))
				feedback.append(data)
				print("Feedback: ",data)
				
			elif data==b'6': #Flight status
				flag=0
	
				MESSAGE="enter source, destination, date"				
				conn.send(bytes(MESSAGE,'utf-8'))
				data=conn.recv(2048)
				data.decode("utf-8")
				deets=data.split(b',')
				if(len(deets)==3):
					for i in available:					
						if(deets[0]==i[0] and deets[1]==i[1] and deets[2]==i[2]):
							flag=1	
							stats=["On Time","Delayed"]
							MESSAGE=random.choice(stats)
							conn.send(bytes(MESSAGE,'utf-8'))
							break
				if (len(deets)==3 and flag==0):
					MESSAGE="Details not available for the selected flight"
					conn.send(bytes(MESSAGE,'utf-8'))
						
				elif(flag==0):
					MESSAGE="Invalid Format! Resend"
					conn.send(bytes(MESSAGE,'utf-8'))
					
			elif data==b'7': #Pets
				flag=0
				MESSAGE="Enter the type of pet. Example, if you have a cat,enter Cat."
				conn.send(bytes(MESSAGE,'utf-8'))
				data=conn.recv(2048)
				data.decode("utf-8")
				for i in pets:
					if data==i :
						flag=1
						MESSAGE="Request for pet cage submitted. PLease report at help desk while checking-in."
						conn.send(bytes(MESSAGE,'utf-8'))
						break
					
				if(flag==0):
					MESSAGE="Your pet is not allowed!"
					conn.send(bytes(MESSAGE,'utf-8'))
			elif data==b'8': #Enquiry desk
				flag=0
				
				MESSAGE="1.Submit query\n2.Status of previous query.\n"
				conn.send(bytes(MESSAGE,'utf-8'))
				data=conn.recv(2048)
				data.decode("utf-8")
				if data==b'1':
					MESSAGE="Enter your first name followed by your query\n"
					conn.send(bytes(MESSAGE,'utf-8'))
					data=conn.recv(2048)
					data.decode("utf-8")
					enquiry=data.split(b',')
					if(len(enquiry)==2):
						MESSAGE="Your query has been submitted. Please check back later."
						conn.send(bytes(MESSAGE,'utf-8'))
						main_enquiry.append(enquiry)
					else:
						MESSAGE="Invalid format.Enter again."
						conn.send(bytes(MESSAGE,'utf-8'))
				elif data==b'2':
					MESSAGE="Enter first name:"
					conn.send(bytes(MESSAGE,'utf-8'))
					data=conn.recv(2048)
					data.decode("utf-8")
					flag=0
					for i in main_enquiry:
						if(data==i[0]):
							flag=1
							MESSAGE="Your query is being processed.Please check back later."
							conn.send(bytes(MESSAGE,'utf-8'))
							break
					if(flag==0):
						MESSAGE="No query found!"
						#MESSAGE='1'
						conn.send(bytes(MESSAGE,'utf-8'))
				else:
					MESSAGE="Invalid entry. Please enter again."
					#MESSAGE="2"
					conn.send(bytes(MESSAGE,'utf-8'))
				
				
				
			#####  Mobile registration
			elif data==b'9': 
				flag=0
				MESSAGE="Enter Name, source, destination, date"				
				conn.send(bytes(MESSAGE,'utf-8'))
				data=conn.recv(2048)
				data.decode("utf-8")
				deets=data.split(b',')
				if(len(deets)==4):
					for i in available:					
						if(deets[1]==i[0] and deets[2]==i[1] and deets[3]==i[2]):# and i[3]!=0):
							flag=1	
							#i[3]=i[3]-1
							#booking.append(deets)
							MESSAGE="Enter your phone number:"
							conn.send(bytes(MESSAGE,'utf-8'))
							data=conn.recv(2048)
							data.decode("utf-8")
							MESSAGE="Your number has been registered. You will now recieve updates."  
							conn.send(bytes(MESSAGE,'utf-8'))
							break
				if (len(deets)==4 and flag==0):
					#print("abc")
					MESSAGE="Sorry, no booking found under the entered credentials."
					#print("abc")
					conn.send(bytes(MESSAGE,"utf-8"))
						
				elif(flag==0):
					MESSAGE="Invalid Format! Resend"
					print("abc")
					conn.send(bytes(MESSAGE,'utf-8'))
				
			
			
			##Special Assistance
			elif data==b'10': 
				flag=0
				MESSAGE="Enter Name, source, destination, date"				
				conn.send(bytes(MESSAGE,'utf-8'))
				data=conn.recv(2048)
				data.decode("utf-8")
				deets=data.split(b',')
				if(len(deets)==4):
					for i in available:					
						if(deets[1]==i[0] and deets[2]==i[1] and deets[3]==i[2] and i[3]!=0):
							flag=1	
							i[3]=i[3]-1
							booking.append(deets)
							MESSAGE="Enter the details of the assistance you need:"
							conn.send(bytes(MESSAGE,'utf-8'))
							data=conn.recv(2048)
							data.decode("utf-8")
							MESSAGE="Your response has been noted. The help will be provided at the check-in counter."  
							conn.send(bytes(MESSAGE,'utf-8'))
							break
				if (len(deets)==4 and flag==0):
					#print("abc")
					MESSAGE="Sorry, no booking found under the entered credentials."
					#print("abc")
					conn.send(bytes(MESSAGE,"utf-8"))
						
				elif(flag==0):
					MESSAGE="Invalid Format! Resend"
					print("abc")
					conn.send(bytes(MESSAGE,'utf-8'))

			
			
			
			elif data==b'11': #In-FLight Catalogue
				flag=0
				Catalogue=[[b"1","Fragrances for Her","1500"],[b"2","Cosmetics","1100"],[b"3","Fragrances for Him","2500"],[b"4","Sunglasses","1300"],[b"5","Jewellery","2500"],[b"6","Watches for Her","1900"],[b"7","Watches for Him","2000"]]
				MESSAGE="Item no. Item Price(Rs)\n1. Fragrances for Her 1500\n2. Cosmetics 1100\n3. Fragrances for Him 2500\n4. Sunglasses 1300\n5. Jewellery 2500\n6. Watches for Her 1900\n7. Watches for Him 2000 "
				conn.send(bytes(MESSAGE,'utf-8'))
				data=conn.recv(2048)
				data.decode("utf-8")
				print(data)
				for i in Catalogue:
					if(data==i[0]):
						flag=1
						conn.send(bytes("Enter Paytm number",'utf-8'))
						data=conn.recv(2048)
						data.decode("utf-8")
						MESSAGE=i[1]+" Ordered,"+i[2]+" Rs. deducted from your account"
						conn.send(bytes(MESSAGE,'utf-8'))
						break
				if(flag==0):
					MESSAGE="Could not process request"
					conn.send(bytes(MESSAGE,'utf-8'))

			
			
			elif data==b'12': #Rent a car
				flag=0
				Car=[[b"1","Sedan","1500"],[b"2","Super Car","1100"],[b"3","Minivan","2500"],[b"4","Luxury Vehicle","1300"],[b"5","Sport Utility Vehicle","2500"],[b"6","Compact Car","1900"],[b"7","Hatchback","2000"]]
				MESSAGE="Item no. Item Price(Rs)\n1. Sedan\n2. Super Car\n3. Minivan\n4. Luxury Vehicle\n5. Sport Utility Vehicle\n6. Compact Car\n7. Hatchback"
				conn.send(bytes(MESSAGE,'utf-8'))
				data=conn.recv(2048)
				data.decode("utf-8")
				print(data)
				for i in Car:
					if(data==i[0]):
						flag=1
						#MESSAGE="Enter your name"				
						conn.send(bytes('Enter your name' ,'utf-8'))
						data=conn.recv(2048)
						data.decode("utf-8")
						conn.send(bytes('Enter your contact details','utf-8'))
						data=conn.recv(2048)
						data.decode("utf-8")
						MESSAGE=i[1]+ 'Vehicle Booked. You will be contacted by the driver when you reach your destination'
						conn.send(bytes(MESSAGE,'utf-8'))
						break
				if(flag==0):
					MESSAGE="Could not process request"
					conn.send(bytes(MESSAGE,'utf-8')) 
				


				
				
				
			'''			
			MESSAGE = input("Multithreaded Python server : Enter Response from Server/Enter exit:")
			if MESSAGE == 'exit':
				#var=False
				print("Har har")
				quit()
				#break
			#else:
				
				#print("YEELLOO!")
			'''
			#conn.send(bytes(MESSAGE,'utf-8')) #echo

#Multithreaded Python server : TCP Server Socket Program Stub

TCP_IP = '0.0.0.0' 
TCP_PORT = 2005
tot_socket=2
list_sock=[]
BUFFER_SIZE = 20 #Usualy 1024 but we need quick response
for i in range(tot_socket):
	tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
	tcpServer.setsockopt (socket.SOL_SOCKET, socket.SO_REUSEADDR ,1)
	tcpServer.bind((TCP_IP , TCP_PORT+i))
	tcpServer.listen(4)
	list_sock.append(tcpServer)
	print("server listening on %s  %d" %(TCP_IP,(TCP_PORT + i)))
	
threads=[]
while 1:
	#for j in range(len(list_sock)):
		#print("heeeer")
	print ("Multithreaded Python Server : waiting for connections from TCP Clients...")
	(conn, (ip,port)) = list_sock[0].accept()
	print("connected with " + ip + ':' + str(port))
	newthread1 = ClientThread(ip,port)
	newthread1.start()
	threads.append(newthread1)
	print ("Multithreaded Python Server : waiting for connections from TCP Clients...")
	(conn, (ip,port)) = list_sock[1].accept()
	print("connected with " + ip + ':' + str(port))
	newthread2 = ClientThread(ip,port)
	newthread2.start()
	threads.append(newthread2)
tcpServer.close()
for t in threads:
	t.join() #end







