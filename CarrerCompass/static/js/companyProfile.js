import {getCookie} from "./common.js"

// Selecting DOM
const scrollContainer = document.querySelector(".review-list");
const leftArrow = document.querySelector(".left-arrow");
const rightArrow = document.querySelector(".right-arrow");
const rateBtn = document.querySelector(".rateBtn");
const ratingBox = document.querySelector(".user-rating");
const discardBtn = document.querySelector(".discardBtn");
const ratingStars = document.querySelector(".stars");
const stars = ratingStars.querySelectorAll(".star");
const addBtn = document.querySelector(".addBtn");

leftArrow.addEventListener("click", function()
{
    scrollContainer.scrollLeft -= 390;
})

rightArrow.addEventListener("click", function()
{
    if (scrollContainer.scrollLeft >= 720)
    {
        scrollContainer.scrollLeft = 0;
        return;
    }
    scrollContainer.scrollLeft += 390;
})

rateBtn.addEventListener("click", function()
{
    ratingBox.style.display = "flex";
})

discardBtn.addEventListener("click", function()
{
    ratingBox.style.display = "none";
})

stars.forEach(function(star)
{
    star.addEventListener("click", function()
    {
        star.classList.toggle("fill");
    })
})

addBtn.addEventListener("click", async function()
{
    // Getting corresponding id
    const id = this.dataset.id;

    // Url
    const url = `http://127.0.0.1:8000/api/createCompanyReview/${id}`;

    // Getting ating count
    const ratingCount = ratingStars.querySelectorAll(".fill").length;
    const description = document.querySelector("#description");

    if (!description.value)
    {
        description.ariaPlaceholder = "Description is Required";
        return;
    }

    // Try to fetch
    try
    {
        const response = await fetch(url, {
            "method" : "POST",
            "headers" : 
            {
                "Content-Type" : "application/json",
                "X-CSRFToken" : getCookie("csrftoken")
            },
            "body" : JSON.stringify({"rating" : ratingCount, "description" : description.value})
        })

        if (response.ok)
        {
            console.log("OK");
        }

        else
        {
            console.log(response);
        }
    }

    // Catching error
    catch(error)
    {
        console.log(error)
    }

    // Remove the rating box
    ratingBox.style.display = "none";
})