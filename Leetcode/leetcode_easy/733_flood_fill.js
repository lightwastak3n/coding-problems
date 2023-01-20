var floodFill = function(image, sr, sc, color) {
    let tColor = image[sr][sc];
    let stack = image[sr][sc] != color ? [[sr, sc]] : [];
    while (stack.length > 0) {
        let [i, j] = stack.pop();
        image[i][j] = color;
        if (i -1 >= 0 && image[i-1][j] == tColor) {
            stack.push([i-1, j]);
        }
        if (i + 1 <= image.length - 1 && image[i+1][j] == tColor) {
            stack.push([i+1, j]);
        }
        if (j - 1 >= 0 && image[i][j-1] == tColor) {
            stack.push([i, j-1]);
        }
        if (j+1 <= image[0].length-1 && image[i][j+1]) {
            stack.push([i, j+1]);
        }
    }
    return image;
};
// I'm not sure about the complexities in this one.
// k - number of elements connected to the start that are the same color
// Time complexity: O(k) - We are checking up to 4k elements but changing k. 
// Space complexity: O(k) - I guess stack holds at least 1 element if its only 1 of same color or a line of same color.
// And at worst if the entire image is the same color we are on avg adding 2-3 new elements and removing one so it's ~k.
