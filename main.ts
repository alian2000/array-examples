let list: string[] = []
let count = 0
input.onButtonPressed(Button.A, function () {
    list = [
    "usama",
    "Muhammad",
    "Walid",
    "Nabil",
    "Nour"
    ]
    basic.showString("" + (list[randint(0, 4)]))
    count = list.length
    basic.showString("" + (count))
    basic.pause(100)
    basic.clearScreen()
})
input.onButtonPressed(Button.AB, function () {
    for (let index = 0; index <= 10; index++) {
        if (index % 2 == 0) {
            basic.showNumber(index)
            basic.showString("Even Numbers")
            basic.pause(50)
        }
    }
})
input.onButtonPressed(Button.B, function () {
    list = [
    "usama",
    "Muhammad",
    "Walid",
    "Nabil",
    "Nour"
    ]
    for (let value of list) {
        basic.showString("" + (value))
        basic.clearScreen()
    }
})
