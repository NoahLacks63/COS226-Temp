## 1st Revision
```
def good_pelosi_hash(s):
    result = 0

    for i in range(len(s)):
        ascii = ord(s[i])
        result += ascii + i

    return result % 32749 
```

I tried this approach because I wanted to have both the ascii and the index effect the final value. This doesn't do great though because different letters at different positions can equal the same value.

### Stats
Linked Title:
Time taken: 0.04823469975963235
Number of collisions:  10805 : 72.03%
Number of wasted slots:  28554 : 87.19%

Linked Quote:
Time taken: 0.06304930010810494
Number of collisions:  11623 : 77.49%
Number of wasted slots:  29372 : 89.69%

Probed Title:
Time taken: 11.707318299915642
Number of collisions:  83403372 : 556022.48%
Number of wasted slots:  17749 : 54.20%

Probed Quote:
Time taken: 12.242003599647433
Number of collisions:  88120532 : 587470.21%
Number of wasted slots:  17749 : 54.20%

## 2nd Revision
```
def good_pelosi_hash(s):
    result = 0

    for i in range(len(s)):
        ascii = ord(s[i])
        result += ascii * i

    result = result * (10 ** len(s)) + len(s)
    return result % 32749
```

I tried this approach because I wanted to put the length of the string at the end. It kinda worked.

### Stats
Linked Title:
Time taken: 0.05773149989545345
Number of collisions:  6184 : 41.23%
Number of wasted slots:  23933 : 73.08%

Linked Quote:
Time taken: 0.12891170009970665
Number of collisions:  3770 : 25.13%
Number of wasted slots:  21519 : 65.71%

Probed Title:
Time taken: 0.05004099989309907
Number of collisions:  18112 : 120.75%
Number of wasted slots:  17749 : 54.20%

Probed Quote:
Time taken: 0.06985990004613996
Number of collisions:  8681 : 57.87%
Number of wasted slots:  17749 : 54.20%

## 3rd Revision
```
def good_pelosi_hash(s):
    result = 0

    for i in range(len(s)):
        ascii = ord(s[i])
        result += result * 31 + ascii

    return result % 32749
```

For this approach, I tried multiplying the result by a prime number, then adding the ascii. This worked okay, but I think it really suffered from the modulus.

### Stats
Linked Title:
Time taken: 0.07332270033657551
Number of collisions:  5466 : 36.44%
Number of wasted slots:  23215 : 70.89%

Linked Quote:
Time taken: 1.0004247999750078
Number of collisions:  3056 : 20.37%
Number of wasted slots:  20805 : 63.53%

Probed Title:
Time taken: 0.0740465996786952
Number of collisions:  14860 : 99.07%
Number of wasted slots:  17749 : 54.20%

Probed Quote:
Time taken: 0.9007242997176945
Number of collisions:  6404 : 42.69%
Number of wasted slots:  17749 : 54.20%

## 4th Revision
```
def good_pelosi_hash(s):
    result = 0

    for i in range(len(s)):
        ascii = ord(s[i])
        result += result * (7**i) + ascii

    return result % 32749
```

I tried this method so the index of the character effects the result a lot, and then adds the ascii, whichthe difference would be multiplied every new loop. I think this is also knee capped by the modulus. This also breaks when the string is too long.

### Stats
Linked Title:
Time taken: 0.15473149996250868
Number of collisions:  5441 : 36.27%
Number of wasted slots:  23190 : 70.81%

Linked Quote:
Broken by Seinfeld's attraction to a human woman.

Probed Title:
Time taken: 0.15816769981756806
Number of collisions:  14852 : 99.01%
Number of wasted slots:  17749 : 54.20%

Probed Quote:
To bee fair, she was better with him than Kronk

## 5th Revision
```
def good_pelosi_hash(s):
    result = 0

    for i in range(len(s)):
        ascii = ord(s[i])
        result += result * (i**7) + ascii

    return result % 32749
```

I decided that putting the index to the power of a constant would fix the issue I found last time with an incalculable number appearing from a particular insect movie. It seems to work somewhat well. I think most of the collisions come from modulus again.

### Stats
Linked Title:
Time taken: 0.10303420014679432
Number of collisions:  5375 : 35.83%
Number of wasted slots:  23124 : 70.61%

Linked Quote:
Time taken: 33.1952088996768
Number of collisions:  2980 : 19.87%
Number of wasted slots:  20729 : 63.30%

Probed Title:
Time taken: 0.10121809970587492
Number of collisions:  14392 : 95.95%
Number of wasted slots:  17749 : 54.20%

Probed Quote:
Time taken: 32.72975629987195
Number of collisions:  6451 : 43.01%
Number of wasted slots:  17749 : 54.20%