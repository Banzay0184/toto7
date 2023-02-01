document.addEventListener("DOMContentLoaded", () => {
  const profileForm = document.getElementById("profile-form");
  const editButtons = profileForm.querySelectorAll(".profile__edit-btn");

  editButtons.forEach((editButton) => {
    editButton.addEventListener("click", (event) => {
      if (event.target.textContent === "Сохранить") {
        event.target.previousElementSibling.disabled = true;
        event.target.textContent = "изменить";
        event.target.type = "submit";
      } else {
        event.target.previousElementSibling.disabled = false;
        event.target.previousElementSibling.focus();
        event.target.textContent = "Сохранить";
        event.target.type = "button";
      }
    });
  });

  const allEditButton = document.querySelector(".profile__edit");

  allEditButton.addEventListener("click", (event) => {
    if (event.target.textContent === "Сохранить") {
      profileForm.querySelectorAll("input.profile__data").forEach((profileData) => {
        profileData.disabled = true;
      });

      event.target.textContent = "Редактировать";
      event.target.type = "submit";
    } else {
      profileForm.querySelectorAll("input.profile__data").forEach((profileData) => {
        profileData.disabled = false;
      });

      event.target.textContent = "Сохранить";
      event.target.type = "button";
    }
  });
});
