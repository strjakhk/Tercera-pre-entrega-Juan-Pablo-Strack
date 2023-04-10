const title = document.getElementById("main-title")
const userNodes = document.querySelectorAll(".user-list td > span")

const colorBlinkAnimation = [
    { opacity : 1 },
    { opacity : 0.4 },
    { opacity : 1 }
]

const colorBlink = (nodes, animationName) =>{

    nodes.forEach((node) =>{
        node.animate(animationName, { duration : 2500 , iterations : Infinity})
    })
}

const textWritten = (text, node, timer) => {
    text += "               "
    let index = 0
    let direction = 1

    if(node){
        const textwrittenInterval = setInterval(() =>{

            if(index == text.length){
                direction = -1
            }else if(index == 0){
                direction = 1
            }
        
            if(direction == -1 && text[index - 1] == " "){
                node.textContent = text.slice(0, index + 1)
                index -= 2
            }else if(direction == 1 && text[index + 1] == " "){
                node.textContent = text.slice(0, index + 1)
                index += 2
            }else{
                node.textContent = text.slice(0, index + 1)
                index += direction
            }
        
        }, timer)
    }
}

textWritten("welcome to strjak blog", title, 80)
colorBlink(userNodes, colorBlinkAnimation)