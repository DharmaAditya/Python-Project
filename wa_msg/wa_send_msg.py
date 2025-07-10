import pywhatkit as pwk

phone_number = input("Masukkan no telp: ")
message = "Hello"
hour = int(input("Masukkan jam (format 24 jam): "))
minute = int(input("Masukkan menit: "))

pwk.sendwhatmsg(phone_number, message, hour, minute)