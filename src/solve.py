# Unpuzzlebee is a word puzzle maker and solver.
# Copyright (C) 2016 Cecilia Donnelly
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#
# Given 7 letters, return a list of all English words greater than 5
# letters long that can be constructed from those letters.  Calculate
# point value of solution set.
#
# Call this like: python solve.py [6 outer letters] [1 central letter]

import sys;

def check_args():
    if len(sys.argv) > 1:
        # TODO: also check that they've given the right number of letters
        outer_letters = list(sys.argv[1]);
    else:
        print("Call this like: python solve.py [6 outer letters] [1 central letter]");
        return False;

    if len(sys.argv) > 2:
        inner_letter = sys.argv[2];
    else:
        print("Please specify a central letter");
        return False;

    return True;



def find_solution_words(outer, inner):

    outer_letters = outer;
    inner_letter = inner;
    
    # for now, playing around:

    outer_letters = ['v', 'a', 'c', 'r', 'i', 'h'];
    inner_letter = 'l';

    print("6 outer letters are: ");
    print(outer_letters);
    print("The central letter is: " + inner_letter);
    print("Calculating...");
    
    # import dictionary of English words here
    
    dict = ['chivalry', 'chivalric', 'civil', 'civic', 'adder', 'liar'];
    
    all_puzzle_letters = outer_letters;
    all_puzzle_letters.append(inner_letter);
    print("All letters are");
    print(all_puzzle_letters);
    
    solution_words = [];
    
    
    for word in dict:
        matching = True;
        word_array = list(word);
        # check that word is long enough
        if len(word_array) < 5:
            break;
        
        # check for center letter
        if inner_letter not in word_array:
            break;
        
        # check for extraneous letters
        for letter in word_array:
            if letter not in all_puzzle_letters:
                matching = False;
                break;
        
        if matching:
            solution_words.append(word);

    print("The solution words are: ");
    print(solution_words);
    print(calculate_score(solution_words, all_puzzle_letters));
    return solution_words;


def calculate_score(solution_words, all_puzzle_letters):
    score = 0;
    normal = True;
    for word in solution_words:
        for letter in all_puzzle_letters:
            if letter not in word:
                normal = True;
                break;
            else:
                normal = False;
        if normal == True:
            score = score + 1;
        else:
            score = score + 3;

    return score;

    

def main():
    valid_args = check_args();
    if valid_args:
        find_solution_words(sys.argv[1], sys.argv[2]);


main();
