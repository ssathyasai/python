def cal_notes(amount):
    twoh_notes,fiveh_notes,twok_notes,hun_notes,fif_notes,twenty_notes,ten_notes=0,0,0,0,0,0,0
    if(amount>=2000):
        twok_notes=amount//2000
        amount=amount%2000
    if(amount>=500):
        fiveh_notes=amount//500
        amount=amount%500
    if(amount>=200):
        twoh_notes=amount//200
        amount=amount%200
    if(amount>=100):
        hun_notes=amount//100
        amount=amount%100
    if(amount>=50):
        fif_notes=amount//50
        amount=amount%50
    if(amount>=20):
        twenty_notes=amount//20
        amount=amount%20
    if(amount>=10):
        ten_notes=amount//10
        amount=amount%10
    
    print("2000 notes are {} 500 Notes are {}, 200 Notes are {},100 notes are {},50 notes are {},20 Notes are {},10 notes are{} ".format(twok_notes,fiveh_notes,twoh_notes,hun_notes,fif_notes,twenty_notes,ten_notes))
amount=int(input())
cal_notes(amount)