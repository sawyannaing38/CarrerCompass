"use strict";
import { showTypingEffect } from "./comon.js";
const infos = document.querySelectorAll(".info");
const descriptions = ["I am Company here to hire", "I am Employee here to apply"]

document.addEventListener("DOMContentLoaded", function() 
{
    setTimeout(() => {
        let index = 0;
        infos.forEach(info => {
            info.style.transform = "translateX(0px)";
            info.style.borderColor = "white";
            showTypingEffect(info.firstElementChild, descriptions[index]);
            index += 1;
        })
    }, 300)
})
