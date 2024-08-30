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

confirmBtn.addEventListener("click", function()
{
    applyConfirmBox.style.display = "none";
    applyBtn.textContent = "Applied";
    applyBtn.disabled = true;
})

rejectBtn.addEventListener("click", function()
{
    applyConfirmBox.style.display = "none";
})