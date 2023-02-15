document.addEventListener("DOMContentLoaded", () => {
  const editButtons = document.querySelectorAll(
    ".tbody-future-circulation tr td:nth-child(3)"
  );

  editButtons.forEach((editButton) => {
    editButton.addEventListener("click", (event) => {
      let target = event.target;
      let firstInput = target.parentElement.previousElementSibling.firstElementChild;
      let secondInput =
        target.parentElement.previousElementSibling.previousElementSibling
          .firstElementChild;

      if (event.target.textContent === "Сохранить") {
        firstInput.disabled = true;
        secondInput.disabled = true;
        event.target.textContent = "редактировать";
        event.target.type = "submit";
      } else {
        firstInput.disabled = false;
        secondInput.disabled = false;
        firstInput.focus();
        event.target.textContent = "Сохранить";
        event.target.type = "button";
      }
    });
  });

  const commpletedEditionEditButtons = document.querySelectorAll(
    "#form-completed-edition tbody tr td:nth-child(4)"
  );

  const futureCirculationDate = document.getElementById("future-circulation-date");
  const futureCirculationTime = document.getElementById("future-circulation-time");
  const futureCirculationButton = document.getElementById("future-circulation-button");

  futureCirculationButton.addEventListener("click", () => {
    if (futureCirculationButton.textContent == "Сохранить") {
      futureCirculationDate.disabled = true;
      futureCirculationTime.disabled = true;
      futureCirculationButton.textContent = "редактировать";
      futureCirculationButton.type = "submit";
      return;
    }
    futureCirculationDate.disabled = false;
    futureCirculationTime.disabled = false;
    futureCirculationTime.focus();

    futureCirculationButton.textContent = "Сохранить";
    futureCirculationButton.type = "button";
  });

  commpletedEditionEditButtons.forEach((editButton) => {
    editButton.addEventListener("click", (event) => {
      let firstInput =
        event.target.parentElement.previousElementSibling.previousElementSibling
          .firstElementChild;
      let secondInput =
        event.target.parentElement.previousElementSibling.previousElementSibling
          .previousElementSibling.firstElementChild;
      let thirdInput =
        event.target.parentElement.previousElementSibling.firstElementChild;

      if (event.target.textContent === "Сохранить") {
        firstInput.disabled = true;
        secondInput.disabled = true;
        thirdInput.disabled = true;
        event.target.textContent = "редактировать";
        event.target.type = "submit";
      } else {
        firstInput.disabled = false;
        secondInput.disabled = false;
        thirdInput.disabled = false;
        firstInput.focus();
        event.target.textContent = "Сохранить";
        event.target.type = "button";
      }
    });
  });

  const ticketsEditButtons = document.querySelectorAll(
    ".form-tickets tbody tr td:nth-child(4) button"
  );

  ticketsEditButtons.forEach((editButton) => {
    editButton.addEventListener("click", () => {
      let firstInput =
        editButton.parentElement.previousElementSibling.previousElementSibling
          .firstElementChild;
      let secondInput =
        editButton.parentElement.previousElementSibling.previousElementSibling
          .previousElementSibling.firstElementChild;
      let thirdInput = editButton.parentElement.previousElementSibling.firstElementChild;

      if (editButton.type == "button") {
        firstInput.disabled = true;
        secondInput.disabled = true;
        thirdInput.disabled = true;
        editButton.setAttribute("type", "submit");
        return;
      }
      firstInput.disabled = false;
      secondInput.disabled = false;
      thirdInput.disabled = false;
      firstInput.focus();
      editButton.setAttribute("type", "button");
    });
  });
});
