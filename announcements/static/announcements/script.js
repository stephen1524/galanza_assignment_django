function toggleText() {
  const moreText = document.getElementById("more-text");
  const btn = document.querySelector("button");

  if (moreText.style.display === "none") {
    moreText.style.display = "inline";
    btn.textContent = "Show less";
  } else {
    moreText.style.display = "none";
    btn.textContent = "Read more";
  }
}