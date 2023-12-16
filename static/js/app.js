const table = document.querySelector("table");
// const rows = table.tBodies[0].rows;
const rows = table.querySelectorAll("tbody tr");
const rowCount = rows.length;
const pageSize = 3;
let currentPage = 1;

function showPage(page) {
  for (let i = 0; i < rowCount; i++) {
    if (i >= (page - 1) * pageSize && i < page * pageSize) {
      rows[i].style.display = "table-row";
    } else {
      rows[i].style.display = "none";
    }
  }
}

showPage(currentPage);
updatePageInfo();

document.querySelector(".prev-btn").addEventListener("click", () => {
  if (currentPage > 1) {
    currentPage--;
    showPage(currentPage);
    updatePageInfo();
  }
});

document.querySelector(".next-btn").addEventListener("click", () => {
  if (currentPage < Math.ceil(rowCount / pageSize)) {
    currentPage++;
    showPage(currentPage);
    updatePageInfo();
  }
});

function updatePageInfo() {
  const pageInfo = document.querySelector(".page-info");
  pageInfo.textContent = `Page ${currentPage} of ${Math.ceil(
    rowCount / pageSize
  )}`;
}

// add numbering on the table
rows.forEach((row, index) => {
  const numberCell = document.createElement("td");
  numberCell.textContent = index + 1;
  row.insertBefore(numberCell, row.firstChild);
});
const deleteButton = document.querySelectorAll(".delete-btn");
const modal = document.querySelector(".modal");
const closeBtn = document.querySelector(".modal .close");
const confirmBtn = document.querySelector(".modal .confirm-btn");

deleteButton.forEach(function (delBtn) {
  delBtn.addEventListener("click", function () {
    modal.style.display = "block";
  });
});

closeBtn.addEventListener("click", function () {
  modal.style.display = "none";
});

document
  .querySelector(".modal .cancel-btn")
  .addEventListener("click", function () {
    modal.style.display = "none";
  });

confirmBtn.addEventListener("click", function () {
  // Perform delete operation
  modal.style.display = "none";
});
