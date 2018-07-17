# Program ParseScript" 

1) How to execute the program:

Run the command "cat input.txt | python parseScript.py > output.txt'

2) Sample Input File Format:
 
* This is an outline
 
. It's not a very good outline
 
.. I've seen better
 
.. I've seen worse
 
... I saw a really bad one back in 2008
 
* This is the second numbered item in the outline
 
. This is sub text that spans multiple lines
 
This should be included with the previous line
 
And this line too
 
.. That is more sub text
 
* Numbers
 
. Some text
 
** Lots
 
. Some more text
 
. And some more
 
*** And lots
 
. One
 
.. Two
 
... Three
 
**** Of numbers
 
. Another line
 
** Less Numbers
 
. Text
 
*** More Numbers
 
. Blah
 
* One number again
 
. The last line
 
3) Parsed Ouput File Format:
 
1 This is an outline
  + It's not a very good outline
   - I've seen better
   + I've seen worse
    - I saw a really bad one back in 2008
2 This is the second numbered item in the outline
  + This is sub text that spans multiple lines
    This should be included with the previous line
    And this line too
   - That is more sub text
3 Numbers
  - Some text
3.1 Lots
  - Some more text
  - And some more
3.1.1 And lots
  + One
   + Two
    - Three
3.1.1.1 Of numbers
  - Another line
3.2 Less Numbers
  - Text
3.2.1 More Numbers
  - Blah
4 One number again
  - The last line



