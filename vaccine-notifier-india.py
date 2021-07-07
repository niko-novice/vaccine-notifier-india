import requests
import smtplib

count =0
res_count =2
dose_available = 0
available_centers={}
pincode = 425001 # Please enter your preferred destination's pincode
dose_no = 2 # Please enter the required dose.1 or 2
date_1= "08-07-2021"#Please enter the preferred date of the booking in "dd-mm-yyyy" format
date_2="09-07-2021"#Please enter any other preferred date of the booking in "dd-mm-yyyy" format


while count==0:
	if res_count%2==0:
		response = requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={date_1}")
		res_count =res_count +1
	else:
		response = requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={date_2}")
		res_count =res_count +1

	mylist = (response.json())
	#print(mylist.get(sessions))
	#print(mylist["sessions"])
	
	if mylist["sessions"] == []:
		print(f"emp{res_count}")
	else:
		for i in mylist["sessions"]:
			if (i[f"available_capacity_dose{dose_no}"])>0:
				available_centers[f'{i["name"]}'] = i[f"available_capacity_dose{dose_no}"]
				dose_available =dose_available + (i[f"available_capacity_dose{dose_no}"])
			

		if dose_available>0:
			print("Vaccines are availble")
			sender_email = "xyz@gmail.com" # Please enter sender's gmail id. Disabling security in google preferences required
			rec_email="receiver@anyemail.com" # Please enter receiver's any email id.
			password = "Sender Email's Password"  #Sender email password
			message= f"Vaccines are available at\n{available_centers}"
			server = smtplib.SMTP_SSL('smtp.gmail.com',465)
			server.login(sender_email,password)
			print("login success")
			server.sendmail(sender_email,rec_email,message)
			print("Email has been sent to receiver")
			server.quit()
			print(available_centers)
			count=count+1
		else:
			print(f"booked{res_count}")
