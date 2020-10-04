$(".menu-toggle").click(function () {
  $(".site-nav").toggleClass("site-nav--open", 500);
  $(this).toggleClass('open');
})

/*
const menuBtn = document.querySelector(".site-nav");
let menuOpen = false;
menuBtn.addEventListener("click", () => {
  if (!menuOpen) {
    menuBtn.classList.add("--open");
    menuOpen = true;
  } else {
    menuBtn.classList.remove("--open");
    menuOpen = false;
  }
});
*/
