
import sys
from greetings import hello,bye

hello(sys.argv[1])
bye(sys.argv[2])





"""

import sys
import greetings

greetings.hello(sys.argv[1])
greetings.bye(sys.argv[1])
"""

"""

if the code we r importing from doesnt use below block we get error o/p or mixed output
##############################
#   if __name__="__main__"   #
#      main()                #
#                            #
#                            #
##############################
o/p-->
hello, sai
bye, sai
hello, sai

"""