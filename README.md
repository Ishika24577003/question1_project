# question1_project
Read Patterns from the Query File 
  Open the query file data/to_select.tsv in read mode ('r') using the open function.
  Read the file line by line using a for loop or the readlines method. 
  Strip each line of whitespace characters using the strip method.
  Add each stripped line to a set or list data structure to allow for efficient lookups
Read the Data File
  Open the compressed data file data/q1_data.tsv.gz in read mode ('r') using the gzip module.
  Use the readline method to read the file line by line, which allows us to handle large files without loading the entire file into memory.
 Process Each Line 
 Print the matching lines to standard output using the print function
