(() => {
  const root = document.documentElement;
  const button = document.querySelector("[data-language-toggle]");
  const saved = localStorage.getItem("royal-frame-language");
  const initial = saved === "en" ? "en" : "he";

  function applyLanguage(language) {
    const english = language === "en";
    root.dataset.language = english ? "en" : "he";
    root.lang = english ? "en" : "he";
    root.dir = english ? "ltr" : "rtl";
    if (button) {
      button.textContent = english ? "עברית" : "English";
      button.setAttribute("aria-label", english ? "החלפה לעברית" : "Switch to English");
    }
    localStorage.setItem("royal-frame-language", english ? "en" : "he");
  }

  if (button) {
    applyLanguage(initial);
    button.addEventListener("click", () => {
      applyLanguage(root.dataset.language === "en" ? "he" : "en");
    });
  }

  document.querySelectorAll("[data-year]").forEach((node) => {
    node.textContent = new Date().getFullYear();
  });
})();
