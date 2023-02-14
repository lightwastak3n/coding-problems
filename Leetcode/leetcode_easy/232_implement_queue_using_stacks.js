class MyQueue {
    constructor() {
        this.stack1 = [];
        this.stack2 = [];
    }

    push(x) {
        this.stack1.push(x);
    }

    peek() {
        if (!this.stack2.length) {
            while (this.stack1.length != 0) {
                this.stack2.push(this.stack1.pop());
            }
        }
        return this.stack2[this.stack2.length - 1];
    }

    pop() {
        this.peek();
        return this.stack2.pop();
    }

    empty() {
        return this.stack1.length == 0 && this.stack2.length == 0;
    }
}

// Time complexity: O(1) amortized - each of n elements moved only once in peek()
// Space complexity: O(n)
