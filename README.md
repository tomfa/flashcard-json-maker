flashcard-json-maker
====================

Small python script creating JSON out of a Q/A text file.

## USAGE:
1. Save your Q-A file as title.txt

2. run 'python simplequiz_interpreter.py title.txt'

Output will be stored in data.js. Do as you please with it(for example, see https://github.com/tomfa/distsys)

## FORMAT:

```
    Chapter 1 - Cakes and burglers. 

    Q: What's up with cakes and burglers?
    A: I don't know. Burglers be stealin' dem cakes, me guess.

    Q: Can I add empty lines?
    A: Yeah, sure. Go ahead. Anywhere, I don't mind.
    
    Q: Can my question go across multiple lines? Like... 
        this? 
    A: Yeah, that's fine. Same goes with answers. They can be a 
    thousand lines if that's your thing. Chapters can't though. 
    
    Q: What if I want to include an image in the question?
    A: Well, you can include html-tags, like <img src='b.png' />, and
    those should work neatly, given that the image is present in the page
    where you want to use the json. When I think of it, double quotes might 
    break your things, so using single quotes is probably a good idea.
```
