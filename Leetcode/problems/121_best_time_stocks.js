var maxProfit = function(prices) {
    let buy = Infinity;
    let sell = -Infinity;
    let profit = 0;
    for (let i = 0; i < prices.length; i++) {
        if (prices[i] < buy) {
            buy = prices[i];
            sell = -Infinity;
        }
        else if (prices[i] > sell){
            sell = prices[i];
        }
        profit = Math.max(profit, sell - buy);
    }
    return profit;
};