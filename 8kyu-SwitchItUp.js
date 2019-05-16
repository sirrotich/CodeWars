// When provided with a number between 0-9, return it in words.

// Input :: 1

// Output :: "One".

// Try using "Switch" statements.


function SwitchItUp(number){
    obj = {
        1:'One',
        2:'Two',
        3:'Three',
        4:'Four',
        5:'Five',
        6:'Six',
        7:'Seven',
        8:'Eight',
        9:'Nine'
    }

    return obj[number]
}