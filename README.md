# interaction-grader
Python package to help grade test questions (interactions) using fuzzy match and phoneme replacement.

The Answer class can be used to check if an answer is basically identical to the desired answer except 
for misspellings.

  
```Python
from interactiongrader import Answer

ans = Answer('Joaquim Phoenix')  
if ans.is_misspelling('Joakim Pheonix'):  
    print('Correct Answer')  
```

Package Dependencies:  
- fuzzywuzzy  
- python-Levenshtein  
- numpy
- pandas  
- random  
- enum  