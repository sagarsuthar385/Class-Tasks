class studentclass:
    name=''
    Institude_name=''
    Class=''
    contact_no=''
    email=''
    score=''
    city=''
 
    dict={}
    def create_student(self,name,Institude_name,Class,contact_no,email,score,city):
        innerdict={}
        self.name=name
        self.Institude_name=Institude_name
        self.Class=Class
        self.contact_no=contact_no
        self.email=email
        self.score=score
        self.city=city

        innerdict['Institude_name']=self.Institude_name
        innerdict['Class']=self.Class
        innerdict['contact_no']=self.contact_no
        innerdict['email']=self.email
        innerdict['score']=self.score
        innerdict['city']=self.city
        self.dict[name]=innerdict
        print(self.dict)