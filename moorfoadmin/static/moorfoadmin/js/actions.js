// actions.js
document.addEventListener("DOMContentLoaded", function () {
    const selectAllCheckbox = document.getElementById("action-toggle");
    const checkboxes = document.querySelectorAll("input.action-select");
    const countElement = document.getElementById("selected-count");
    const totalCount = checkboxes.length;

    function updateSelectedCount() {
        const selectedCount = Array.from(checkboxes).filter(checkbox => checkbox.checked).length;
        countElement.textContent = `${selectedCount} of ${totalCount} selected`;
        if (selectedCount === totalCount) {
            selectAllCheckbox.checked = true;
        }   else if (selectedCount === 0) {
            selectAllCheckbox.checked = false;
        }
    }

    selectAllCheckbox.addEventListener("change", function () {
        checkboxes.forEach(function (checkbox) {
            checkbox.checked = selectAllCheckbox.checked;
        });
        updateSelectedCount();
    });

    checkboxes.forEach(function (checkbox) {
        checkbox.addEventListener("change", function () {
            updateSelectedCount();
        });
    });

    // Initial count update
    updateSelectedCount();
});
