Calendar Converter converts dates from the Gregorian Calendar to the French Revolutionary Calendar (Two-Way Conversion is coming)
It uses roman.py by Mark Pilgrim
It is licensed under the MIT License

### Usage:
```python
# Import calendar.py (Must be in same dir with roman.py)
import calendar as cal


# Convert to FRC
date_in_frc = cal.Calendar().to_french_revolutionary("25 January 2012") # MUST BE IN THE FORMAT OF "<day> <month> <year>"
```