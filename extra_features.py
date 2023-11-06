import re
class Extras:

    def __init__(self, text):
        self.text=text

    #Does the number of digits in a message relate to spam
    def count_digits(self):
        num_digits = 0
        for char in self.text:
            if char.isdigit():
                num_digits+=1
        return num_digits/len(self.text)


    #Does the number of Capital letters help in determing the spam
    def count_upppercase(self):
        upper_case = 0
        for char in self.text:
            if char.isupper():
                upper_case+=1
        return upper_case/len(self.text)

    #Count the number of special characters 
    def count_special_characters(self):
      """Counts the number of special characters in the given text."""
      special_character_pattern = r"[^\w\s]"
      matches = re.findall(special_character_pattern, self.text)
      return len(matches)

    #Count the number of hyperlinks
    

    def count_hyperlinks(self):
      
      hyperlink_pattern = r"(https?://[^\s]+)"
      matches = re.findall(hyperlink_pattern, self.text)
      return len(matches)

