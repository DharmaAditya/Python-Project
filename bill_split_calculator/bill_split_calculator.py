print("Bill Split Calculator")

bill_amount = float(input('Masukkan nilai bon:'))
tip_percentage = float(input('Masukkan tipnya:'))
number_of_people = int(input('Berapa banyak orang:'))

tip_amount = (tip_percentage / 100) * bill_amount
total_amount = bill_amount + tip_amount 
amount_per_person = total_amount / number_of_people

print(f"Total (including tip): ${total_amount}")
print(f"Each person pays: ${amount_per_person}")