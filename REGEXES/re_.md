  .  any character except a newline
    
  *  0 or more repetitions
    
  +  1 or more repetitions
    
  ?  0 or 1 repetition
    
  {m}  m repetitions
    
  {m-n} m-n repetitions







^ --matches the start of the string

$ --matches the end of the string or
just before the newline at the end
of the string



[]===- set to include
[^]===- set to exclude





\d  decimal digit
\D  not a decimal digit
\s  whitespace characters
\S  not a whitespace character
\w  word character ... as well as
    numbers and the underscore

\W  not a word character




(\w|\s) -- either can match 
(...)=== a group
(?:...)===== non capturing version