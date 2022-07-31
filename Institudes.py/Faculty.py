from tokenize import Number


class facultyclass:
    name=''
    position=''
    subject=''
    contact_no=''
    email=''
    score=''
    city=''
 
    dict={}
    def create_faculty(self,name,position,subject,contact_no,email,score,city):
        innerdict={}
        self.name=name
        self.position=position
        self.subject=subject
        self.contact_no=contact_no
        self.email=email
        self.score=score
        self.city=city

        innerdict['position']=self.position
        innerdict['subject']=self.subject
        innerdict['contact_no']=self.contact_no
        innerdict['email']=self.email
        innerdict['score']=self.score
        innerdict['city']=self.city
        self.dict[name]=innerdict
        print(self.dict)


