#1. Middleware
#2. Service Layer
#3. Repo layer
#4. JWT
#5. API Router


#1. Routers
# Books
# HTTP handling

# 2. Services
# Business Logic

# 3. Repositry
# Database Queries

# 4. Database
# Actual Storage




# Request & Responses Schemas

# BookCreate

# id
# title
# author

# request
{
    "title": "FastApi",
    "author": "Rahul"
}

# response

{
    "id":2,
    "title": "FastApi",
    "author": "Rahul"
}



# 2. Seprate Schemas

# Request.
# create

# class BookCreate(BaseModel):
#     title:str
#     author:str


# update patch ke liye

# class BookUpdate(BaseModel):
#     title:str | None = None
#     author:str | None = None


# Response . 

# class BookResponse(BaseModel):
        # id:int  
        # title:str
        # author:str

# Why This ?  : Database se client ko return ke liye   
# 
# 

# Create Schema :   Client kya bhej skta hai  
# Update Schema : Client kya update kar skta hai

# Response schema :  Client ko kya dikhana hai