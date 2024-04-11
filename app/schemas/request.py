from pydantic import BaseModel, Field


class IrisReq(BaseModel):
   sepal_length: float = Field(..., example=5.1,
                                                        description="Sepal length")
   sepal_width: float = Field(..., example=3.5,
                                                      description="Sepal width")
   petal_length: float = Field(..., example=1.4,
                                                       description="Petal length")
   petal_width: float = Field(..., example=0.2,
                                                     description="Petal width")

