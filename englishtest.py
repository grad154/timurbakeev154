
count2 = 0
count = 0
 
a = int(input("Введите 1, если хотите запустить программ: ")) 

while a == 1:
    count2 = 0
    count = 0   
    answer = {
    "Hello":"привет",
    "timur":"тимур",
    "you":"ты",
    "flawless":"безупречный",
    "and":"и",
    "the best":"лучший",
    "programmer":"программист",
    "in":"в",
    "all":"все",
    "world":"мир",
    }
    for i in answer:
            q = "переведите слово", i, "на русский"
            ans = input(q)
            if ans.lower() == answer.get(i):
                count += 1
                print("верно!")
    print("Вы набрали ", count , "очков.")
    a = int(input("Введите 1, если хотите запустить программу снова: "))

