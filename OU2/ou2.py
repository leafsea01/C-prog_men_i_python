# Jude competition
# 3- 10 Juges 



def main():
    
    programinformation()
    Judges = number_of_judges()
    Sccore = [[0] * Judges]
    Sccore = score_judges(Judges,Sccore)
    
    load_scorre(Judges, Sccore)
    min,max, average = min_max(Judges, Sccore)

    final_result(min,max,average,Judges)



    
    




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
        print("Scorre frome judge",i+1,": ",end="")
        Scorre[0][i] = float(input())

    return Scorre

def load_scorre (Judges, scorre):
    print("Scorre loaded:")

    for i in range(Judges):
        print("Judge", i+1,"sccore is:",scorre[0][i])


def min_max(Judges, scorre):
    min = scorre[0][0]
    max = scorre[0][0]
    average = 0

    for i in range(Judges):

        if min > scorre[0][i]:
            min = scorre[0][i]


        if max < scorre[0][i]:
            max = scorre[0][i]

        average = average + scorre[0][i]

    return min,max,(average -min -max)/(Judges - 2)

def final_result(min,max,average, Judges):
    print("The final result are : ",end="")
    print("the average sccore is",average,end="")
    print(", the min sccore was",min,end="")
    print(", the max sccore was",max,end="")
    print(", the number of judges was", Judges, "but only from", Judges - 2, "judges did the sccore counted in the final sccore")






if __name__ == "__main__":

    main()

