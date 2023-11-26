import psutil 
#შემოვაიმპორტეთ პითონის ერთ-ერთი ბიბლიოთეკა, რომელიც შესაძლებლობას გვაძლევს მივიღოთ ინფორმაცია პროცესორის მუშაობაზე(ჩემს შემთხვევაშ)

def cpuRandomNumbers(): 
    CPUtimes = psutil.cpu_times() 
    #გვაძლევს ინფორმაციას პროცესორზე, თუ დროის რა რაოდენობა გაატარა მან სხვადასხვა მდგომარეობაში
    intRandomNumber = round((CPUtimes.user + CPUtimes.system + CPUtimes.idle) % 2**15 + 2**15) 
    '''
    მიღებულ პარამეტრებს ვუმატებთ ერთმანეთს რანდომ რიცხვის მისაღებად, მაგრამ რიცხვი რომ არ აღემატებოდეს 
    ან პატარა იყოს 16 ბიტზე 2**15ის ნაშთიან გაყოფას და დამატებას ვიყენებ
    '''
    binRandomNumber = bin(intRandomNumber)[2:] 
    #მიღებული რიცხვი გადავიყვანე ათობითიდან ორობითში 0b-ის გარეშე. 
    print("decimal random number ", intRandomNumber)
    print("binary random number", binRandomNumber)
cpuRandomNumbers()
# print(CPUtimes)

# print(intRandomNumber)
# print(binRandomNumber)