import colander


#---Class to display the member form---#
class MemberSchema(colander.Schema):   
    first_name = colander.SchemaNode(colander.String())
    middle_name = colander.SchemaNode(colander.String())
    last_name = colander.SchemaNode(colander.String())
    
    birthdate = colander.SchemaNode(colander.Date())
    age = colander.SchemaNode(colander.Integer())
    
    address_1 = colander.SchemaNode(colander.String(), title='Address (1st Line)')
    address_2 = colander.SchemaNode(colander.String(), title = 'Address (2nd Line)')
    city = colander.SchemaNode(colander.String())
    post_number = colander.SchemaNode(colander.Integer())

#class MemberTemplate(IMemberTemplate):
        
#class Member(Object):
    
    