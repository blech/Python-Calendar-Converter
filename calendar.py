# MIT Licensed 2013 Robert Greener

import roman

class Calendar(object):
 
    # Correct input "<number in month> <month> <year>"
    def to_french_revolutionary(self, date):
        # Check if date is string
        if not isinstance(date, str):
            return -1
        
        # Split date into array
        date_split = date.split()
        
        # Check to see if new array has correct length (3)
        if len(date_split) != 3:
            return -2
            
        date_dict = {
            "day": date_split[0],
            "month": date_split[1],
            "year": date_split[2]
        }
        
        # Attempting to convert day to int
        try:
            date_dict["day"] = int(date_dict["day"])
        except:
            return -3
            
        date_dict["month"] = date_dict["month"].upper()
        
        # Converting month to number and making sure that the month is infact a month
        date_dict["month"] = self.__is_month__(date_dict["month"])
        
        if not date_dict["month"]:
            return - 4
        
        # Attempting to convert the year to an int
        try:
            date_dict["year"] = int(date_dict["year"])
        except:
            return -5
        
        # Testing to see if date is after start of calendar
        if date_dict["year"] == 1792:
            if date_dict["month"] < 9:
                return -6
            elif date_dict["month"] == 9:
                if date_dict["day"] < 22:
                    return -6
        
        # Converting year to French Revolutionary
        if date_dict["month"] < 9:
            date_dict["french_year"] = date_dict["year"] - 1792
        elif date_dict["month"] == 9 and date_dict["day"] < 22:
            date_dict["french_year"] = date_dict["year"] - 1792
        else:
            date_dict["french_year"] = date_dict["year"] - 1791
        
        if date_dict["french_year"] > 4999:
            return -7
        # Converting days + month to  days_passed
        date_dict["days_passed"] = self.__days_passed__(date_dict["day"], date_dict["month"], self.__is_gregorian_leap_year__(date_dict["year"]))
        
        
        french_date = self.__to_french__(date_dict["days_passed"], date_dict["french_year"])
        return french_date
    
    def __to_french__(self, days_passed, year):
        roman_year = roman.toRoman(year)
        
        # Error Check
        if days_passed > 366:
            return -8
        
        # Look for Complementary Days
        if days_passed == 366:
            return "La Fête de la Révolution de l'Année " + roman_year + " de la Revolution"
        elif days_passed == 365:
            return "La Fête des Récompenses de l'Année " + roman_year + " de la Revolution"
        elif days_passed == 364:
            return "La Fête de l'Opinion de l'Année " + roman_year + " de la Revolution"
        elif days_passed == 363:
            return "La Fête du Travail de l'Année " + roman_year + " de la Revolution"
        elif days_passed == 362:
            return "La Fête du Génie de l'Année de l'Année " + roman_year + " de la Revolution"
        elif days_passed == 361:
            return "La Fête de la Vertu de l'Année de l'Année " + roman_year + " de la Revolution"
        
        days_in_month = days_passed % 30
        month_number = ((days_passed - days_in_month) / 30) + 1
        month_name = ""
        if days_in_month == 0:
            month_number -= 1
            days_in_month = 30
        days_in_decade = days_in_month % 10
        day_name = ""
        decade = ((days_in_month - days_in_decade) / 10) + 1
        if days_in_decade == 0:
            decade -= 1
            days_in_decade = 10
        decade_name = roman.toRoman(decade)
        
        
        if month_number == 1:
            month_name = "Vendémiaire"
        elif month_number == 2:
            month_name = "Brumaire"
        elif month_number == 3:
            month_name = "Frimaire"
        elif month_number == 4:
            month_name = "Nivôse"
        elif month_number == 5:
            month_name = "Pluviôse"
        elif month_number == 6:
            month_name = "Ventôse"
        elif month_number == 7:
            month_name = "Germinal"
        elif month_number == 8:
            month_name = "Floréal"
        elif month_number == 9:
            month_name = "Prairial"
        elif month_number == 10:
            month_name = "Messidor"
        elif month_number == 11:
            month_name = "Thermidor"
        elif month_number == 12:
            month_name = "Fructidor"
        
        if days_in_decade == 1:
            day_name = "Primidi"
        if days_in_decade == 2:
            day_name = "Duodi"
        if days_in_decade == 3:
            day_name = "Tridi"
        if days_in_decade == 4:
            day_name = "Quartidi"
        if days_in_decade == 5:
            day_name = "Quintidi"
        if days_in_decade == 6:
            day_name = "Sextidi"
        if days_in_decade == 7:
            day_name = "Septidi"
        if days_in_decade == 8:
            day_name = "Octidi"
        if days_in_decade == 9:
            day_name = "Nonidi"
        if days_in_decade == 10:
            day_name = "Décadi"
        
        return "Décade " + decade_name + ", " + day_name +" de " + month_name + " de l'Année " + roman_year + " de la Revolution."
    
    def __days_passed__(self, day, month, leap):
        days_passed = day
        
        if month < 9 or (month == 9 and day < 22):
            if month > 1:
                days_passed += 31
            if month > 2 and not leap:
                days_passed += 28
            if month > 2 and leap:
                days_passed += 29
            if month > 3:
                days_passed += 31
            if month > 4:
                days_passed += 30
            if month > 5:
                days_passed += 31
            if month > 6:
                days_passed += 30
            if month > 7:
                days_passed += 31
            if month > 8:
                days_passed += 21
            days_passed += 101
        else:
            if month == 9:
                days_passed = day - 21
            elif month == 10:
                days_passed = 9 + day
            elif month == 11:
                days_passed = 9 + 31 + day
            elif month == 12:
                days_passed = 9 + 31 + 30 + day
        return days_passed
        
    def __is_gregorian_leap_year__(self, year):
        if year % 4 == 0:
            return True
        else:
            return False
    
    def __is_month__(self, month):
        if month == "JANUARY":
            return 1
        elif month == "FEBRUARY":
            return 2
        elif month == "MARCH":
            return 3
        elif month == "APRIL":
            return 4
        elif month == "MAY":
            return 5
        elif month == "JUNE":
            return 6
        elif month == "JULY":
            return 7
        elif month == "AUGUST":
            return 8
        elif month == "SEPTEMBER":
            return 9
        elif month == "OCTOBER":
            return 10
        elif month == "NOVEMBER":
            return 11
        elif month == "DECEMBER":
            return 12
        else:
            return False