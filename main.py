def calculateMoney(ticket_count):
   
    if ticket_count < 0:
        return "ইনপুট সংখ্যাটি অস্বীকার্য"

    
    total_income = ticket_count * 120
    total_expense = 500 + (8 * 50)
    profit = total_income - total_expense

    return profit


ticket_count = int(input("টিকেট সংখ্যা দিন: "))


print("বেকার ভাইর কাছে বাকি থাকা টাকার পরিমাণ:", calculateMoney(ticket_count))
print('sayem')
