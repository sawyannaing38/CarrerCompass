import {getCookie, showTypingEffect} from "./common.js";

const rejectBtnPrimary = document.querySelector(".rejectBtn-primary");
const confirmContainerPrimary = document.querySelector(".confirm-container-primary");
const yesBtnPrimary = document.querySelector(".yesBtn-primary");
const noBtnPrimary = document.querySelector(".noBtn-primary");
const candidates = document.querySelectorAll(".candidate");
const rejectBtns = document.querySelectorAll(".rejectBtn");
const rejectYesBtns = document.querySelectorAll(".reject-yes");
const rejectNoBtns = document.querySelectorAll(".reject-no");
let remainCandidates = candidates;

let currentIndex = 0;

// Removing button list from first candidate
candidates[currentIndex].querySelector(".button-list").style.display = "none";
candidates[currentIndex].classList.add("active");

// Showing confirm Box when click contactBtnPrimary
rejectBtnPrimary.addEventListener("click", function() 
{
    confirmContainerPrimary.style.display = "flex";
})

// When yes btn is clicked, reject the employee removes its ui, make another employee data is showed
yesBtnPrimary.addEventListener("click", async function() 
{   
    // Getting Candidate id
    const id = this.dataset.id;

    console.log(id);
    // End point for rejecting employee
    const url = `http://127.0.0.1:8000/api/rejectCandidate/${id}`;

    // Staring loading animation
    confirmContainerPrimary.classList.add("show-loading");

    // Try to reject that candidates
    try 
    {
        let response = await fetch(url, {
            "method" : "PATCH",
            "headers" : 
            {
                "Content-Type" : "application/json",
                "X-CSRFToken" : getCookie("csrftoken")
            }
            ,
            "body" : JSON.stringify({"reject" : true})
        })

        if (response.ok)
        {   
            // Stopping loading animation
            confirmContainerPrimary.classList.remove("show-loading");

            // Close the confirmBox
            confirmContainerPrimary.style.display = "none";

            // Removing the related navigation
            candidates[currentIndex].remove();

            remainCandidates = document.querySelectorAll(".candidate");

            if (remainCandidates.length === 0)
            {
                document.querySelector(".job-description").remove();
                document.querySelector(".container").remove();

                document.querySelector(".no-candidate").textContent = "No Candidates Remain";
                return;
            }

            // Increasing current Index
            currentIndex = getIndex();

            console.log(currentIndex);

            // Get data for another users
            showNextUser(currentIndex);
        }

        // If something unexpected Happen
        else
        {
            // Stopping loading animation
            confirmContainerPrimary.classList.remove("show-loading");
            confirmContainerPrimary.style.display = "none";

            return response;
        }
    }

    // Catching error
    catch(error)
    {
        // Stopping loading animation
        confirmContainerPrimary.classList.remove("show-loading");
        confirmContainerPrimary.style.display = "none";

        console.log(error);
    }
    
})

noBtnPrimary.addEventListener("click", function() {
    confirmContainerPrimary.style.display = "none";
})

// Changing info page whenever the user click the navigation
for (let i = 0; i < candidates.length; i++)
{
    candidates[i].addEventListener("click", function() 
    {
        currentIndex = i;
        showNextUser(i);
    })
}

// Showing confirm reject box when clicking rejectBtn
rejectBtns.forEach(function(rejectBtn) 
{
    rejectBtn.addEventListener("click", function(event) 
    {   
        event.stopPropagation();
        
        rejectBtn.parentElement.nextElementSibling.style.display = "flex";
    })
})

// Rejecting related candidate when rejectYes btn is clicked
rejectYesBtns.forEach(function(rejectYesBtn) 
{
    rejectYesBtn.addEventListener("click", async function(event)
    {
        event.stopPropagation();

        // Disable click candidate
        this.parentElement.parentElement.parentElement.classList.add("disabled");
        // Getting id 
        const id = Number(this.dataset.id);

        const url = `http://127.0.0.1:8000/api/rejectCandidate/${id}`;

        // Try to reject
        try 
        {   
            // Showing loading animation
            this.parentElement.parentElement.style.display = "none";
            this.parentElement.parentElement.nextElementSibling.style.display = "flex";
            const response = await fetch(url, {
                "method" : "PATCH",
                "headers" : 
                {
                    "Content-Type" : "application/json",
                    "X-CSRFToken" : getCookie("csrftoken")
                },
                "body" : JSON.stringify({"reject" : true})
            })

            // if everyting goes right
            if (response.ok)
            {
                // Remove the candidate from dom
                this.parentElement.parentElement.parentElement.remove();
            }

            // if not 
            else 
            {
                // Stop loading animation 
                this.parentElement.parentElement.nextElementSibling.style.display = "none";
            }
        }

        catch(error)
        {

        }
    })
})

rejectNoBtns.forEach(function(rejectNoBtn)
{
    rejectNoBtn.addEventListener("click", function(event)
    {
        event.stopPropagation();

        this.parentElement.parentElement.style.display = "none";
    })
})

// For showing another user data on the page
async function showNextUser(index)
{
    // Getting candidates id
    const id = candidates[index].dataset.id;

    const url = `http://127.0.0.1:8000/api/getEmployee/${id}`;

    // Try to get the information
    try
    {
        const response = await fetch(url);

        if (response.ok)
        {
            const result = await response.json();

            console.log(result);

            const candidateProfile = document.querySelector(".candidate-profile");

            // Change image 
            candidateProfile.querySelector("img").src = result.image;

            // Change name 
            showTypingEffect(candidateProfile.querySelector(".candidate-username"), result.user.username);

            // Change gender icon
            candidateProfile.querySelector("span").textContent = result.gender;

            // Change age
            showTypingEffect(candidateProfile.querySelector(".candidate-age"), `${result.age} years old`);

            // Change description
            showTypingEffect(candidateProfile.querySelector(".candidate-description"), result.description);

            // Change location
            showTypingEffect(document.querySelector(".candidate-location"), result.location);

            // Change education
            showTypingEffect(document.querySelector(".candidate-education"), result.education);

            // Change experience
            showTypingEffect(document.querySelector(".candidate-experience"), result.experience);

            // Change profession
            showTypingEffect(document.querySelector(".candidate-profession"), result.profession);

            // Change email
            showTypingEffect(document.querySelector(".candidate-email"), result.user.email);

            console.log("Candidate Id");
            console.log(id);
            // Change id of primaryConfirmBox
            confirmContainerPrimary.querySelector(".yesBtn-primary").dataset.id = candidates[index].dataset.candidate;

            // Removing active class from other navigation
            candidates.forEach(function(candidate) 
            {
                candidate.classList.remove("active");
                candidate.querySelector(".button-list").style.display = "block";
            })

            candidates[index].classList.add("active");
            candidates[index].querySelector(".button-list").style.display = "none";
        }
    }

    // Catching error
    catch(error)
    {
        console.log(error);
    }
}

// Function for getting index
function getIndex()
{
    // Converting node list into array
    const candidatesArr = Array.from(candidates);
    const remainCandidatesArr = Array.from(remainCandidates);

    // increasing current index until it reaches existing element
    if (currentIndex >= candidatesArr.length - 1)
    {
        console.log("Large");
        while(true)
        {
            currentIndex -= 1;

            if (candidatesArr.includes(candidates[currentIndex]) && remainCandidatesArr.includes(candidates[currentIndex]))
            {
                return currentIndex;
            }
        }
    }

    else 
    {
        
        while(true)
        {
            currentIndex += 1;

            if (candidatesArr.includes(candidates[currentIndex]) && remainCandidatesArr.includes(candidates[currentIndex]))
            {
                console.log("Include");
                return currentIndex;
            }
        }
        
    }
}