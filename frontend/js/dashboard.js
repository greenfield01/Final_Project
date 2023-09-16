const userDropdownToggle = document.querySelector("#user-dropdown-toggle");
const userDropdownContent = document.querySelector("#user-dropdown-content");
const openDataModalButton = document.querySelector("#open-data-modal");

const addDataModal = document.querySelector("#add-data-modal");
const closeAddDataModal = document.querySelector("#close-button");
const listItems = document.querySelectorAll("li");
const readMoreBtn = document.querySelector("#read-more");

function toglModal() {
  addDataModal.classList.toggle("show-modal");
}

function showProfile() {
  userDropdownContent.style.display =
    userDropdownContent.style.display === "block" ? "none" : "block";
}

function showItemContent(content) {
  if (content.style.display === "block") {
    content.style.display = "none";
  } else {
    content.style.display = "block";
  }
}

function readMore(event, elementId) {
  event.stopPropagation();
  const itemArticle = document.getElementById(elementId);
  if (itemArticle.className == "open") {
    // Read less
    itemArticle.className = "";
    readMoreBtn.innerHTML = "Read more";
  } else {
    itemArticle.className = "open";
    readMoreBtn.innerHTML = "Read less";
  }
}

userDropdownToggle.addEventListener("click", showProfile);

openDataModalButton.addEventListener("click", toglModal);

closeAddDataModal.addEventListener("click", toglModal);

listItems.forEach((item) => {
  const content = item.querySelector(".content");
  item.addEventListener("click", () => showItemContent(content));
});

readMoreBtn.addEventListener("click", readMore);
