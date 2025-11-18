"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Nursery & Kindergarten application schema
class Application(BaseModel):
    """
    Applications collection schema
    Collection name: "application"
    """
    child_name: str = Field(..., description="Child's full name")
    dob: str = Field(..., description="Date of birth (YYYY-MM-DD)")
    gender: Optional[Literal['Male','Female','Non-binary','Prefer not to say']] = Field(None)
    program: Literal['Nursery', 'Pre-K', 'Kindergarten'] = Field(..., description="Program applying for")
    start_term: Literal['Fall', 'Winter', 'Spring', 'Summer'] = Field(..., description="Intended start term")

    parent_name: str = Field(..., description="Primary guardian's name")
    email: EmailStr = Field(..., description="Contact email")
    phone: str = Field(..., description="Contact phone")
    address: Optional[str] = Field(None, description="Home address")

    message: Optional[str] = Field(None, description="Additional notes")
    consent: bool = Field(..., description="Consent to store and process data for admission purposes")

    status: Literal['submitted', 'reviewed', 'accepted', 'waitlisted', 'rejected'] = Field(
        'submitted', description="Application status"
    )
