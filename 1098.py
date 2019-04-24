# -*- coding: utf-8 -*-

from math import trunc

j = 1
i = 0

while i < 1.8:
    if (i - trunc(i)) == 0:
        print('I=' + str("%.0f"% i) + ' J=' + str("%.0f"% j))
        print('I=' + str("%.0f"% i) + ' J=' + str("%.0f"% (j+1)))
        print('I=' + str("%.0f"% i) + ' J=' + str("%.0f"% (j+2)))
    else:
        print('I=' + str("%.1f"% i) + ' J=' + str("%.1f"% j))
        print('I=' + str("%.1f"% i) + ' J=' + str("%.1f"% (j+1)))
        print('I=' + str("%.1f"% i) + ' J=' + str("%.1f"% (j+2)))
    j += 0.2
    i += 0.2
    
print('I=2 J=3')
print('I=2 J=4')
print('I=2 J=5')