var groupAnagrams = function(strs) {
    const sortWord = (word) => word.split("").sort().join();
    const output = [];
    const map = {};
    let i = 0;
    for (const word of strs) {
        let sortedWord = sortWord(word);
        if (sortedWord in map) {
            output[map[sortedWord]].push(word);
        } else {
            map[sortedWord] = i;
            output.push([word])
            i++;
        }
    }
    return output;
};

// Time complexity: O(n) - one loop through array
// Space complexity: O(n) - output is same size as original array, map is at most n length
