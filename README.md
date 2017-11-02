## Make Bintrees

### Easily create "Custom Tests" binary trees in the format used by popular code contest site

I find the format for binary trees used on this site to be difficult to read and 
write. So this script converts trees, expressed very simply, into the site's format.

For example, create a text file that looks like this:

    1
    2 2
    3 x x 3

to represent the tree

       1
      /  \
     2    2
    /      \
   3        3

where an 'x' represents a null child.

Pass your text file as a command-line argument to this Python script. The output will be a string suitable for the 'Input' field
in "Custom Tests -> Add Custom Test -> Add Test Case". Then put `true` or `false` into the 'Output' field,
and you should have a good test case.

This code is released under the MIT License. Please see LICENSE.txt for details.
