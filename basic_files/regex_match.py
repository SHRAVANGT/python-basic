#
#
#
#
#
#############################################
############################################
#
#
#
#
#regular expression are default or inbuilt functions mainly used for certian things like check for certain strinf pattern
#
#Here match regex matches start of sentence with pattern if matches then it passes otherwise none found
#
##############################################
#
#

import re

text = "the melodious song sang by girl"

pattern = r"the"

match = re.match(pattern , text)
if match:
   print("match found:",match.group())
else:
   print("not found")

