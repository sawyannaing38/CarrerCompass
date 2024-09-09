import { getCookie, toggleShow} from "./common.js";

const heading = document.querySelector(".job-offer-heading")
const reviewHeading = document.querySelector(".review-heading");
const reviews = document.querySelectorAll(".review");
const jobs = document.querySelectorAll(".job");
const jobLists = document.querySelector(".job-lists");
const leftBtn = document.querySelector(".leftBtn");
const rightBtn = document.querySelector(".rightBtn");
const scrollContainer = document.querySelector(".review-list");
const rateBtn = document.querySelector(".rateBtn");
const rateContainer = document.querySelector(".rate-container");
const description = document.querySelector("#description");
const addBtn = document.querySelector(".addBtn");
const discardBtn = document.querySelector(".discardBtn");
const error = document.querySelector("#error");
const starConainer = document.querySelector(".stars");
const stars = starConainer.querySelectorAll("span");

if (jobs.length == 4)
{
    jobLists.style.justifyContent = "space-between";
}

document.addEventListener("scroll", function()
{
    jobs.forEach(function(job)
    {
        toggleShow(job);
    })

    reviews.forEach(function(review)
    {
        toggleShow(review);
    })

    toggleShow(leftBtn);
    toggleShow(rightBtn);
    toggleShow(heading);
    toggleShow(reviewHeading);
    toggleShow(rateBtn);
})

leftBtn.addEventListener("click", function()
{
    scrollContainer.scrollLeft -= 388;
})

rightBtn.addEventListener("click", function()
{   
    console.log(scrollContainer.scrollLeft);
    if (scrollContainer.scrollLeft >= 750)
    {
        scrollContainer.scrollLeft -= 780;
        return;
    }
    scrollContainer.scrollLeft += 390;
})

rateBtn.addEventListener("click", function()
{
    rateContainer.style.display = "flex";
})

addBtn.addEventListener("click", async function()
{
    // Get the input value
    const descriptionValue = description.value;
    const rating = starConainer.querySelectorAll(".fill").length;

    if (!descriptionValue)
    {
        error.textContent = "Description is required";
        return;
    }

    const url = `http://127.0.0.1:8000/api/createWebsiteReview/`;

    try 
    {
        const response = await fetch(url, {
            "method" : "POST",
            "headers" : 
            {
                "Content-Type" : "application/json",
                "X-CSRFToken" : getCookie("csrftoken")
            },
            "body" : JSON.stringify({"rating" : rating, "description" : descriptionValue})
        })
    }

    catch(error)
    {
        console.log(error);
    }

    // Remove ratebox
    rateContainer.style.display = "none";
})

stars.forEach(function(star)
{
    star.addEventListener("click", function()
    {
        star.classList.toggle("fill");
    })
})

discardBtn.addEventListener("click", function()
{
    rateContainer.style.display = "none";
})