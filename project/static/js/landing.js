//  toggle_btn = document.querySelector(".toggle-btn");
//   big_wrapper = document.querySelector(".big-wrapper");
 var toggle_btn;
 var big_wrapper;
 var menu;
function declare() {
    toggle_btn = document.querySelector(".toggle-btn");
    big_wrapper = document.querySelector(".big-wrapper");
    menu = document.querySelector(".menu");
}
declare();
const main = document.querySelector("main");
let dark = false;
function toggleAnimation() {
    // alert("Hello");
    dark = !dark;
    let clone = big_wrapper.cloneNode(true);

    if (dark) {
        clone.classList.remove("dark");
        clone.classList.add("light");
    }
    else {
        clone.classList.remove("light");
        clone.classList.add("dark");
    }
    clone.classList.add("copy");
    main.appendChild(clone);
    document.body.classList.add("stop-scrolling");
    clone.addEventListener("animationend", () => {
        big_wrapper.remove();
        clone.classList.remove("copy");
    document.body.classList.remove("stop-scrolling");

        declare();
        events();

    });

}

function events() {
    toggle_btn.addEventListener("click", toggleAnimation);
    menu.addEventListener("click", ()=>{
        big_wrapper.classList.toggle("active");
    });

}
events();

