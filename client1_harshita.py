
###CLIENTS SIDE
###CLIENT NO:2  SIDE


#Python TCP Client B
import socket

host = socket.gethostname()
port=2005
BUFFER_SIZE=2000
MESSAGE = input("Enter your option:\n1.Ticket Booking\n2.Lost and Found\n3.Food Menu\n4.Changes & Cancellation\n5.Feedback\n6.Flight Status\n7.Travel with pets\n8.Enquiry\n9.SMS Notification\n10.Special Assistance\n11.In-Flight Shopping\n12.Rent a Car\nEnter \'exit\' to quit\n")
deets=""
tcpClientB = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
tcpClientB.connect((host,port))

while MESSAGE!= 'exit':
	tcpClientB.send(bytes(MESSAGE,'utf-8'))
	data= tcpClientB.recv(BUFFER_SIZE)
	data.decode("utf-8")
	print (data)
	if(MESSAGE=='1'):		
		name=input()
		source=input()
		destination=input()
		date=input()
		deets=name+","+source+","+destination+","+date
		print(deets)
		tcpClientB.send(bytes(deets,'utf-8'))
		data= tcpClientB.recv(BUFFER_SIZE)
		data.decode("utf-8")
		print (data)
		#if(data=="Invalid Format! Resend")
			#continue
	elif(MESSAGE=='2'):
		option=input()
		tcpClientB.send(bytes(option,'utf-8'))
		data=tcpClientB.recv(2048)
		data.decode("utf-8")
		print (data)
		baggage=input()
		tcpClientB.send(bytes(baggage,'utf-8'))
		data= tcpClientB.recv(BUFFER_SIZE)
		data.decode("utf-8")
		print (data)
		
	elif(MESSAGE=='3'):
		opt=input()
		tcpClientB.send(bytes(opt,'utf-8'))
		data= tcpClientB.recv(BUFFER_SIZE)
		data.decode("utf-8")
		print(data)
		paytm=input()
		tcpClientB.send(bytes(paytm,'utf-8'))
		data= tcpClientB.recv(BUFFER_SIZE)
		data.decode("utf-8")
		print(data)
	elif(MESSAGE=='4'):
		name=input()
		source=input()
		destination=input()
		date=input()
		deets=name+","+source+","+destination+","+date
		print(deets)
		tcpClientB.send(bytes(deets,'utf-8'))
		data= tcpClientB.recv(BUFFER_SIZE)
		data.decode("utf-8")
		print (data)
	elif(MESSAGE=='5'):
		stars=input()
		tcpClientB.send(bytes(stars,'utf-8'))
		data= tcpClientB.recv(BUFFER_SIZE)
		data.decode("utf-8")
		print (data)
		feedback=input()
		tcpClientB.send(bytes(feedback,'utf-8'))
		data= tcpClientB.recv(BUFFER_SIZE)
		data.decode("utf-8")
		print (data)
	elif(MESSAGE=='6'):		#flight status
		source=input()
		destination=input()
		date=input()
		deets=source+","+destination+","+date
		print(deets)
		tcpClientB.send(bytes(deets,'utf-8'))
		data= tcpClientB.recv(BUFFER_SIZE)
		data.decode("utf-8")
		print (data)
		
	elif(MESSAGE=='7'):                #pets
		option=input()
		tcpClientB.send(bytes(option,'utf-8'))
		data=tcpClientB.recv(2048)
		data.decode("utf-8")
		print (data)
		
	elif(MESSAGE=='8'):
		opt=input()                    #enquiry
		tcpClientB.send(bytes(opt,'utf-8'))
		data= tcpClientB.recv(BUFFER_SIZE)
		data.decode("utf-8")
		print (data)
		
		if opt=='1':
			name=input()
			query=input()
			final=name+","+query
			tcpClientB.send(bytes(final,"utf-8"))
			data=tcpClientB.recv(BUFFER_SIZE)
			data.decode('utf-8')
			print(data)
		elif(opt=='2'):
			name=input()
			tcpClientB.send(bytes(name,"utf-8"))
			data=tcpClientB.recv(BUFFER_SIZE)
			data.decode('utf-8')
			if(data==b'No query found!'):
				print(data)
			elif(data==b'Invalid entry. Please enter again.'):
				print(data)
			else:
				print(data)
		else:
			print("Invalid entry!")	
		
		
	elif(MESSAGE=='9'):		
		name=input()
		source=input()
		destination=input()
		date=input()
		deets=name+","+source+","+destination+","+date
		print(deets)
		tcpClientB.send(bytes(deets,'utf-8'))
		data= tcpClientB.recv(BUFFER_SIZE)
		data.decode("utf-8")
		#print (data)
		if(data==b'Sorry, no booking found under the entered credentials.'):
			print(data)
		elif(data==b'Invalid Format! Resend'):
			print(data)
		else:
			print(data)
			number=input()
			tcpClientB.send(bytes(number,'utf-8'))
			data= tcpClientB.recv(BUFFER_SIZE)
			data.decode("utf-8")
			print (data)
		"""name=input()
		src=input()
		4dest=input()
		date=input()
		deets=name+","+src+","+dest+","+date
		print(deets)
		tcpClientB.send(bytes(deets,"utf-8"))
		data=tcpClentB.recv(BUFFER_SIZE)
		"""
		
	
	

	elif(MESSAGE=='10'):		
			name=input()
			source=input()
			destination=input()
			date=input()
			deets=name+","+source+","+destination+","+date
			print(deets)
			tcpClientB.send(bytes(deets,'utf-8'))
			data= tcpClientB.recv(BUFFER_SIZE)
			data.decode("utf-8")
			#print (data)
			if(data==b'Sorry, no booking found under the entered credentials.'):
				print(data)
			elif(data==b'Invalid Format! Resend'):
				print(data)
			else:
				print(data)
				assistance=input()
				tcpClientB.send(bytes(assistance,'utf-8'))
				data= tcpClientB.recv(BUFFER_SIZE)
				data.decode("utf-8")
				print (data)
	


	elif(MESSAGE=='11'):
			op=input()
			tcpClientB.send(bytes(op,'utf-8'))
			data= tcpClientB.recv(BUFFER_SIZE)
			data.decode("utf-8")
			print(data)
			paytms=input()
			tcpClientB.send(bytes(paytms,'utf-8'))
			data= tcpClientB.recv(BUFFER_SIZE)
			data.decode("utf-8")
			print(data)

	elif(MESSAGE=='12'):
			name=input()
			tcpClientB.send(bytes(name,"utf-8"))
			data= tcpClientB.recv(BUFFER_SIZE)
			data.decode("utf-8")
			print(data)
			option1=input()
			tcpClientB.send(bytes(option1,'utf-8'))
			data= tcpClientB.recv(BUFFER_SIZE)
			data.decode("utf-8")
			print(data)
			phno=input()
			tcpClientB.send(bytes(phno,'utf-8'))
			data= tcpClientB.recv(BUFFER_SIZE)
			data.decode("utf-8")
			print(data)
		

		
	MESSAGE = input ("tcpClientB : Enter message to continue /Enter exit:")

tcpClientB.close()

