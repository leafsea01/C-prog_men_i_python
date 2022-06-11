# Jude competition
# 3- 10 Juges 
def main():
    
    programinformation()
    Judges = number_of_judges()
    Sccore = [[None] * Judges]
    Sccore = score_judges(Judges,Sccore)
    print(Sccore)

    
    




def programinformation():
    massage = "Programinformation"
    massage1 = "The program reads in the number of judges and the score from each judege"
    massage2 = "Then it calculates the avrage score without regard to the higest and lowest judege score"
    massage3 = "Finally it prints the results (the higest, the lowest, and the avrage score). "
    print(massage, massage1, massage2, massage3)

def number_of_judges():
    Nr_judes = 0
    while Nr_judes < 3 or Nr_judes > 10:

        Nr_judes = float(input("Enter the number of judges (3-10 judges): "))
        Nr_judes = int(Nr_judes)
    return Nr_judes

def score_judges(Judges, Scorre):

    for i in range(0,Judges,1):
        print(i)
        print(Scorre)
        Scorre[0][i] = float(input("Score for jude"))

    return Scorre






main()

