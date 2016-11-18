Plugin for CudaText.
It allows to format tables in Markdown docs, using Python code from https://github.com/bitwiser73/MarkdownTableFormatter
If selection is made (only normal selection supported) then only selection is formatted, otherwise entire file is formatted.

Example, from:
  |   Tables        | Are       | Cool  |
  |:-------------|:-----------:|-----:|
   | col 3 is      | right-aligned | $1600 |  
   col 2 is      | centered|   $12  
  | zebrà stripes | are neat      |    $1 |  
  |||    $2 |  

to:
  | Tables        |      Are      |  Cool |
  |:--------------|:-------------:|------:|
  | col 3 is      | right-aligned | $1600 |
  | col 2 is      |   centered    |   $12 |
  | zebrà stripes |   are neat    |    $1 |
  |               |               |    $2 |

Plugin has few commands in menu "Plugins".
Plugin has configuration file, which can be edited using two "Configure" commands.

  "Configure" opens config-file from plugin's folder, which is used when local file doesn't exist.
  "Configure (local)" opens config-file from the folder of currently active editor file. If local file doesn't exist, command suggests to copy global file into local name, and then opens it. 

Author: Alexey T.
License: MIT
