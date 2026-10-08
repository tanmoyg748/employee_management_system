function deleteEmployee(employeeId) {

    const confirmed = confirm(
        "Are you sure you want to delete this employee?"
    );

    if (!confirmed) {
        return;
    }

    const csrfToken = document.querySelector(
        '[name=csrfmiddlewaretoken]'
    ).value;

    fetch(`/delete/${employeeId}/`, {
        method: "POST",

        headers: {
            "X-CSRFToken": csrfToken,
            "Content-Type": "application/json"
        }
    })

    .then(response => response.json())

    .then(data => {

        if (data.success) {

            const row = document.getElementById(
                `employee-row-${employeeId}`
            );

            row.remove();

            const remainingRows =
                document.querySelectorAll(
                    "#employee-table-body tr"
                );

            if (remainingRows.length === 0) {

                document.getElementById(
                    "employee-table-body"
                ).innerHTML = `
                    <tr>
                        <td colspan="4">
                            No employees found.
                        </td>
                    </tr>
                `;
            }

            alert(data.message);
        }
    })

    .catch(error => {

        console.error("Error:", error);

        alert(
            "Something went wrong. Employee was not deleted."
        );
    });
}