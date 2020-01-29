name=input()
mobile=int(input())
def travel():
        source=int(input())
        destination=int(input())
        kms=destination-source
        cost=kms*20
        print(mobile,'of',name,'your cost is ',cost)
decide=input()
if(decide=='start'):
        travel()
