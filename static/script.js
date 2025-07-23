// Show alert after submitting booking form
function confirmBooking(event) {
  const seats = document.getElementById("seats").value;
  if (seats < 1) {
    alert("Please enter a valid number of seats!");
    event.preventDefault(); // prevent form submission
    return false;
  }
  alert(`You have booked ${seats} seat(s). Thank you!`);
}

// Optional: Highlight cards on hover
document.addEventListener("DOMContentLoaded", () => {
  const cards = document.querySelectorAll(".card");
  cards.forEach(card => {
    card.addEventListener("mouseenter", () => {
      card.style.boxShadow = "0 8px 16px rgba(0,0,0,0.3)";
    });
    card.addEventListener("mouseleave", () => {
      card.style.boxShadow = "0 4px 8px rgba(0,0,0,0.1)";
    });
  });
});
