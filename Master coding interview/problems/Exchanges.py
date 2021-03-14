def Exchanges(Amount):
    Notes = [1,2,5,10,20,50,100,500,1000]
    n = len(Notes)-1
    notes_required = 0
    while(Amount):
        if Amount>=Notes[n]:
            notes_required+=Amount//Notes[n]
            Amount%=Notes[n]
        else:
            n-=1
    return notes_required

if __name__=="__main__":
    print(Exchanges(500))
