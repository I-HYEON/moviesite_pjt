// const cardText = document.querySelector('.card-text');
// const cardTextFull = cardText.querySelector('.card-text-full');
// const overviewToggle = document.querySelector('.overview-toggle');

// overviewToggle.addEventListener('click',function() {
//     cardText.classList.toggle('card-text-collapsed');
//     if (cardText.classList.contains('card-text-collapsed')) {
//         overviewToggle.textContent = '더보기';
//     } else {
//         overviewToggle.textContent = '접기';
//     }
// });

const cardTexts = document.querySelectorAll('.card-text');
const overviewToggles = document.querySelectorAll('.overview-toggle');

overviewToggles.forEach((toggle, index) => {
  const cardText = cardTexts[index];
  const cardTextFull = cardText.querySelector('.card-text-full');

  toggle.addEventListener('click', () => {
    cardText.classList.toggle('card-text-collapsed');
    if (cardText.classList.contains('card-text-collapsed')) {
      toggle.textContent = '더보기';
    } else {
      toggle.textContent = '접기';
    }
  });
});
