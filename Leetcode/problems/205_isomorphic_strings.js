// Time: O(n) - Getting values from object is O(n) and then checking for value in there is also O(n) so O(2n) = O(n)
// Space: O(1) - Creating object of at most size 26

var isIsomorphic = function(s, t) {
    let mapping = {}
    for (let i = 0; i < s.length; i++){
        if (s[i] in mapping && mapping[s[i]] != t[i]){
            return false
        }
        else if (!(s[i] in mapping)){
            if (Object.values(mapping).includes(t[i])){return false}
            mapping[s[i]] = t[i]
        }
    }
    return true
};

// We can make it a bit faster by using object for reverse mapping and checking if the value is already there
// instead of creating array with Object.values() and checking for value like we did above. 
// Since checking for a value in object takes constant time.
// Same complexity as above.

var isIsomorphic = function(s, t) {
    let mapping = {}
    let reverseMapping = {}
    for (let i = 0; i < s.length; i++){
        if (s[i] in mapping && mapping[s[i]] != t[i]){
            return false
        }
        else if (!(s[i] in mapping)){
            if (t[i] in reverseMapping){return false}
            mapping[s[i]] = t[i]
            reverseMapping[t[i]] = s[i]
        }
    }
    return true
};