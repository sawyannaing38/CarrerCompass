"use strict";

const infos = document.querySelectorAll(".info");
const descriptions = ["I am Company here to hire", "I am Employee here to apply"]

setTimeout(() => {
    let index = 0;
    infos.forEach(info => {
        info.style.transform = "translateX(0px)";
        info.style.borderColor = "white";
        showTypingEffect(info.firstElementChild, descriptions[index]);
        index += 1;
    })
}, 300)

function showTypingEffect(obj, texts)
{   
    obj.textContent = "";
    const words = texts.split(" ");
    console.log(words);
    let currentIndex = 0;

    const intervalId = setInterval(() => {
        obj.textContent += `${words[currentIndex]} `;
        currentIndex += 1;

        if (currentIndex >= words.length)
        {
            clearInterval(intervalId);
        }
    }, 100)
}