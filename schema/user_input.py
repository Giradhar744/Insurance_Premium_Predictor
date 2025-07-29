from pydantic import Field, computed_field,BaseModel,field_validator # type: ignore
from typing import Literal, Annotated
from config.city_tier import tier_1_cities, tier_2_cities



# Male a pydantic model to validate incoming data

class User_Input(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt =120, description='Age of the User')]
    weight:Annotated[float, Field(..., gt=0, description='Weight of the User')]
    height: Annotated[float, Field(..., gt=0,description='Height of the User')]
    income_lpa: Annotated[float, Field(..., gt=0, description='Income of the User in LPA')]
    smoker: Annotated[bool, Field(..., description='Is user Smoker')]
    city: Annotated[str, Field(..., description='City that the user belongs to')]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(..., description='Occupation of the User')]
    

    @field_validator('city')
    @classmethod
    def normalize_city(cls,v:str)-> str:
      v = v.strip().title()  # strip means remove the extra space before and after the city name.
      # title  make the first letter of the city capital
      return v    

    @computed_field
    @property
    def bmi(self)-> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def lifestyle_risk(self)->str:
        if self.smoker and self.bmi >30:
         return "high"
        elif self.smoker  and self.bmi>27:
         return "Medium"
        else:
         return "Low"

    @computed_field
    @property
    def age_group(self)->str:
     if self.age<25:
        return "young"
     elif self.age<45:
         return "Adult"
     elif self.age<60:
        return "Middle_Aged"
     else:
        return "Senior"
     
    @computed_field
    @property
    def city_tier(self) -> int:
     if self.city in tier_1_cities:
        return 1
     elif self.city in tier_2_cities:
        return 2
     else:
        return 3