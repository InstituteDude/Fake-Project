def Encrypt(filename, key):
	file = open(filename,"rb")
	data= file.read()
	file.close()

	data=bytearray(data)
	for index, value in enumerate(data):
		data[index] = value ^ key

	file=open("CC-" + filename, "wb")
	file.write(data)
	file.close()

def Decrypt(filename, key):
	file = open(filename,"rb")
	data= file.read()
	file.close()

	data=bytearray(data)
	for index, value in enumerate(data):
		data[index] = value ^ key

	file=open(filename, "wb")
	file.write(data)
	file.close()



choice = ""
while choice != "3":
	print("Pilih opsi yang kamu mau > ")
	print("1. Ingin mengenkripsi file ")
	print("2. Ingin mendekripsi file")
	print("3. Keluar")
	choice =input()
	if choice == "1" or choice == "2":
		key= int(input("Enter a key as int! >\n"))
		filename=input("Enter filename with extension:\n")
	if choice == "1":
		Encrypt(filename, key)
	if choice == "2":
		Decrypt(filename, key)
		
