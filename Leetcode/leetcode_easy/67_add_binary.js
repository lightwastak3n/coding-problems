var addBinary = function(a, b) {
    a = a.length < b.length ? "0".repeat(b.length-a.length) + a : a;
    b = b.length < a.length ? "0".repeat(a.length-b.length) + b : b;
    let c = "", carry = "0";
    for (let i = a.length - 1; i >= 0; i--) {
        if (a[i] == b[i]) {
            c = carry + c;
            carry = a[i] == 1 ? "1" : "0";
        }
        else {
            c = carry == "1" ? "0" + c : "1" + c;
            carry = carry == "1" ? "1" : "0";
        }
    }
    if (carry == "1") {
        c = "1" + c;
    }
    return c;
};

// There is a cheeky solution with prepending 0b and using BigInt - (BigInt(`0b${a}`) + BigInt(`0b${b}`) ...
// But it's probably expected of us to do some string manipulation

// Time complexity: O(n)
// Lets say numbers have lengths (digits) n and m where n is the larger number.
// At lines 2 and 3 we are prepending n - m digits
// I don't know the complexity of String.prototype.repeat() but let's say in the worst case, m = 0, it is O(n)
// We are also doing for loop of length n so in total O(n+n) = O(n)

// Space complexity: O(n)
// Storing carry and c which has n or n+1 digits
