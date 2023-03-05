var canConstruct = function(ransomNote, magazine) {
    let noteFreq = {};
    let total = 0;
    for (let char of ransomNote) {
        if (noteFreq[char]) {
            noteFreq[char]++;
        }
        else {
            noteFreq[char] = 1;
        }
        total++;
    }
    for (let char of magazine) {
        if (noteFreq[char] && noteFreq[char] > 0) {
            noteFreq[char]--;
            total--;
        }
    }
    return total == 0;
};

//Time Complexity: O(n+m) - where n is the length of ransomNote and m is the length of magazine
//Space Complexity: O(k) - k number of distinct characters in ransomNote. Worst case is O(n) if all characters are distinct.