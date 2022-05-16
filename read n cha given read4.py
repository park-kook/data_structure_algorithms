
'''
Read N characters Given Read4
Given a file and assume that you can only read the file using a given method read4, 
implement a method to read n characters.

Method read4:
The API read4 reads four consecutive characters from file, then writes those characters into 
the buffer array buf4. The return value is the number of actual characters read.
Note that read4() has its own file pointer, much like FILE *fp in C

Because of the physical implementation, loading 4 bytes in DDR is faster than to load 1 byte 4 times.
On the majority of computers today, collection of 4 bytes, or 32 bits, is called a word. 
Most modern CPUs are optimized for the operations with words.
To sum up, the problem is a practical low-level question. The standard approach (Approach 1) 
to solve it using the internal buffer of 4 characters:
'''
import read4

   def read(buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        copied_chars = 0
        read_chars = 4
        buf4 = [''] * 4
        
        while copied_chars < n and read_chars == 4:
            read_chars = read4(buf4)
            
            for i in range(read_chars):
                if copied_chars == n:
                    return copied_chars
                buf[copied_chars] = buf4[i]
                copied_chars += 1
        
        return copied_chars


read("abcde",5)

read4()
