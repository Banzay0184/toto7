document.addEventListener("DOMContentLoaded", () => {
  const tabButtons = document.querySelectorAll(".content__tab-btn");
  const tabPages = [
    "future-circulation",
    "current-circulation",
    "completed-edition",
    "tickets",
    "users",
  ];

  tabButtons.forEach((tabButton) => {
    tabButton.addEventListener("click", (event) => {
      const currentTab = document.getElementById(event.target.dataset.tab);

      tabPages.forEach((tabPage) => {
        if (tabPage === event.target.dataset.tab) {
          currentTab.hidden = false;
        }
        document.getElementById(tabPage).hidden = true;
      });
    });
  });
});
