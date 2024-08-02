document.addEventListener("DOMContentLoaded", function () {
  const navToggle = document.getElementById("nav-toggle");
  const navMenu = document.getElementById("nav-menu");
  const navClose = document.getElementById("nav-close");
  const navMenuItems = document.querySelectorAll(".nav-menu_item");

  navToggle.addEventListener("click", function () {
    navMenu.classList.toggle("open");
    document.body.classList.toggle("overlay");
  });

  navClose.addEventListener("click", function () {
    navMenu.classList.remove("open");
    document.body.classList.remove("overlay");
  });

  document.addEventListener("click", function (event) {
    if (!navMenu.contains(event.target) && !navToggle.contains(event.target)) {
      navMenu.classList.remove("open");
      document.body.classList.remove("overlay");
    }
  });

  navMenuItems.forEach(item => {
    item.addEventListener("click", function () {
      navMenu.classList.remove("open");
      document.body.classList.remove("overlay");
    });
  });
});
