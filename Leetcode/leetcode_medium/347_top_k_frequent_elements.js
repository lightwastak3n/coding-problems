var topKFrequent = function(nums, k) {
    const freq = {};
    for (const num of nums) {
        freq[num] = (freq[num] || 0) + 1;
    }
    return Object.entries(freq).sort((a ,b) => b[1] - a[1]).slice(0, k).map(x => parseInt(x[0]));
};
