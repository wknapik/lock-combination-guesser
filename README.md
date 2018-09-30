# What ?
This script is meant to guess a lock combination based on observed
combinations, as "randomized" by users after closing the lock.

It reads combinations from stdin (one per line) and writes guesses to stdout.
```
guess.py <codes.txt >guesses.txt
```

# Assumptions ?
* Digits 0-9 on rotating dials (distance between 0 and 9 is 1)
* The observable combinations are not truly random

# Why ?
The key to the gate at my office is protected by a combination lock. Every day
I'd see combinations set by different people and realized they were not very
well randomized, so I figured I'd see if a simple script could guess the
combination that opens the lock.

# How ?
This script implements what is probably the most naive approach to the problem
\- for every position in the combination, it checks what digits have the
smallest distance to all the digits observed at that position - those become
candidates for that position.

Could this be done better ? Sure. The implementation is not the most efficient
and the approach to the problem is clearly not optimal, since we're not even
looking at entire combinations, just the digits at each position individually.

This would be a great problem for AI, but I didn't have the training data and I
never will, so...

# Results ?
The results are surprisingly good, though a sample of 1 is hardly a basis for
any far reaching conclusions ;] With the constants as currently set in the
script, when fed the combinations I observed for a 4-digit lock, it usually
produces the correct combination within at most 220 guesses, depending on the
subset of inputs used, with a correct guess most often within the first 100.

The guesses are printed in an order that usually requires only one digit to be
changed to try the next one, so assuming 2 seconds to test a combination, it
would take 3min20s to try 100 guesses and 7min20s to try 220.

# Tweaks ?
There are two constants that can be used to tweak the results, their meaning is
explained in the script sources.

A higher value of MAX_SCORE may increase the number of guesses per position, up
to MAX_CAND.

Considering straight up brute force requires at most 10 \*\* NUM_OF_DIGITS
attempts, the default MAX_CAND value of 5 reduces the number of combinations to
try by 2 orders of magnitude for a 4-digit combination. That would be the
difference between trying for 20min and trying for 5h30min.
