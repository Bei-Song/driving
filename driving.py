country = input ('請問您哪國人：')
age = input ('請問您幾歲：')
age = int(age)
if country == '台灣':
	if age >= 18 :
		print ('那你可以考駕照嚕')
	else:
		print ('你還不考駕照喔')
elif country == '美國':
	if age >= 16:
		print ('你可以考駕照喔')
	else:
		print ('你還不能考駕照喔')

