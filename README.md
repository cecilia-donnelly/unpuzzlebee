# unpuzzlebee

This is a little work in progress that will be able to make and solve
puzzles of the "beehive" format, like those that appear in the NYT
magazine every Sunday.  [Someone else has done a similar
project](http://aaronsdevera.com/2015/12/09/dailybeehive-automating-word-game-creation/),
but I'm looking into it for fun/practice anyway.

Beehive puzzles are word games that take 7 letters, like so:

V | A | C
  | L |
R | I | H

The challenge is to find words with 5 or more letters that can be
constructed from these seven letters.  Note that the middle letter (in
the example above, "L") MUST be used in each word.  Letters may be
repeated.

Each word is worth 1 point, except that words using all seven letters
are worth 3 points.

_Example solution words from this puzzle:_ chivalric, viral, civil


The goals of this project are to:

1. Solve a puzzle given the central letter and 6 surrounding letters.

2. Give hints for a puzzle of the form "common chunks are" (in the
example above, a common chunk might be "ch").

3. Create a new puzzle, with letters such that the solution set is worth
25+ points (my extremely casual and unscientific observation of the NYT
mag puzzles suggests that they're usually worth around 28-30 points).

