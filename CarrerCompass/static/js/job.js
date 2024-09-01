import {getCookie} from "./common.js"

const descirption = document.querySelector(".description");
const benefit = document.querySelector(".benefit");
const requirement = document.querySelector(".requirement");
const applyBtn = document.querySelector(".applyBtn");
const body = document.querySelector("body");
const applyConfirmBox = document.querySelector(".apply-confirm");
const confirmBtn = document.querySelector(".confirm");
const rejectBtn = document.querySelector(".reject");

transformHeight(descirption, 100);
transformHeight(benefit, 200);
transformHeight(requirement, 300);

function transformHeight(obj, time)
{
    setTimeout(function() {
        obj.style.maxHeight = "500px";
    }, time)
}

applyBtn.addEventListener("click", function()
{
    // Show applyConfirmBox
    applyConfirmBox.style.display = "block";
})

confirmBtn.addEventListener("click", async function()
{   
    const id = Number(applyBtn.dataset.id);

    // fetch the createCandidate api
    const url = `http://127.0.0.1:8000/api/createCandidate/${id}`;

    try
    {
        const response = await fetch(url , {
            "method" : "POST",
            "headers" : 
            {
                "Content-Type" : "application/json",
                "X-CSRFToken" : getCookie("csrftoken")
            }
        })

        if (!response.ok)
        {
            console.log(response)
        }
    }

    catch(error)
    {
        console.log(error)
    }   

    // Changing textContent
    applyBtn.textContent = "Applied";
    applyBtn.disabled = true;
    applyConfirmBox.style.display = "none";
})

rejectBtn.addEventListener("click", function()
{
    applyConfirmBox.style.display = "none";
})