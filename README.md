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
An sample script is in example.py.

python interactiongrader/example.py

Package Dependencies: See requirments.txt

pip install -r requirements.txt