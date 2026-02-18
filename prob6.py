p1= 'Make a lot of money '
p2= 'buy now'
p3=  'click this'
message=input("enter the message:")
if((p1 in message) or(p2 in message) or (p3 in message)):
    print("this message is a spam")
else:
    print("this message is not spam")