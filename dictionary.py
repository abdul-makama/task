print("DICTIONARY")
a = 5
while a!=0:
    print("Enter Word")
    d = {'database': 'database is an organized collection of related data', 'computer' : 'computer is an electronic device', 'magnet':'magnet is a piece of metal that attract small piece of metal towards it', 'mathematics':'maths is expression of numbers and variables','school':'school is a place where we learn','botany':'botany is the study of plants','zoology':'zoology is the study of animals'}
    word = input()
    word = str(word)
    word = d.get(word)
    print(word)
    a = a + 1

    
    
 
