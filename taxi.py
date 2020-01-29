name=input()
mobile=int(input())
source=int(input())
destination=int(input())
km=destination-source
def travel():
    def nano():
        cost=km*50
        print(cost)
        return cost
    def micro():
        cost=km*40
        print(cost)
        return cost
    def mini():
        cost=km*30
        print(cost)
        return cost
    i=input()
    if(i=="nano"):
        nano()
    elif(i=="micro"):
        micro()
    else:
        mini()
    decide=input()
    if(decide=='start'):
        travel()



decide=input()
if(decide=='start'):
    travel()

