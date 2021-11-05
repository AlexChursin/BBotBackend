from ninja import Schema
from ninja.orm import create_schema
from .models import NavigationDisplay, NavigationButtons, ContentCategory, Content


NavigationDisplay = create_schema(NavigationDisplay, depth=1)
NavigationButtons = create_schema(NavigationButtons)
ContentCategory = create_schema(ContentCategory)
Content = create_schema(Content)

