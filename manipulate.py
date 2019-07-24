class man:
    def __init__(self,start,end,content):
        self.start=start
        self.end=end
        self.content=content

    def consume(self):
        print ('>>>>>>>>>>>>>')
        print(self.start,self.end, self.content)
    # print(event)

    def consume_more(self):
        msg='hello world'
        msg.split(' ')
        print(msg)

    def subtractedTime(self):
        start=self.start
        end=self.end
        print(start)

    def unnecesaryDigitsInTime(self):
        starttimeWithoutPlus=self.start.split('+')
        endtimeWithoutPlus=self.end.split('+')
        print('Task  :',self.content)
        print('Started at :',starttimeWithoutPlus[0])
        print('Ended at at :',endtimeWithoutPlus[0])
    
